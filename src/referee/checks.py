"""The four mechanical checks on a completed review (Scott's v4 plan, Stage 2).

1. form complete: every row rated with a permitted level, a permitted
   recommendation, both free-text fields present, at least one critique.
2. every critique names a location.
3. every Poor or Marginal score has at least one critique bearing on that row.
4. nothing fabricated, as far as text matching can tell: every quoted passage
   is found in the manuscript text; every number in a critique appears in the
   manuscript; every author-year citation in a critique appears in the
   manuscript or is declared as an external reference. External references
   are listed for a person to verify; the check cannot confirm they exist.

Each check reports pass or fail with the items that failed. Failures are
recorded, not fixed, so that no critique is removed from the study record.
"""

import json
import re
import unicodedata
from pathlib import Path

from .form import load_form


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("­", "")
    s = re.sub(r"-\s*\n\s*", "", s)  # hyphenation at line ends
    s = re.sub(r"\s+", " ", s)
    # PDF text extraction inserts stray spaces around punctuation and brackets
    s = re.sub(r"\s+([,.;:!?)\]])", r"\1", s)
    s = re.sub(r"([(\[])\s+", r"\1", s)
    s = re.sub(r"\s*-\s*", "-", s)
    return s.strip().lower()


def manuscript_text(pdf: Path) -> str:
    import pypdf

    r = pypdf.PdfReader(str(pdf))
    return "\n".join((p.extract_text() or "") for p in r.pages)


NUMBER = re.compile(r"(?<![\w.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?![\w])")
CITATION = re.compile(
    r"\b([A-Z][A-Za-z'\-]+(?:\s+(?:&|and)\s+[A-Z][A-Za-z'\-]+|\s+et al\.?)?)[,\s]*\(?\s*((?:19|20)\d{2}[a-z]?)\)?"
)


def numbers_in(s: str) -> set[str]:
    return {m.group(0).replace(",", "") for m in NUMBER.finditer(s)}


def run_checks(review: dict, pdf: Path, form: dict | None = None) -> dict:
    form = form or load_form()
    text = manuscript_text(pdf)
    ntext = normalize(text)
    nums_in_ms = numbers_in(text)
    levels = set(form["rating_levels"])
    explain = set(form["ratings_requiring_explanation"])
    row_ids = [r["id"] for r in form["rows"]]
    critiques = review.get("critiques") or []

    # 1. form complete
    missing = []
    ratings = review.get("ratings") or {}
    for rid in row_ids:
        if ratings.get(rid) not in levels:
            missing.append(f"row '{rid}': rating is {ratings.get(rid)!r}")
    if review.get("recommendation") not in set(form["recommendation_options"]):
        missing.append(f"recommendation is {review.get('recommendation')!r}")
    for field in ("comments_to_editor", "summary_for_authors"):
        if not (review.get(field) or "").strip():
            missing.append(f"{field} is empty")
    if not critiques:
        missing.append("no critiques")
    c1 = {"name": "form complete", "pass": not missing, "failures": missing}

    # 2. every critique names a location
    no_loc = [c.get("id") for c in critiques if not (c.get("location") or "").strip()]
    c2 = {"name": "every critique names a location", "pass": not no_loc, "failures": [f"critique {i}" for i in no_loc]}

    # 3. every Poor or Marginal score has a critique
    unexplained = []
    for rid in row_ids:
        if ratings.get(rid) in explain and not any(rid in (c.get("rows") or []) for c in critiques):
            unexplained.append(f"row '{rid}' rated {ratings[rid]} with no critique bearing on it")
    c3 = {"name": "every Poor or Marginal score has a critique", "pass": not unexplained, "failures": unexplained}

    # 4. nothing fabricated (text matching)
    quote_fail, number_fail, cite_fail, external = [], [], [], []
    declared_external = {normalize(e.get("citation", "")) for e in (review.get("external_references") or [])}
    for c in critiques:
        cid = c.get("id")
        q = (c.get("quote") or "").strip()
        if q:
            nq = normalize(q).strip('"').strip("'").strip(".")
            if nq and nq not in ntext:
                # allow a quote to be matched in two halves across a line or page break
                half = len(nq) // 2
                a, b = nq[:half].strip(), nq[half:].strip()
                if not (len(a) > 15 and len(b) > 15 and a in ntext and b in ntext):
                    quote_fail.append({"critique": cid, "quote": q})
        else:
            quote_fail.append({"critique": cid, "quote": "(no quote given)"})
        body = f"{c.get('text', '')} {c.get('location', '')}"
        for n in numbers_in(c.get("text", "")):
            if n not in nums_in_ms and float(n) not in {1.0, 2.0, 3.0}:
                number_fail.append({"critique": cid, "number": n})
        for m in CITATION.finditer(c.get("text", "")):
            name, year = m.group(1), m.group(2)
            surname = normalize(name.split()[0])
            if surname in ntext and year in text:
                continue
            key = normalize(f"{name} {year}")
            if any(surname in d and year in d for d in declared_external):
                external.append({"critique": cid, "citation": f"{name} ({year})", "status": "declared external; verify by hand"})
            else:
                cite_fail.append({"critique": cid, "citation": f"{name} ({year})"})
    for e in review.get("external_references") or []:
        external.append({"critique": e.get("used_in_critique"), "citation": e.get("citation"), "status": "declared external; verify by hand"})
    c4 = {
        "name": "nothing fabricated (text matching)",
        "pass": not (quote_fail or number_fail or cite_fail),
        "failures": {
            "quotes not found in manuscript": quote_fail,
            "numbers not found in manuscript": number_fail,
            "citations not in manuscript and not declared external": cite_fail,
        },
        "for_human_verification": external,
    }

    return {"checks": [c1, c2, c3, c4], "all_pass": all(c["pass"] for c in (c1, c2, c3, c4)), "critique_count": len(critiques)}


def render_checks(results: dict, title: str) -> str:
    out = [f"# {title}", "", f"Critiques: {results['critique_count']}. All checks pass: {'yes' if results['all_pass'] else 'no'}.", ""]
    for c in results["checks"]:
        out.append(f"## {c['name']}: {'pass' if c['pass'] else 'FAIL'}")
        out.append("")
        f = c["failures"]
        if isinstance(f, dict):
            for k, items in f.items():
                if items:
                    out.append(f"- {k}:")
                    for it in items:
                        out.append(f"    - critique {it.get('critique')}: {it.get('quote') or it.get('number') or it.get('citation')}")
        else:
            for it in f:
                out.append(f"- {it}")
        if c.get("for_human_verification"):
            out.append("- For a person to verify (the check cannot confirm these exist):")
            for it in c["for_human_verification"]:
                out.append(f"    - critique {it.get('critique')}: {it.get('citation')}")
        out.append("")
    return "\n".join(out)


def check_run(run_dir: Path, pdf: Path) -> dict:
    form = load_form()
    summary = {}
    # Review files are named review-<reviewer>.*: a bare "claude.md" would be read
    # as an agent-instruction file on case-insensitive filesystems.
    for j in sorted(Path(run_dir).glob("review-*.json")):
        name = j.stem[len("review-"):]
        review = json.loads(j.read_text(encoding="utf-8"))
        res = run_checks(review, pdf, form)
        (Path(run_dir) / f"checks-{name}.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
        (Path(run_dir) / f"checks-{name}.md").write_text(render_checks(res, f"Mechanical checks: {name}"), encoding="utf-8", newline="\n")
        summary[name] = res
    return summary
