"""Split a review into individual critiques, and find each critique's context.

The split is done by the grader model with grader/prompt-segment.md. The
context (one sentence before and after) is found in the review text by code.
"""

import re
import unicodedata
from pathlib import Path

from . import config


def load_segment_prompt(report: str) -> str:
    text = config.PATHS["grader_prompt_segment"].read_text(encoding="utf-8")
    return text.replace("{{report}}", report)


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip()


_SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(\[*\-\d])")


def sentences(text: str) -> list[str]:
    return [s for s in _SENT.split(_norm(text)) if s.strip()]


def context_for(review: str, critique_text: str) -> dict:
    """One sentence before and after the critique in the review, if the critique is found verbatim."""
    nrev = _norm(review)
    ncrit = _norm(critique_text)
    i = nrev.find(ncrit)
    if i < 0:
        # try the first and last 60 characters, for a critique the model trimmed at a boundary
        head, tail = ncrit[:60], ncrit[-60:]
        i = nrev.find(head)
        j = nrev.find(tail, i) if i >= 0 else -1
        if i < 0 or j < 0:
            return {"before": "", "after": "", "verbatim_match": False}
        end = j + len(tail)
    else:
        end = i + len(ncrit)
    before_text = nrev[:i].strip()
    after_text = nrev[end:].strip()
    before = sentences(before_text)[-1] if before_text else ""
    after = sentences(after_text)[0] if after_text else ""
    return {"before": before, "after": after, "verbatim_match": True}
