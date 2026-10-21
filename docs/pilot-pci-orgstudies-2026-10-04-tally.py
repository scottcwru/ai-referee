"""Tally the PCI Organization Studies pilot codes; prints the memo's tables."""
import csv
from collections import Counter
from pathlib import Path

rows = list(csv.DictReader(open(Path(__file__).with_name("pilot-pci-orgstudies-2026-10-04-codes.csv"))))
stretch = [r for r in rows if r["fit"] == "stretch"]
print(f"critiques {len(rows)}, stretched {len(stretch)}, reports {len({(r['rec'], r['report']) for r in rows})}\n")
for rec in dict.fromkeys(r["rec"] for r in rows):
    sub = [r for r in rows if r["rec"] == rec]
    print(f"| {rec} | {len({r['report'] for r in sub})} | {len(sub)} | {sum(r['fit'] == 'stretch' for r in sub)} |")
print()
n, s = Counter(r["entry"] for r in rows), Counter(r["entry"] for r in stretch)
for entry, k in n.most_common():
    print(f"| {entry} | {k}{f' ({s[entry]} stretched)' if s[entry] else ''} |")
print()
for gap, k in Counter(r["gap"] for r in stretch).most_common():
    print(f"{k}  {gap}")
