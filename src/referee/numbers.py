"""Write the sample's prototype numbers from the recorded runs. Nobody types a result.

Two versions: sample/prototype-numbers.md, published, covers the AI reviews only; the full
version, with the referee reports and decision letter, is in sample/confidential/ and goes in
the technical appendix (decision of 2026-10-21).
"""

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from . import config
from .form import load_form


def pct(n: int, d: int) -> str:
    return f"{100 * n / d:.0f}%" if d else "n/a"


def shares(rows: list[dict]) -> dict:
    c = Counter(r["category"] for r in rows if r.get("category"))
    rc = c["rigor"] + c["contribution"]
    return {
        "n": len(rows), "rigor": c["rigor"], "contribution": c["contribution"], "other": c["other"],
        "uncoded": len(rows) - c["rigor"] - c["contribution"] - c["other"],
        "rigor_share": (c["rigor"] / rc) if rc else None,
    }


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def fmt_share(x):
    return f"{100 * x:.0f}%" if x is not None else "n/a"


def manuscript_fingerprints(rm: dict) -> dict:
    """The reviewed and posted fingerprints of the sample manuscript, checked against the files.

    The reviewers read the manuscript with its journal ID on the cover; the posted copy has the
    ID blanked. Both fingerprints live in sample/manuscript/fingerprints.json.
    """
    import hashlib

    fp = json.loads(config.PATHS["manuscript_fingerprints"].read_text(encoding="utf-8"))
    if rm["manuscript"]["sha256"] not in {fp["reviewed_sha256"], fp["posted_sha256"]}:
        raise ValueError("fingerprints.json does not match the manuscript fingerprint in the run manifest")
    posted = hashlib.sha256(config.PATHS["manuscript"].read_bytes()).hexdigest()
    if fp["posted_sha256"] != posted:
        raise ValueError("fingerprints.json does not match sample/manuscript/manuscript.pdf")
    return fp


RESTRICTED_NOTE = (
    "This grader run did not code the sample's referee reports and decision letter, which are restricted inputs "
    "(see 'Reproducing the sample results' in README.md), so only the public numbers, covering the AI reviews, "
    "were written. With the reports, `ref grade <reviewer run> --human-dir <folder>` codes them and writes the full numbers."
)


def restricted_inputs_present() -> bool:
    """Whether this copy holds the sample's editorial facts (the working repository does; the public one does not)."""
    return config.PATHS["sample_article"].exists()


def is_sample_run(grader_run: Path) -> bool:
    """Whether a grader run codes reviews of the sample manuscript, the only article the numbers describe."""
    gm = json.loads((Path(grader_run) / "manifest.json").read_text(encoding="utf-8"))
    rm = json.loads((config.PATHS["runs"] / gm["reviewer_run"] / "manifest.json").read_text(encoding="utf-8"))
    fp = json.loads(config.PATHS["manuscript_fingerprints"].read_text(encoding="utf-8"))
    return rm["manuscript"]["sha256"] in {fp["reviewed_sha256"], fp["posted_sha256"]}


WITHHELD_NOTE = (
    "The sample article's referee reports and decision letter are private communications between "
    "Organization Science, the authors, and the referees, so their coded critiques, the editor's decision, "
    "and every comparison with them are in the technical appendix submitted with the proposal, "
    "not in the public repository."
)


def write_numbers(grader_run: Path, out: Path | None = None) -> Path:
    """Write the public numbers (AI reviews only) and the full numbers (with the journal's reviews).

    The full version, in the confidential folder, is the one the appendix and the proposal use.
    Returns the path of the public version.
    """
    grader_run = Path(grader_run)
    gm = json.loads((grader_run / "manifest.json").read_text(encoding="utf-8"))
    reviewer_run = config.PATHS["runs"] / gm["reviewer_run"]
    rm = json.loads((reviewer_run / "manifest.json").read_text(encoding="utf-8"))
    form = load_form()
    article = json.loads(config.PATHS["sample_article"].read_text(encoding="utf-8")) if restricted_inputs_present() else None

    with (grader_run / "coded-critiques.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    by_review = defaultdict(list)
    for r in rows:
        by_review[r["review"]].append(r)
    arm_of = {r["review"]: r["arm"] for r in rows}

    ai_names = [n for n in rm["reviewers"] if (reviewer_run / f"review-{n}.json").exists()]
    reviews = {n: json.loads((reviewer_run / f"review-{n}.json").read_text(encoding="utf-8")) for n in ai_names}
    all_human = [n for n, a in arm_of.items() if a == "human"]
    all_editor = [n for n, a in arm_of.items() if a == "editor"]
    # the full numbers need the journal's reviews coded in this run (restricted inputs)
    full = bool(all_human or all_editor)

    arm_shares = {arm: mean([shares(by_review.get(n, []))["rigor_share"] for n in names])
                  for arm, names in (("AI", ai_names), ("human", all_human), ("editor", all_editor))}
    costs = [rm["reviewers"][n]["cost_usd"] for n in ai_names]
    times = [rm["reviewers"][n]["elapsed_seconds"] for n in ai_names]
    fp = manuscript_fingerprints(rm)

    def document(public: bool) -> str:
        human_names = [] if public else all_human
        editor_names = [] if public else all_editor
        L = []
        L += ["# Prototype numbers from the sample article", ""]
        if public:
            L += [f"Generated by `ref numbers` from reviewer run `{rm['run_id']}` and grader run `{gm['run_id']}`. "
                  "One article and its two AI reviews. "
                  "These numbers demonstrate that the pipeline runs and is inspectable; they are not a result of the study.", "",
                  WITHHELD_NOTE, ""]
        else:
            L += [f"Generated by `ref numbers` from reviewer run `{rm['run_id']}` and grader run `{gm['run_id']}`. "
                  "One article, two AI reviews, three human referee reports, and the editor's decision letter. "
                  "These numbers demonstrate that the pipeline runs and is inspectable; they are not a result of the study.", ""]

        # 1. critiques per reviewer
        L += ["## Critiques per reviewer", "", "| Reviewer | Arm | Critiques as the grader segmented them | Critiques as the reviewer numbered them |", "|:--|:--|--:|--:|"]
        for n in ai_names:
            L.append(f"| {n} | AI | {len(by_review.get(n, []))} | {len(reviews[n].get('critiques', []))} |")
        for n in human_names:
            L.append(f"| {n} | human | {len(by_review.get(n, []))} | not numbered |")
        for n in editor_names:
            L.append(f"| {n} | editor | {len(by_review.get(n, []))} | not numbered |")
        L.append("")

        # 2. rigor and contribution shares
        L += ["## Rigor and contribution", "",
              "Rigor share is rigor critiques divided by rigor plus contribution critiques (decision of 2026-09-16). "
              "Critiques coded other (writing and presentation) are excluded from the share and reported separately. "
              "The arm means average the share within reviewer type (decision of 2026-09-17).", "",
              "| Reviewer | Critiques | Rigor | Contribution | Other | Percent rigor | Percent contribution |", "|:--|--:|--:|--:|--:|--:|--:|"]
        for n in ai_names + human_names + editor_names:
            s = shares(by_review.get(n, []))
            L.append(f"| {n} | {s['n']} | {s['rigor']} | {s['contribution']} | {s['other']} | {fmt_share(s['rigor_share'])} | "
                     f"{fmt_share(1 - s['rigor_share']) if s['rigor_share'] is not None else 'n/a'} |")
        L.append("")
        L += [f"- **AI reviews, mean rigor share:** {fmt_share(arm_shares['AI'])}; mean contribution share {fmt_share(1 - arm_shares['AI']) if arm_shares['AI'] is not None else 'n/a'}."]
        if not public:
            L += [f"- **Human reviews, mean rigor share:** {fmt_share(arm_shares['human'])}; mean contribution share {fmt_share(1 - arm_shares['human']) if arm_shares['human'] is not None else 'n/a'}.",
                  f"- **Editor's letter (descriptive, not part of either arm):** rigor share {fmt_share(arm_shares['editor'])}."]
        L.append("")
        shown = ai_names + human_names + editor_names
        uncoded = sum(shares(by_review.get(n, []))["uncoded"] for n in shown)
        invalid = sum(1 for n in shown for r in by_review.get(n, []) if r.get("code_valid") == "no")
        if uncoded or invalid:
            L.append(f"Critiques without a category: {uncoded}. Dimension codes not in the codebook: {invalid}. These are listed in the coded file and were not corrected.")
            L.append("")

        # checkability of rigor critiques
        L += ["### Checkability of rigor critiques", "", "| Arm | Rigor critiques | Checkable error | Omission | Judgment |", "|:--|--:|--:|--:|--:|"]
        for arm, names in (("AI", ai_names), ("human", human_names), ("editor", editor_names)):
            if not names:
                continue
            rr = [r for n in names for r in by_review.get(n, []) if r["category"] == "rigor"]
            c = Counter(r["checkability"] for r in rr)
            L.append(f"| {arm} | {len(rr)} | {c['checkable error']} | {c['omission']} | {c['judgment']} |")
        L.append("")

        # 3. cost and time of one AI review
        L += ["## Cost and time of one AI review", "", "| Reviewer | Model served | Fees | Elapsed | Input tokens | Output tokens |", "|:--|:--|--:|--:|--:|--:|"]
        for n in ai_names:
            r = rm["reviewers"][n]
            L.append(f"| {n} | {r['model_served']} | ${r['cost_usd']:.2f} | {r['elapsed_seconds']:.0f} s | {r['usage']['input_tokens']:,} | {r['usage']['output_tokens']:,} |")
        L += ["", f"Mean per AI review: ${mean(costs):.2f} in fees, {mean(times) / 60:.1f} minutes. Both reviews together: ${sum(costs):.2f}."]
        model = ", ".join(gm["totals"]["models_served"]) or gm["grader"]["model"]
        if public and (full or gm.get("journal_reviews_withheld")):
            L += [f"Grading cost ${gm['totals']['cost_usd']:.2f} ({gm['totals']['elapsed_seconds'] / 60:.1f} minutes of model time) on {model}, "
                  "a total that includes coding the referee reports and decision letter.", ""]
        elif public:
            L += [f"Grading the AI reviews cost ${gm['totals']['cost_usd']:.2f} "
                  f"({gm['totals']['elapsed_seconds'] / 60:.1f} minutes of model time) on {model}.", ""]
        else:
            L += [f"Grading all {len(rows)} critiques in {len(by_review)} reviews cost ${gm['totals']['cost_usd']:.2f} over {gm['totals']['calls']} grader calls "
                  f"({gm['totals']['elapsed_seconds'] / 60:.1f} minutes of model time) on {model}.", ""]

        # 4. scores and recommendations, beside the editor's decision in the full version
        if public:
            L += ["## Form scores and recommendations", ""]
        else:
            L += ["## Form scores and recommendations beside the editor's decision", "",
                  "Human referees' form scores are not in the exported decision letter, so they are unavailable; they are not inferred from the narrative reports (Stage 2 of the v4 plan).", ""]
        cols = ai_names + human_names
        L.append("| Row | " + " | ".join(cols) + " |")
        L.append("|:--|" + "|".join([":--"] * len(cols)) + "|")
        for row in form["rows"]:
            vals = [reviews[n]["ratings"].get(row["id"], "") for n in ai_names] + ["unavailable"] * len(human_names)
            L.append(f"| {row['label']} | " + " | ".join(vals) + " |")
        recs = [reviews[n].get("recommendation", "") for n in ai_names] + ([article["human_recommendations"] if article else "unavailable"] * len(human_names))
        L.append("| **Recommendation** | " + " | ".join(recs) + " |")
        L.append("")
        if not public:
            L += [f"**Editor's decision:** {article['editor_decision']} ({article['decision_date']}). {article['decision_note']}" if article
                  else "**Editor's decision:** not recorded in this copy; it is reported in the technical appendix.", ""]

        # 5. provenance
        where = ("They are not in this repository." if public else
                 "Their coded critiques (codes, locations, and word counts only) are in the working repository and the technical appendix, and are not published.")
        manuscript_note = (
            "The fingerprint above identifies the file the reviewers read; the posted copy has the journal's "
            "manuscript ID blanked on the cover page and nothing else changed"
        )
        if rm["manuscript"]["sha256"] == fp["posted_sha256"]:
            manuscript_note = (
                "This run reviewed the posted copy. Its journal manuscript ID is blanked on the cover page"
            )
        L += ["## Provenance", "",
              f"- Reviewer run `{rm['run_id']}`: prompt SHA-256 `{rm['prompt']['sha256'][:16]}…`, manuscript SHA-256 `{rm['manuscript']['sha256'][:16]}…`, {rm['manuscript']['pages']} pages.",
              f"- Grader run `{gm['run_id']}`: {gm['grader']['vendor']} `{gm['grader']['model']}`; codebook SHA-256 `{gm['prompt']['codebook_sha256'][:16]}…`; instructions SHA-256 `{gm['prompt']['instructions_sha256'][:16]}…`.",
              "- The grader has not been validated against human coders (decision of 2026-09-17); the agreement test runs after selection (decision of 2026-10-09).",
              f"- The anonymized manuscript is in the repository at `sample/manuscript/manuscript.pdf`, with its co-authors' consent. {manuscript_note} (SHA-256 `{fp['posted_sha256'][:16]}…`; both in `sample/manuscript/fingerprints.json`). The referee reports and the decision letter are private communications. {where}", ""]
        return "\n".join(L)

    out = Path(out) if out else config.PATHS["numbers"]
    out.write_text(document(public=True), encoding="utf-8", newline="\n")
    if not full:
        # a public copy: the full numbers need the restricted inputs
        print(RESTRICTED_NOTE)
        return out
    config.PATHS["numbers_full"].parent.mkdir(parents=True, exist_ok=True)
    config.PATHS["numbers_full"].write_text(document(public=False), encoding="utf-8", newline="\n")

    def pct_int(x):
        return f"{100 * x:.0f}" if x is not None else "n/a"

    gen = {
        "what": "Numbers from the recorded sample runs, written by `ref numbers`. The display fields fill the double-braced placeholders in paper/proposal.md at render time. Confidential: the human fields come from the sample's referee reports.",
        "reviewer_run": rm["run_id"], "grader_run": gm["run_id"],
        "ai_critiques": {n: len(by_review.get(n, [])) for n in ai_names},
        "ai_rigor_share_mean": arm_shares["AI"], "human_rigor_share_mean": arm_shares["human"],
        "ai_review_cost_usd_mean": mean(costs), "ai_review_minutes_mean": (mean(times) or 0) / 60,
        # display fields
        **{f"{n}_critiques": len(by_review.get(n, [])) for n in ai_names},
        "ai_rigor_percent": pct_int(arm_shares["AI"]),
        "ai_contribution_percent": pct_int(1 - arm_shares["AI"]) if arm_shares["AI"] is not None else "n/a",
        "human_rigor_percent": pct_int(arm_shares["human"]),
        "human_contribution_percent": pct_int(1 - arm_shares["human"]) if arm_shares["human"] is not None else "n/a",
        "human_review_count": {1: "one", 2: "two", 3: "three", 4: "four"}.get(len(all_human), str(len(all_human))),
        "ai_review_cost_usd": f"{mean(costs):.2f}",
        "ai_review_minutes": f"{(mean(times) or 0) / 60:.1f}",
    }
    config.PATHS["sample_numbers"].write_text(json.dumps(gen, indent=2), encoding="utf-8", newline="\n")
    return out
