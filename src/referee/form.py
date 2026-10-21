"""The review form template and the assembly of the reviewer prompt from it."""

import json
import re
from pathlib import Path

from .config import PATHS


def load_form(path: Path | None = None) -> dict:
    return json.loads((path or PATHS["form"]).read_text(encoding="utf-8"))


def journal_statements(folder: Path | None = None) -> str:
    folder = folder or PATHS["journal_sources"]
    parts = []
    for f in sorted(folder.glob("*.md")):
        if f.name.lower() == "readme.md":
            continue
        body = re.sub(r"<!--.*?-->", "", f.read_text(encoding="utf-8"), flags=re.S)
        parts.append(re.sub(r"\n{3,}", "\n\n", body).strip())
    if not parts:
        return "(No journal statements are on file.)"
    return "\n\n".join(parts)


def assemble_prompt(form: dict, template_path: Path | None = None) -> str:
    text = (template_path or PATHS["prompt"]).read_text(encoding="utf-8")
    rows = "\n".join(f"- {r['label']} (row id: `{r['id']}`)" for r in form["rows"])
    schema = ", ".join(f'"{r["id"]}": "<rating>"' for r in form["rows"])
    fills = {
        "journal_statements": journal_statements(),
        "rating_levels": ", ".join(form["rating_levels"]),
        "form_rows": rows,
        "recommendation_options": ", ".join(form["recommendation_options"]),
        "ratings_requiring_explanation": " or ".join(form["ratings_requiring_explanation"]),
        "ratings_schema": schema,
        "row_ids": ", ".join(r["id"] for r in form["rows"]),
    }
    for k, v in fills.items():
        text = text.replace("{{" + k + "}}", v)
    leftover = [t for t in text.split("{{")[1:]]
    if leftover:
        raise ValueError("unfilled placeholder in prompt: {{" + leftover[0].split("}}")[0] + "}}")
    return text


def render_review(form: dict, review: dict, title: str) -> str:
    """Render a parsed review as the completed form, in markdown."""
    labels = {r["id"]: r["label"] for r in form["rows"]}
    out = [f"# {title}", ""]
    out += ["| Row | Rating |", "|:--|:--|"]
    for r in form["rows"]:
        out.append(f"| {r['label']} | {review.get('ratings', {}).get(r['id'], '')} |")
    out += ["", f"**Recommendation:** {review.get('recommendation', '')}", ""]
    out += ["## Confidential comments to the editor", "", review.get("comments_to_editor", "").strip(), ""]
    out += ["## Comments to the author", "", review.get("summary_for_authors", "").strip(), ""]
    for c in review.get("critiques", []):
        rows = ", ".join(labels.get(x, x) for x in c.get("rows", []))
        out.append(f"{c.get('id')}. **{c.get('location', '')}.** {c.get('text', '').strip()}")
        if c.get("quote"):
            out.append(f"   > {c['quote'].strip()}")
        if rows:
            out.append(f"   *Rows: {rows}*")
        out.append("")
    ext = review.get("external_references") or []
    if ext:
        out += ["## References cited that the manuscript does not cite", ""]
        for e in ext:
            out.append(f"- {e.get('citation', '')} (critique {e.get('used_in_critique', '')})")
        out.append("")
    return "\n".join(out)
