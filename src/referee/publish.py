"""Publish the approved folders of this working repository to the public repository.

Changes flow one way: everything is edited here, and the public repository changes
only when we publish. A publish copies the committed version of the folders in
PUBLISH (never uncommitted work), puts publish/README.md in place as the public
README, and refuses if the copy contains a key-like string, a personal path, the
journal manuscript ID, a term on the do-not-publish list (people's names, private
folders, this working repository's name), a Word or PDF file other than
the sample manuscript, or if a file the appendix cites is missing. A published file
that names a working document left out of the publish set gets a warning. It commits the
copy in a local clone of the public repository with the working version in the
message, and labels it if asked. It pushes only when asked.

The do-not-publish list lives outside the repository (DO_NOT_PUBLISH), one term
per line, matched without regard to case, because the terms on it must never be
published themselves.

The sample's referee reports and decision letter are private communications between
Organization Science, the authors, and the referees (publication scope clarified on 2026-10-21).
Their substantive content is withheld; report and critique counts and processing metadata may
be published. Folders named config.CONFIDENTIAL and the files in WITHHELD are left out, and
the grader runs' coded critiques and manifests are published without the rows and entries for
the journal's reviews (config.JOURNAL_ARMS). They go in the technical appendix instead.
"""

import csv
import io
import json
import re
import shutil
import subprocess
import tarfile
import tempfile
from io import BytesIO
from pathlib import Path

from . import config

# What the public repository holds: the approved folders and files, as committed here.
PUBLISH = [
    "src/referee",
    "pyproject.toml",
    "tests",
    "LICENSE",
    "reviewer",
    "grader",
    "sample",
    "paper",
    "analysis",
    "docs/decisions",
    "docs/rules-agreement-test.md",
    # the public summary of AI assistance; the session logs stay in the working repository
    "docs/ai-use.md",
    # the October 4 BMJ Open pilot's data, which the coding instructions cite; its write-up stays out
    "docs/pilot-bmjopen-qual-2026-10-04-codes.csv",
    "docs/pilot-bmjopen-qual-2026-10-04-sample.csv",
    "docs/pilot-bmjopen-qual-2026-10-04-collect.py",
    "docs/pilot-bmjopen-qual-2026-10-04-tally.py",
    # the PCI Organization Studies pilot's codes, which the rules-agreement test cites
    "docs/pilot-pci-orgstudies-2026-10-04-codes.csv",
    "docs/pilot-pci-orgstudies-2026-10-04-tally.py",
]
# Published path: source path in this repository.
REPLACE = {"README.md": "publish/README.md", ".gitignore": "publish/gitignore"}
# The submitted documents: the generated appendix carries the journal's reviews, and the proposal is
# submitted rather than published (decision of 2026-10-21).
WITHHELD = {"paper/appendix.md", "paper/proposal.md"}
# Grader-run files published without the journal's reviews (see _strip_journal_reviews).
GRADER_RUN_FILES = ("coded-critiques.csv", "manifest.json")
# The only Word or PDF file that may be published.
BINARY_ALLOWED = {"sample/manuscript/manuscript.pdf"}
BINARY_SUFFIXES = {".docx", ".doc", ".pdf", ".xlsx", ".xls", ".pptx", ".ppt"}

DO_NOT_PUBLISH = Path.home() / ".config" / "referee" / "do-not-publish.txt"

REFUSE = {
    "key-like string": [
        r"sk-ant-[A-Za-z0-9_-]{20,}", r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}", r"AIza[0-9A-Za-z_-]{35}",
        r"\bgh[pousr]_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{20,}", r"\bAKIA[0-9A-Z]{16}\b",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"\bxox[abprs]-[A-Za-z0-9-]{10,}",
    ],
    "personal path": [r"\b[A-Za-z]:\\{1,2}Users\\{1,2}", r"/Users/[A-Za-z]", r"/home/[a-z]"],
    "journal manuscript ID": [r"ORSC-MS-\d{4}-\d+"],
}
# Names of private folders, of this working repository, and of people go in DO_NOT_PUBLISH,
# not here, so that publishing this file does not publish them.


class PublishRefused(Exception):
    pass


def _git(*args, cwd=config.ROOT) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def export(dest: Path) -> str:
    """Write the committed version of the publish set into dest; return the working version."""
    sources = PUBLISH + list(REPLACE.values())
    dirty = _git("status", "--porcelain", "--", *sources)
    if dirty:
        raise PublishRefused("uncommitted changes in the publish set; sync first:\n" + dirty)
    commit = _git("rev-parse", "HEAD")
    excluded = [f":(exclude,glob)**/{config.CONFIDENTIAL}/**"] + [f":(exclude){w}" for w in WITHHELD]
    tar = subprocess.run(["git", "archive", "--format=tar", commit, "--", *PUBLISH, *excluded], cwd=config.ROOT,
                         check=True, capture_output=True).stdout
    with tarfile.open(fileobj=BytesIO(tar)) as t:
        t.extractall(dest, filter="data")
    for published, source in REPLACE.items():
        data = subprocess.run(["git", "show", f"{commit}:{source}"], cwd=config.ROOT, check=True, capture_output=True).stdout
        (dest / published).write_bytes(data)
    _strip_journal_reviews(dest)
    return commit


def _journal_review(entry: dict) -> bool:
    return entry.get("arm") in config.JOURNAL_ARMS


def _strip_journal_reviews(tree: Path) -> None:
    """Remove substantive journal-review records; retain permitted processing totals."""
    for run in sorted((tree / "sample" / "grader").glob("*/")):
        coded = run / "coded-critiques.csv"
        names = set()
        if coded.exists():
            with coded.open(encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                fields = reader.fieldnames
            names = {r["review"] for r in rows if _journal_review(r)}
            out = io.StringIO()
            w = csv.DictWriter(out, fieldnames=list(fields), lineterminator="\n")
            w.writeheader()
            w.writerows(r for r in rows if not _journal_review(r))
            coded.write_text(out.getvalue(), encoding="utf-8", newline="")
        manifest = run / "manifest.json"
        if manifest.exists():
            m = json.loads(manifest.read_text(encoding="utf-8"))
            names |= {e["review"] for e in m.get("reviews_coded", []) if _journal_review(e)}
            m["reviews_coded"] = [e for e in m.get("reviews_coded", []) if not _journal_review(e)]
            m["calls"] = [c for c in m.get("calls", []) if not set(c.get("label", "").split(":")) & names]
            m["failures"] = [f for f in m.get("failures", []) if f.get("review") not in names]
            m["journal_reviews_withheld"] = ("The referee reports and decision letter were also coded in this run; their entries are "
                                             "withheld from the public repository and reported in the technical appendix. Totals include them.")
            manifest.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")


def _text(p: Path) -> str | None:
    if p.suffix.lower() == ".pdf":
        import logging

        from pypdf import PdfReader

        logging.getLogger("pypdf").setLevel(logging.ERROR)

        return "\n".join(page.extract_text() or "" for page in PdfReader(p).pages)
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def _term(t: str) -> re.Pattern:
    left = r"\b" if re.match(r"\w", t) else ""
    right = r"\b" if re.search(r"\w$", t) else ""
    return re.compile(left + re.escape(t) + right, re.I)


def unpublished() -> list[str]:
    """Working documents left out of the publish set: tracked files outside it, and their top folders."""
    out = set()
    for f in _git("ls-files").splitlines():
        if _withheld(f):
            out.add(f)
            continue
        if f in REPLACE or any(f == p or f.startswith(p + "/") for p in PUBLISH + list(REPLACE.values())):
            continue
        out.add(f)
        if "/" in f and f.split("/")[0] not in {p.split("/")[0] for p in PUBLISH}:
            out.add(f.split("/")[0] + "/")
    return sorted(out)


def _withheld(rel: str) -> bool:
    return rel in WITHHELD or config.CONFIDENTIAL in rel.split("/")


def _ai_use_stale() -> str | None:
    """The public AI-use summary must cover every session in the working logs."""
    summary = (config.ROOT / "docs" / "ai-use.md").read_text(encoding="utf-8")
    m = re.search(r"Covers sessions through (\d{4}-\d{2}-\d{2})", summary)
    if not m:
        return "docs/ai-use.md does not say which sessions it covers"
    logs = sorted(p.name[:10] for p in (config.ROOT / "docs" / "ai-log").glob("20*.md"))
    if logs and logs[-1] > m.group(1):
        return f"docs/ai-use.md covers sessions through {m.group(1)}, but there is a session log from {logs[-1]}; update the summary"
    return None


def check(tree: Path, names: list[str], left_out: list[str] = (), appendix: str | None = None) -> tuple[list[str], list[str]]:
    """Return (refusals, warnings) for an exported tree.

    appendix is the text of the working appendix, whose citations must resolve in the copy.
    """
    refusals, warnings = [], []
    patterns = {k: [re.compile(x) for x in v] for k, v in REFUSE.items()}
    if names:
        patterns["do-not-publish term"] = [_term(n) for n in names]
    left_out = [d for d in left_out if not d.startswith(".")]
    files = sorted(p for p in tree.rglob("*") if p.is_file())
    for p in files:
        rel = p.relative_to(tree).as_posix()
        if _withheld(rel):
            refusals.append(f"{rel}: withheld (the journal's reviews)")
        if p.name in GRADER_RUN_FILES and rel.startswith("sample/grader/"):
            if p.suffix == ".csv":
                with p.open(encoding="utf-8", newline="") as f:
                    journal = any(_journal_review(r) for r in csv.DictReader(f))
            else:
                journal = any(_journal_review(e) for e in json.loads(p.read_text(encoding="utf-8")).get("reviews_coded", []))
            if journal:
                refusals.append(f"{rel}: holds entries for the journal's reviews")
        if p.suffix.lower() in BINARY_SUFFIXES and rel not in BINARY_ALLOWED:
            refusals.append(f"{rel}: Word or PDF file other than the sample manuscript")
        text = _text(p)
        if text is None:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            for kind, regs in patterns.items():
                if any(r.search(line) for r in regs):
                    # the line itself is not shown: it may hold a key or a name
                    refusals.append(f"{rel}:{n}: {kind}")
            for d in left_out:
                if d in line:
                    warnings.append(f"{rel}:{n}: names {d}, which is not published")
                    break
    stale = _ai_use_stale()
    if stale:
        refusals.append(stale)
    if appendix is None:
        appendix = (config.ROOT / "paper" / "appendix.md").read_text(encoding="utf-8")
    tops = {"reviewer", "grader", "sample", "src", "paper", "docs", "analysis"}
    for cited in sorted(set(re.findall(r"`([\w.-]+/[\w./-]*)`", appendix))):
        if cited.split("/")[0] in tops and not _withheld(cited.rstrip("/")) and not (tree / cited.rstrip("/")).exists():
            refusals.append(f"paper/appendix.md cites {cited}, which is not in the published copy")
    return refusals, warnings


def _names() -> list[str]:
    if not DO_NOT_PUBLISH.exists():
        raise PublishRefused(f"the do-not-publish list is missing ({DO_NOT_PUBLISH}); create it, one term per line")
    return [ln.strip() for ln in DO_NOT_PUBLISH.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")]


def publish(target: Path | None, label: bool = False, push: bool = False) -> dict:
    """Export, check, and (with a target) commit the copy in a clone of the public repository.

    Without a target, only the export and the checks run.
    """
    names = _names()
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp) / "copy"
        tree.mkdir()
        commit = export(tree)
        appendix = _git("show", f"{commit}:paper/appendix.md")
        refusals, warnings = check(tree, names, unpublished(), appendix)
        report = {"working_version": commit, "files": sum(1 for p in tree.rglob("*") if p.is_file()),
                  "refusals": refusals, "warnings": warnings}
        if refusals or target is None:
            return report
        target = Path(target)
        if not (target / ".git").exists():
            raise PublishRefused(f"{target} is not a clone of {config.PUBLIC_REPOSITORY['url']}")
        origin = _git("remote", "get-url", "origin", cwd=target)
        if origin.removesuffix(".git").rstrip("/") != config.PUBLIC_REPOSITORY["url"]:
            raise PublishRefused(f"{target} points at {origin}, not {config.PUBLIC_REPOSITORY['url']}")
        if _git("status", "--porcelain", cwd=target):
            raise PublishRefused(f"{target} has changes of its own; the public repository changes only by publishing")
        tag = config.PUBLIC_REPOSITORY["tag"]
        if label and tag in _git("tag", "--list", tag, cwd=target).split():
            raise PublishRefused(f"the label {tag} already exists in {target}; decide together before moving it")
        for p in target.iterdir():
            if p.name != ".git":
                shutil.rmtree(p) if p.is_dir() else p.unlink()
        shutil.copytree(tree, target, dirs_exist_ok=True)
        # the target is a clone that only this command writes to, so staging everything is safe here
        _git("add", "--all", cwd=target)
        if _git("status", "--porcelain", cwd=target):
            _git("commit", "-m", f"publish from working version {commit[:12]}", cwd=target)
            report["committed"] = True
        else:
            report["committed"] = False
        if label:
            _git("tag", "-a", tag, "-m", f"Stage 1 submission; working version {commit[:12]}", cwd=target)
            report["labeled"] = tag
        if push:
            _git("push", "origin", "HEAD", cwd=target)
            if label:
                _git("push", "origin", tag, cwd=target)
            report["pushed"] = True
        return report
