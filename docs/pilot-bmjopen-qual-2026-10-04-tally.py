"""Tally the BMJ Open qualitative pilot codes; prints the memo's tables."""
import csv
from collections import Counter
from pathlib import Path

here = Path(__file__).parent
rows = list(csv.DictReader(open(here / "pilot-bmjopen-qual-2026-10-04-codes.csv")))
sample = list(csv.DictReader(open(here / "pilot-bmjopen-qual-2026-10-04-sample.csv")))
coded = [s for s in sample if s["status"] == "coded"]
print(f"papers {len(coded)}, first-round reports {sum(int(s['first_round_reports']) for s in coded)}, "
      f"reports with critiques {len({(r['pmcid'], r['report']) for r in rows})}, critiques {len(rows)}")
for q in ("y", "n"):
    sub = [r for r in rows if r["qual"] == q]
    print(f"qual={q}: {len(sub)} critiques, {sum(r['fit'] == 'clean' for r in sub)} clean, "
          f"{sum(r['fit'] == 'stretch' for r in sub)} stretch, {sum(r['fit'] == 'none' for r in sub)} none")
print("\nstretch gaps (critiques, papers):")
st = [r for r in rows if r["fit"] != "clean"]
for gap, k in Counter(r["gap"] for r in st).most_common():
    print(f"| {gap} | {k} | {len({r['pmcid'] for r in st if r['gap'] == gap})} |")
print("\nqualitative-specific critiques, by entry (clean / stretch):")
qy = [r for r in rows if r["qual"] == "y"]
for entry, k in Counter(r["entry"] for r in qy).most_common():
    c = sum(r["entry"] == entry and r["fit"] == "clean" for r in qy)
    print(f"| {entry} | {c} | {k - c} |")
methods = {"Appropriateness of Design", "Sample selection", "Appropriateness of Analysis and Interpretation",
           "Validity and reliability of measures", "Construct validity", "Construct validity of measures",
           "Construct validity of manipulations", "Reliability", "Participant state: order, practice, fatigue, or inattention",
           "Reactive arrangements", "Internal validity", "Alternative explanation or confound",
           "Causal claim rests on a measured, not manipulated, variable", "Analysis plan or model not specified",
           "Robustness", "Full disclosure", "Process or findings not described", "Preregistration", "Research ethics", "Methods"}
mr = [r for r in rows if r["entry"] in methods]
print(f"\nMethods block: {len(mr)} of {len(rows)} ({len(mr) / len(rows):.0%}); stretched {sum(r['fit'] != 'clean' for r in mr)}")
