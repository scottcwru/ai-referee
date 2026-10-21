"""Manuscript in, two independent completed review forms out, with a run record.

Each reviewer is called with the same assembled prompt and the manuscript PDF.
The manifest records the model string the API served, settings, token usage,
fees, elapsed time, request ids, failures, and retries. Keys are never logged.
"""

import base64
import hashlib
import json
import re
import time
import traceback
from collections.abc import Iterable
from datetime import datetime, timezone
from pathlib import Path

from . import config
from .form import assemble_prompt, load_form, render_review
from .keys import MissingKey, load_keys, require


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def pdf_pages(p: Path) -> int:
    import pypdf

    return len(pypdf.PdfReader(str(p)).pages)


def parse_json_output(text: str) -> dict:
    """Parse the model's JSON, tolerating a fenced code block or stray prose."""
    s = text.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", s, re.S)
    if m:
        s = m.group(1)
    else:
        i, j = s.find("{"), s.rfind("}")
        if i >= 0 and j > i:
            s = s[i : j + 1]
    return json.loads(s)


def cost(prices: dict, usage: dict) -> float:
    per = {k: v / 1_000_000 for k, v in prices.items()}
    c = usage.get("input_tokens", 0) * per.get("input", 0)
    c += usage.get("output_tokens", 0) * per.get("output", 0)
    c += usage.get("cache_write_tokens", 0) * per.get("cache_write", 0)
    c += usage.get("cache_read_tokens", 0) * per.get("cache_read", 0)
    return round(c, 4)


def safe_error(e: Exception, secrets: Iterable[str] = ()) -> str:
    """Redact loaded credentials and known key formats before truncating an error."""
    msg = str(e)
    for secret in sorted({s for s in secrets if s}, key=len, reverse=True):
        msg = msg.replace(secret, "[redacted]")
    for pattern in (
        r"sk-[A-Za-z0-9_\-]{8,}",
        r"AIza[0-9A-Za-z_-]{35,}",
        r"\bgh[pousr]_[A-Za-z0-9]{30,}",
        r"github_pat_[A-Za-z0-9_]{20,}",
    ):
        msg = re.sub(pattern, "[redacted]", msg)
    return f"{type(e).__name__}: {msg[:400]}"


# --- vendor calls -------------------------------------------------------------


def call_anthropic(spec: dict, api_key: str, prompt: str, pdf_b64: str) -> dict:
    import anthropic

    client = anthropic.Anthropic(api_key=api_key, max_retries=2)
    s = spec["settings"]
    with client.messages.stream(
        model=spec["model"],
        max_tokens=s["max_tokens"],
        system=prompt,
        output_config={"effort": s["effort"]},
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64},
                        "title": "manuscript.pdf",
                    },
                    {"type": "text", "text": "The manuscript is attached. Complete the review form as instructed."},
                ],
            }
        ],
    ) as stream:
        msg = stream.get_final_message()
    text = "".join(b.text for b in msg.content if b.type == "text")
    u = msg.usage
    return {
        "model_served": msg.model,
        "request_id": getattr(msg, "_request_id", None),
        "stop_reason": msg.stop_reason,
        "usage": {
            "input_tokens": u.input_tokens,
            "output_tokens": u.output_tokens,
            "cache_write_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
            "cache_read_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
        },
        "raw_text": text,
    }


def call_openai(spec: dict, api_key: str, prompt: str, pdf_b64: str) -> dict:
    import openai

    client = openai.OpenAI(api_key=api_key, max_retries=2)
    s = spec["settings"]
    r = client.responses.create(
        model=spec["model"],
        instructions=prompt,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "filename": "manuscript.pdf",
                        "file_data": "data:application/pdf;base64," + pdf_b64,
                    },
                    {"type": "input_text", "text": "The manuscript is attached. Complete the review form as instructed."},
                ],
            }
        ],
        reasoning={"effort": s["reasoning_effort"]},
        max_output_tokens=s["max_output_tokens"],
        store=s["store"],
    )
    u = r.usage
    cached = 0
    if getattr(u, "input_tokens_details", None) is not None:
        cached = getattr(u.input_tokens_details, "cached_tokens", 0) or 0
    reasoning = 0
    if getattr(u, "output_tokens_details", None) is not None:
        reasoning = getattr(u.output_tokens_details, "reasoning_tokens", 0) or 0
    return {
        "model_served": r.model,
        "request_id": getattr(r, "_request_id", None) or r.id,
        "stop_reason": r.status,
        "usage": {
            "input_tokens": (u.input_tokens or 0) - cached,
            "output_tokens": u.output_tokens or 0,
            "cache_read_tokens": cached,
            "reasoning_tokens_included_in_output": reasoning,
        },
        "raw_text": r.output_text,
    }


CALLERS = {"anthropic": call_anthropic, "openai": call_openai}
KEY_NAMES = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY"}


# --- the run ------------------------------------------------------------------


def run(manuscript: Path, run_dir: Path | None = None, reviewers: list[str] | None = None, keys_file: Path | None = None) -> Path:
    manuscript = Path(manuscript)
    form = load_form()
    prompt = assemble_prompt(form)
    keys, keys_path = load_keys(keys_file)

    run_id = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    run_dir = Path(run_dir) if run_dir else config.PATHS["runs"] / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "prompt-as-sent.md").write_text(prompt, encoding="utf-8", newline="\n")

    pdf_bytes = manuscript.read_bytes()
    pdf_b64 = base64.standard_b64encode(pdf_bytes).decode("ascii")

    manifest = {
        "run_id": run_id,
        "started_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "manuscript": {
            "file": manuscript.name,
            "sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            "bytes": len(pdf_bytes),
            "pages": pdf_pages(manuscript),
            "note": "This fingerprint identifies the file reviewed.",
        },
        "prompt": {"file": "prompt-as-sent.md", "sha256": sha256_text(prompt), "template": "reviewer/prompt.md"},
        "form": {"file": "reviewer/form/template.json", "sha256": sha256_file(config.PATHS["form"])},
        "keys_file": str(keys_path.relative_to(config.ROOT)) if keys_path.is_relative_to(config.ROOT) else "outside repository",
        "price_source": config.PRICE_SOURCE,
        "reviewers": {},
    }

    for name in reviewers or list(config.REVIEWERS):
        spec = config.REVIEWERS[name]
        rec = {
            "vendor": spec["vendor"],
            "model_requested": spec["model"],
            "settings": spec["settings"],
            "price_per_million": spec["price_per_million"],
            "attempts": [],
            "status": "not run",
        }
        manifest["reviewers"][name] = rec
        try:
            api_key = require(keys, KEY_NAMES[spec["vendor"]])
        except MissingKey as e:
            rec["status"] = "failed"
            rec["attempts"].append({"error": safe_error(e, keys.values()), "elapsed_seconds": 0})
            continue

        t0 = time.perf_counter()
        attempt = {"started_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        try:
            result = CALLERS[spec["vendor"]](spec, api_key, prompt, pdf_b64)
            attempt["elapsed_seconds"] = round(time.perf_counter() - t0, 1)
            attempt.update({k: v for k, v in result.items() if k != "raw_text"})
            (run_dir / f"review-{name}.raw.txt").write_text(result["raw_text"], encoding="utf-8", newline="\n")
            rec["usage"] = result["usage"]
            rec["cost_usd"] = cost(spec["price_per_million"], result["usage"])
            rec["elapsed_seconds"] = attempt["elapsed_seconds"]
            rec["model_served"] = result["model_served"]
            try:
                review = parse_json_output(result["raw_text"])
                (run_dir / f"review-{name}.json").write_text(json.dumps(review, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
                (run_dir / f"review-{name}.md").write_text(
                    render_review(form, review, f"Review by {name} ({result['model_served']})"), encoding="utf-8", newline="\n"
                )
                rec["status"] = "completed"
            except (json.JSONDecodeError, ValueError) as e:
                rec["status"] = "completed; output not parseable as JSON"
                attempt["parse_error"] = safe_error(e, keys.values())
        except Exception as e:  # recorded, never raised past the run
            attempt["elapsed_seconds"] = round(time.perf_counter() - t0, 1)
            attempt["error"] = safe_error(e, keys.values())
            attempt["sdk_retries"] = "up to 2 automatic retries by the SDK on 408/409/429/5xx"
            rec["status"] = "failed"
        rec["attempts"].append(attempt)

    manifest["finished_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    manifest["total_cost_usd"] = round(sum(r.get("cost_usd", 0) for r in manifest["reviewers"].values()), 4)
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
    return run_dir
