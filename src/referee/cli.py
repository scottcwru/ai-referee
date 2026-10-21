"""One entry point: `ref <command>` (or `python -m referee.cli <command>`).

    ref review <manuscript.pdf> [--reviewers claude,chatgpt] [--run-dir DIR] [--keys FILE]
    ref check <run-dir> <manuscript.pdf>
    ref prompt            print the assembled reviewer prompt
    ref publish [--to CLONE] [--label] [--push]
"""

import argparse
import json
import sys
from pathlib import Path


def main(argv=None):
    p = argparse.ArgumentParser(prog="ref")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("review", help="run both reviewers on a manuscript and record the run")
    r.add_argument("manuscript", type=Path)
    r.add_argument("--reviewers", default=None, help="comma-separated subset, e.g. claude")
    r.add_argument("--run-dir", type=Path, default=None)
    r.add_argument("--keys", type=Path, default=None, help="keys.env file (default: see config.KEY_FILES)")
    r.add_argument("--no-check", action="store_true", help="skip the mechanical checks after the run")

    c = sub.add_parser("check", help="run the four mechanical checks on a recorded run")
    c.add_argument("run_dir", type=Path)
    c.add_argument("manuscript", type=Path)

    sub.add_parser("prompt", help="print the assembled reviewer prompt")

    g = sub.add_parser("grade", help="code every critique in a reviewer run's AI reviews and in the human reports")
    g.add_argument("reviewer_run", type=Path)
    g.add_argument("--human-dir", type=Path, default=None, help="private folder holding reviewer1.txt, reviewer2.txt, reviewer3.txt, decision-letter.txt")
    g.add_argument("--out", type=Path, default=None)
    g.add_argument("--keys", type=Path, default=None)
    g.add_argument("--no-numbers", action="store_true", help="skip writing sample/prototype-numbers.md")

    nn = sub.add_parser("numbers", help="write sample/prototype-numbers.md from a grader run")
    nn.add_argument("grader_run", type=Path)

    ap = sub.add_parser("appendix", help="assemble paper/appendix.md from the repository and render paper/appendix.docx")
    ap.add_argument("--reviewer-run", type=Path, default=None)
    ap.add_argument("--grader-run", type=Path, default=None)

    pb = sub.add_parser("publish", help="check the publish set and, with --to, commit it in a clone of the public repository")
    pb.add_argument("--to", type=Path, default=None, help="local clone of the public repository; without it, only the checks run")
    pb.add_argument("--label", action="store_true", help="label this publish as the Stage 1 submission (config.PUBLIC_REPOSITORY)")
    pb.add_argument("--push", action="store_true", help="push the commit (and label) to GitHub")

    a = p.parse_args(argv)

    if a.cmd == "publish":
        from .publish import PublishRefused, publish

        try:
            rep = publish(a.to, a.label, a.push)
        except PublishRefused as e:
            print(f"refused: {e}")
            return 1
        print(f"working version {rep['working_version'][:12]}; {rep['files']} files")
        for w in rep["warnings"]:
            print(f"  warning: {w}")
        for r in rep["refusals"]:
            print(f"  REFUSED: {r}")
        if rep["refusals"]:
            print("nothing published")
            return 1
        if a.to is None:
            print("checks passed; nothing written (use --to to commit in a clone of the public repository)")
        else:
            print(("committed" if rep["committed"] else "no changes to commit") + f" in {a.to}"
                  + (f"; labeled {rep['labeled']}" if rep.get("labeled") else "")
                  + ("; pushed" if rep.get("pushed") else "; not pushed"))
        return 0

    if a.cmd == "appendix":
        from .appendix import build
        from .numbers import restricted_inputs_present

        if not restricted_inputs_present():
            print("The technical appendix reports the sample's referee reports and decision letter, which are restricted "
                  "inputs; it was submitted with the proposal and cannot be assembled from the public repository. "
                  "See 'Reproducing the sample results' in README.md.")
            return 1
        md, docx = build(a.reviewer_run, a.grader_run)
        print(f"wrote {md} and {docx}")
        return 0

    if a.cmd == "grade":
        from .grade import grade
        from .numbers import write_numbers

        out = grade(a.reviewer_run, a.human_dir, a.out, a.keys)
        m = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        t = m["totals"]
        print(f"grader run recorded in {out}")
        print(f"  {t['calls']} calls ({t['failed_calls']} failed); ${t['cost_usd']:.2f}; {t['elapsed_seconds']}s; served by {', '.join(t['models_served'])}")
        for f in m["failures"]:
            print(f"  FAILED {f['review']} {f['step']}: {f['error'][:160]}")
        if not a.no_numbers:
            from .numbers import is_sample_run

            if is_sample_run(out):
                print(f"  numbers written to {write_numbers(out)}")
            else:
                print("  numbers not written: they describe the sample article, and this run is of another manuscript")
        return 0

    if a.cmd == "numbers":
        from .numbers import write_numbers

        print(write_numbers(a.grader_run))
        return 0

    if a.cmd == "prompt":
        from .form import assemble_prompt, load_form

        print(assemble_prompt(load_form()))
        return 0

    if a.cmd == "review":
        from .checks import check_run
        from .review import run

        reviewers = a.reviewers.split(",") if a.reviewers else None
        run_dir = run(a.manuscript, a.run_dir, reviewers, a.keys)
        manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
        print(f"run recorded in {run_dir}")
        for name, rec in manifest["reviewers"].items():
            line = f"  {name}: {rec['status']}"
            if "cost_usd" in rec:
                line += f"; ${rec['cost_usd']:.2f}; {rec['elapsed_seconds']}s; served by {rec.get('model_served')}"
            else:
                err = rec["attempts"][-1].get("error") if rec["attempts"] else ""
                line += f"; {err}"
            print(line)
        if not a.no_check:
            summary = check_run(run_dir, a.manuscript)
            for name, res in summary.items():
                print(f"  checks for {name}: " + ", ".join(f"{c['name']}={'pass' if c['pass'] else 'FAIL'}" for c in res["checks"]))
        return 0

    if a.cmd == "check":
        from .checks import check_run

        summary = check_run(a.run_dir, a.manuscript)
        for name, res in summary.items():
            print(f"{name}: " + ", ".join(f"{c['name']}={'pass' if c['pass'] else 'FAIL'}" for c in res["checks"]))
        return 0


if __name__ == "__main__":
    sys.exit(main())
