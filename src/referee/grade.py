"""Code every critique in a set of reviews: category, dimension, checkability, form row, location.

Two steps, both on the grader model (a family neither reviewer uses):
  1. segment: split each review into critiques (grader/prompt-segment.md);
  2. code: show each critique alone, with one sentence of context either side,
     and code it by the codebook and the coding instructions (grader/prompt.md).

Inputs: the AI reviews of a recorded reviewer run (their comments to the author)
and the human reports from a private folder. Output: one coded row per critique
with codes, location, and word count. The text of a human critique is written
only to a work folder inside the private folder, never to the repository.
"""

import csv
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from . import config
from .form import load_form
from .keys import load_keys, require
from .review import parse_json_output, safe_error, sha256_text
from .segment import context_for, load_segment_prompt

# --- the grader prompt --------------------------------------------------------


def codebook_codes(codebook: str) -> set[str]:
    codes = set()
    for line in codebook.splitlines():
        m = re.match(r"\|\s*([A-Z][A-Z.]+[A-Z])\s*\|", line)
        if m and m.group(1) not in {"CODE"}:
            codes.add(m.group(1))
    return codes


def instructions_with_rulings(text: str) -> str:
    """The instructions as written, with the open-questions section retitled as questions that have been ruled on."""
    text = text.replace("## Questions for Scott", "## Questions that were open, with the rulings that settled them")
    text = text.replace("Each needs a ruling before the agreement test. Options are listed without a recommendation.",
                        "The rulings below settle each question; the lettered options are kept so that the ruling can be read against them.")
    return text.strip()


def grader_prompt_template() -> tuple[str, dict]:
    form = load_form()
    codebook = config.PATHS["codebook"].read_text(encoding="utf-8")
    instructions = instructions_with_rulings(config.PATHS["coding_instructions"].read_text(encoding="utf-8"))
    text = config.PATHS["grader_prompt"].read_text(encoding="utf-8")
    rows = "\n".join(f"- {r['label']} (row id: `{r['id']}`)" for r in form["rows"])
    text = (
        text.replace("{{instructions}}", instructions)
        .replace("{{codebook}}", codebook)
        .replace("{{form_rows}}", rows)
        .replace("{{row_ids}}", ", ".join(r["id"] for r in form["rows"]))
    )
    meta = {
        "codebook_sha256": sha256_text(codebook),
        "instructions_sha256": sha256_text(config.PATHS["coding_instructions"].read_text(encoding="utf-8")),
        "codes": sorted(codebook_codes(codebook)),
        "row_ids": [r["id"] for r in form["rows"]],
    }
    return text, meta


def fill_critique(template: str, critique: str, before: str, after: str) -> str:
    return (
        template.replace("{{critique}}", critique)
        .replace("{{before}}", before or "(start of report)")
        .replace("{{after}}", after or "(end of report)")
    )


# --- the grader model ---------------------------------------------------------


class Grader:
    def __init__(self, api_key: str):
        from google import genai

        self.client = genai.Client(api_key=api_key)
        self._secrets = (api_key,)
        self.spec = config.GRADER
        self.calls = []
        self.raw_dir: Path | None = None

    def ask(self, prompt: str, label: str) -> dict:
        from google.genai import types

        t0 = time.perf_counter()
        rec = {"label": label, "started_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "retries": 0}
        try:
            for attempt in range(6):
                try:
                    resp = self.client.models.generate_content(
                        model=self.spec["model"],
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            response_mime_type=self.spec["settings"]["response_mime_type"],
                            max_output_tokens=self.spec["settings"]["max_output_tokens"],
                            thinking_config=types.ThinkingConfig(thinking_level=self.spec["settings"]["thinking_level"]),
                        ),
                    )
                    break
                except Exception as e:  # retry only overload and rate-limit responses
                    code = getattr(e, "code", None) or getattr(e, "status_code", None)
                    if code in (429, 500, 503) and attempt < 5:
                        rec["retries"] += 1
                        time.sleep(min(60, 5 * 2**attempt))
                        continue
                    raise
            u = resp.usage_metadata
            finish = None
            if getattr(resp, "candidates", None):
                finish = str(getattr(resp.candidates[0], "finish_reason", None))
            rec.update(
                {
                    "model_served": getattr(resp, "model_version", None) or self.spec["model"],
                    "finish_reason": finish,
                    "input_tokens": (u.prompt_token_count or 0) - (getattr(u, "cached_content_token_count", 0) or 0),
                    "cache_read_tokens": getattr(u, "cached_content_token_count", 0) or 0,
                    "output_tokens": (u.candidates_token_count or 0) + (getattr(u, "thoughts_token_count", 0) or 0),
                    "elapsed_seconds": round(time.perf_counter() - t0, 1),
                }
            )
            self.calls.append(rec)
            try:
                return parse_json_output(resp.text or "")
            except (json.JSONDecodeError, ValueError):
                if self.raw_dir:  # keep the unparseable output for diagnosis, in the private work folder
                    (self.raw_dir / f"{label.replace(':', '-')}.unparsed.txt").write_text(resp.text or "", encoding="utf-8")
                raise
        except Exception as e:
            rec["error"] = safe_error(e, self._secrets)
            rec["elapsed_seconds"] = round(time.perf_counter() - t0, 1)
            self.calls.append(rec)
            raise

    def totals(self) -> dict:
        p = {k: v / 1_000_000 for k, v in self.spec["price_per_million"].items()}
        ok = [c for c in self.calls if "error" not in c]
        inp = sum(c["input_tokens"] for c in ok)
        cr = sum(c["cache_read_tokens"] for c in ok)
        out = sum(c["output_tokens"] for c in ok)
        return {
            "calls": len(self.calls),
            "failed_calls": len(self.calls) - len(ok),
            "input_tokens": inp,
            "cache_read_tokens": cr,
            "output_tokens": out,
            "elapsed_seconds": round(sum(c["elapsed_seconds"] for c in self.calls), 1),
            "cost_usd": round(inp * p["input"] + cr * p.get("cache_read", 0) + out * p["output"], 4),
            "models_served": sorted({c["model_served"] for c in ok}),
        }


# --- inputs -------------------------------------------------------------------


def ai_review_text(run_dir: Path, name: str) -> str:
    """The AI reviewer's comments to the author, as the grader sees them: summary then critiques, no row tags."""
    rev = json.loads((run_dir / f"review-{name}.json").read_text(encoding="utf-8"))
    parts = [rev.get("summary_for_authors", "").strip()]
    for c in rev.get("critiques", []):
        loc = c.get("location", "").strip()
        parts.append(f"{c.get('id')}. {loc + '. ' if loc else ''}{c.get('text', '').strip()}")
    return "\n\n".join(p for p in parts if p)


def human_review_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# --- the run ------------------------------------------------------------------

FIELDS = [
    "review", "arm", "critique", "grader_segment_order", "location_named", "words",
    "dimension", "proposed_label", "category", "checkability", "form_row", "location",
    "verbatim_match", "note", "code_valid",
]


def grade(reviewer_run: Path, human_dir: Path | None, out_dir: Path | None = None, keys_file: Path | None = None,
          humans: tuple[str, ...] = ("reviewer1", "reviewer2", "reviewer3", "decision-letter")) -> Path:
    keys, keys_path = load_keys(keys_file)
    grader = Grader(require(keys, "GOOGLE_API_KEY"))
    template, meta = grader_prompt_template()
    valid_codes = set(meta["codes"]) | {"NEW"}

    run_id = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    out_dir = Path(out_dir) if out_dir else config.PATHS["grader_runs"] / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    work = (human_dir / "grader-work" / run_id) if human_dir else None  # private: holds human critique text
    if work:
        work.mkdir(parents=True, exist_ok=True)
        grader.raw_dir = work

    reviews = []  # (review id, arm, text, public)
    rm = json.loads((reviewer_run / "manifest.json").read_text(encoding="utf-8"))
    for name in rm["reviewers"]:
        if (reviewer_run / f"review-{name}.json").exists():
            reviews.append((name, "ai", ai_review_text(reviewer_run, name), True))
    if human_dir:
        for h in humans:
            p = human_dir / f"{h}.txt"
            if p.exists():
                reviews.append((h, "editor" if h == "decision-letter" else "human", human_review_text(p), False))

    rows, segments_public, failures = [], {}, []
    for rid, arm, text, public in reviews:
        try:
            seg = grader.ask(load_segment_prompt(text), f"segment:{rid}")
        except Exception as e:
            failures.append({"review": rid, "step": "segment", "error": safe_error(e, keys.values())})
            continue
        crits = seg.get("critiques") or []
        if public:
            segments_public[rid] = crits
        elif work:
            (work / f"{rid}-segments.json").write_text(json.dumps(crits, indent=2, ensure_ascii=False), encoding="utf-8")
        for k, c in enumerate(crits, 1):
            ctext = (c.get("text") or "").strip()
            ctx = context_for(text, ctext)
            row = {
                "review": rid, "arm": arm, "critique": c.get("id", k), "grader_segment_order": k,
                "location_named": "no" if (c.get("location") or "none").strip().lower() == "none" else "yes",
                "words": len(ctext.split()), "verbatim_match": "yes" if ctx["verbatim_match"] else "no",
            }
            try:
                coded = grader.ask(fill_critique(template, ctext, ctx["before"], ctx["after"]), f"code:{rid}:{k}")
            except Exception as e:
                failures.append({"review": rid, "step": f"code:{k}", "error": safe_error(e, keys.values())})
                row.update({f: "" for f in FIELDS if f not in row})
                row["note"] = "grader call failed"
                rows.append(row)
                continue
            dim = (coded.get("dimension") or "").strip()
            row.update(
                {
                    "dimension": dim,
                    "proposed_label": (coded.get("proposed_label") or "").strip(),
                    "category": (coded.get("category") or "").strip().lower(),
                    "checkability": (coded.get("checkability") or "").strip().lower(),
                    "form_row": (coded.get("form_row") or "none").strip().lower(),
                    "location": (coded.get("location") or "none").strip(),
                    "note": (coded.get("note") or "").strip(),
                    "code_valid": "yes" if dim in valid_codes else "no",
                }
            )
            if not public and row["note"]:
                # a coder note can paraphrase a human critique; keep it out of the repository
                if work:
                    with (work / "private-notes.csv").open("a", encoding="utf-8", newline="") as pf:
                        csv.writer(pf).writerow([rid, row["critique"], row["note"]])
                row["note"] = "(coder note held in the private work folder)"
            rows.append(row)

    with (out_dir / "coded-critiques.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    (out_dir / "ai-critique-segments.json").write_text(json.dumps(segments_public, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
    (out_dir / "grader-prompt-as-sent.md").write_text(template, encoding="utf-8", newline="\n")

    manifest = {
        "run_id": run_id,
        "reviewer_run": reviewer_run.name,
        "grader": {k: config.GRADER[k] for k in ("vendor", "model", "settings", "price_per_million", "price_note")},
        "prompt": {"template": "grader/prompt.md", "segment_template": "grader/prompt-segment.md",
                   "as_sent_sha256": sha256_text(template), **{k: meta[k] for k in ("codebook_sha256", "instructions_sha256")}},
        "reviews_coded": [{"review": rid, "arm": arm, "words": len(text.split()), "text_in_repository": public} for rid, arm, text, public in reviews],
        "keys_file": str(keys_path.relative_to(config.ROOT)) if keys_path.is_relative_to(config.ROOT) else "outside repository",
        "totals": grader.totals(),
        "failures": failures,
        "calls": grader.calls,
        "finished_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
    return out_dir
