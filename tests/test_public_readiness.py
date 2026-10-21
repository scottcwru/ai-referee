"""Local publication regressions; no API keys or paid model calls required.

Run with: uv run python -m unittest discover -s tests
"""

import contextlib
import io
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from referee import config
from referee.grade import Grader
from referee.numbers import is_sample_run, manuscript_fingerprints, write_numbers
from referee.publish import _strip_journal_reviews
from referee.review import run, safe_error


ROOT = Path(__file__).resolve().parents[1]
REVIEW_RUN = "2026-10-17T110416Z"
GRADER_RUN = "2026-10-17T122945Z"


class SampleNumbersTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.reviewer = self.root / "sample/runs" / REVIEW_RUN
        self.grader = self.root / "sample/grader" / GRADER_RUN
        self.reviewer.mkdir(parents=True)
        self.grader.mkdir(parents=True)
        for name in ("manifest.json", "review-claude.json", "review-chatgpt.json"):
            shutil.copyfile(ROOT / "sample/runs" / REVIEW_RUN / name, self.reviewer / name)
        for name in ("manifest.json", "coded-critiques.csv"):
            shutil.copyfile(ROOT / "sample/grader" / GRADER_RUN / name, self.grader / name)
        _strip_journal_reviews(self.root)
        for name in ("manuscript.pdf", "fingerprints.json"):
            shutil.copyfile(ROOT / "sample/manuscript" / name, self.root / name)
        self.output = self.root / "numbers.md"
        paths = {
            "runs": self.root / "sample/runs",
            "manuscript": self.root / "manuscript.pdf",
            "manuscript_fingerprints": self.root / "fingerprints.json",
            "sample_article": self.root / "absent-editorial-facts.json",
            "numbers": self.output,
        }
        patcher = patch.dict(config.PATHS, paths)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.rm = json.loads((self.reviewer / "manifest.json").read_text())
        self.fp = json.loads((self.root / "fingerprints.json").read_text())

    def set_reviewed_hash(self, value):
        self.rm["manuscript"]["sha256"] = value
        (self.reviewer / "manifest.json").write_text(json.dumps(self.rm))

    def write_numbers(self):
        with contextlib.redirect_stdout(io.StringIO()):
            write_numbers(self.grader)
        return self.output.read_text()

    def test_saved_public_numbers_reproduce_exactly(self):
        self.assertTrue(is_sample_run(self.grader))
        self.assertEqual(self.write_numbers(), (ROOT / "sample/prototype-numbers.md").read_text())

    def test_new_review_of_posted_pdf_generates_numbers(self):
        self.set_reviewed_hash(self.fp["posted_sha256"])
        gm = json.loads((self.grader / "manifest.json").read_text())
        gm.pop("journal_reviews_withheld", None)
        gm["totals"].update(cost_usd=0.10, elapsed_seconds=30, models_served=["fixture-grader"])
        (self.grader / "manifest.json").write_text(json.dumps(gm))
        self.assertTrue(is_sample_run(self.grader))
        text = self.write_numbers()
        self.assertIn("This run reviewed the posted copy.", text)
        self.assertIn("Grading the AI reviews cost $0.10", text)
        self.assertNotIn("a total that includes coding", text)

    def test_unrelated_manuscript_is_rejected(self):
        self.set_reviewed_hash("0" * 64)
        self.assertFalse(is_sample_run(self.grader))
        with self.assertRaises(ValueError):
            self.write_numbers()
        self.assertFalse(self.output.exists())

    def test_tampered_posted_pdf_is_rejected_for_both_versions(self):
        with (self.root / "manuscript.pdf").open("ab") as f:
            f.write(b"fixture alteration")
        for fingerprint in ("reviewed_sha256", "posted_sha256"):
            with self.subTest(version=fingerprint):
                self.set_reviewed_hash(self.fp[fingerprint])
                with self.assertRaises(ValueError):
                    manuscript_fingerprints(self.rm)


class CredentialRedactionTests(unittest.TestCase):
    def test_known_formats_are_redacted_without_loaded_values(self):
        synthetic = [
            "sk-" + "O" * 32,
            "sk-ant-" + "A" * 32,
            "AIza" + "G" * 35,
        ]
        result = safe_error(RuntimeError("credentials: " + " ".join(synthetic)))
        for value in synthetic:
            self.assertNotIn(value, result)
        self.assertIn("[redacted]", result)

    def test_exact_values_are_redacted_before_truncation(self):
        synthetic = "fixture credential with no vendor prefix"
        result = safe_error(ValueError("x" * 380 + synthetic), [synthetic])
        self.assertNotIn("fixture credential", result)
        self.assertIn("[redacted]", result)

    def test_reviewer_failure_record_redacts_loaded_value(self):
        synthetic = "fixture-reviewer-credential"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manuscript = root / "fixture.pdf"
            manuscript.write_bytes(b"fixture, not a PDF")
            caller = Mock(side_effect=RuntimeError("invalid credential: " + synthetic))
            with patch("referee.review.load_keys", return_value=({"ANTHROPIC_API_KEY": synthetic}, root / "keys.env")), \
                 patch("referee.review.pdf_pages", return_value=1), \
                 patch.dict("referee.review.CALLERS", {"anthropic": caller}):
                out = run(manuscript, root / "run", reviewers=["claude"])
            manifest = (out / "manifest.json").read_text()
            self.assertNotIn(synthetic, manifest)
            self.assertIn("[redacted]", manifest)
            self.assertEqual(json.loads(manifest)["reviewers"]["claude"]["status"], "failed")

    def test_grader_failure_record_redacts_loaded_value(self):
        synthetic = "fixture-grader-credential"
        grader = Grader.__new__(Grader)
        grader.client = SimpleNamespace(models=SimpleNamespace(
            generate_content=Mock(side_effect=RuntimeError("invalid credential: " + synthetic))))
        grader._secrets = (synthetic,)
        grader.spec = config.GRADER
        grader.calls = []
        grader.raw_dir = None
        with self.assertRaises(RuntimeError):
            grader.ask("fixture prompt", "fixture call")
        record = json.dumps(grader.calls)
        self.assertNotIn(synthetic, record)
        self.assertIn("[redacted]", record)


class PublicIgnoreTests(unittest.TestCase):
    def test_credentials_and_private_outputs_are_ignored_but_sample_is_publishable(self):
        source = ROOT / "publish/gitignore"
        if not source.exists():
            source = ROOT / ".gitignore"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copyfile(source, root / ".gitignore")
            subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)
            paths = {
                "keys.env": True,
                ".env.local": True,
                "sample-private/report.txt": True,
                "sample/confidential/results.json": True,
                "local/manuscript.pdf": True,
                "paper/appendix.docx": True,
                ".venv/pyvenv.cfg": True,
                "sample/manuscript/manuscript.pdf": False,
                "sample/runs/recorded/manifest.json": False,
                "src/referee/review.py": False,
            }
            for path, ignored in paths.items():
                with self.subTest(path=path):
                    result = subprocess.run(["git", "check-ignore", "--no-index", "-q", path],
                                            cwd=root, capture_output=True)
                    self.assertIn(result.returncode, (0, 1))
                    self.assertEqual(result.returncode == 0, ignored)


if __name__ == "__main__":
    unittest.main()
