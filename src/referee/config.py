"""Model names, versions, settings, and prices: the only place they appear.

Prices are US dollars per one million tokens, as published by each vendor on the
date in PRICE_SOURCE. The run manifest records the model string the API reports
back, which is the version actually served.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Where the API keys are read from, in order. The first file that exists wins.
# Keys are never printed or logged. See AGENTS.md, hard rule 2.
KEY_FILES = [
    ROOT / "sample-private" / "keys.env",
    Path.home() / ".config" / "referee" / "keys.env",
]

REVIEWERS = {
    "claude": {
        "vendor": "anthropic",
        "model": "claude-opus-5-5",
        "settings": {
            "max_tokens": 32000,
            "effort": "high",
            "thinking": "adaptive (the model's default; not configurable on this model)",
            "temperature": "not set (not accepted with adaptive thinking)",
        },
        "price_per_million": {
            "input": 4.00,
            "output": 20.00,
            "cache_write": 5.00,
            "cache_read": 0.20,
        },
    },
    "chatgpt": {
        "vendor": "openai",
        "model": "gpt-5.5-2026-04-23",
        "settings": {
            "max_output_tokens": 32000,
            "reasoning_effort": "high",
            "temperature": "not set (not accepted by reasoning models)",
            "store": False,
        },
        "price_per_million": {
            "input": 5.00,
            "output": 30.00,
            "cache_read": 0.50,
        },
    },
}

# The grader: a model family neither reviewer uses (decision of 2026-09-17).
GRADER = {
    "vendor": "google",
    "model": "gemini-3.8-flash",
    "settings": {
        "temperature": "model default (Google advises against lowering it on Gemini 3 models)",
        "response_mime_type": "application/json",
        "thinking_level": "low",
        "max_output_tokens": 65536,
    },
    "price_per_million": {
        "input": 0.75,
        "output": 3.75,
        "cache_read": 0.0,
    },
    "price_note": "Paid-tier rates from Google's own pricing page, ai.google.dev/gemini-api/docs/pricing, confirmed by Scott Shane on 2026-10-17. No cached content is used, so the cache-read rate is not applied. Output price covers thinking tokens.",
    "model_note": "Chosen on 2026-10-17. Google's API refuses gemini-2.5-pro to new accounts, and gemini-3.1-pro-preview and gemini-pro-latest returned 'high demand' (HTTP 503) on every attempt that day. gemini-3.8-flash is the newest Gemini model with a stable, non-preview id that the key could call. The manifest records the model version the API reports for every call.",
}

PRICE_SOURCE = {
    "anthropic": "Anthropic model table, retrieved 2026-10-17",
    "openai": "GPT-5.5 at $5.00 input and $30.00 output per million tokens, consistent across independent pricing trackers and confirmed by Scott Shane on 2026-10-17; OpenAI's own pricing page refused automated access",
    "note": "GPT-5.5 is the newest OpenAI model that offers a dated snapshot id. gpt-6-astra (September 2026) is served only under an undated alias and so cannot be pinned.",
}

# Folders with this name, and the sample grader runs' coded critiques from these arms, are never published
# (`ref publish`; decision of 2026-10-21). The study's coded dataset is governed by the data agreement instead.
CONFIDENTIAL = "confidential"
JOURNAL_ARMS = {"human", "editor"}

PATHS = {
    "prompt": ROOT / "reviewer" / "prompt.md",
    "form": ROOT / "reviewer" / "form" / "template.json",
    "journal_sources": ROOT / "reviewer" / "journal-sources",
    "runs": ROOT / "sample" / "runs",
    "codebook": ROOT / "grader" / "codebook_v9.md",
    "coding_instructions": ROOT / "grader" / "coding-instructions.md",
    "grader_prompt": ROOT / "grader" / "prompt.md",
    "grader_prompt_segment": ROOT / "grader" / "prompt-segment.md",
    "grader_runs": ROOT / "sample" / "grader",
    "manuscript": ROOT / "sample" / "manuscript" / "manuscript.pdf",
    "manuscript_fingerprints": ROOT / "sample" / "manuscript" / "fingerprints.json",
    "numbers": ROOT / "sample" / "prototype-numbers.md",
    # Material drawn from the sample's referee reports and decision letter, which are private
    # communications between Organization Science, the authors, and the referees. It goes in
    # the technical appendix submitted with the proposal and is never published.
    "sample_article": ROOT / "sample" / CONFIDENTIAL / "sample-article.json",
    "numbers_full": ROOT / "sample" / CONFIDENTIAL / "prototype-numbers.md",
    "sample_numbers": ROOT / "sample" / CONFIDENTIAL / "sample-numbers.json",
}

# The public repository the proposal and appendix link to, and the label of the
# version submitted at Stage 1. `ref publish` writes to it; nothing else names it.
PUBLIC_REPOSITORY = {
    "name": "scottcwru/ai-referee",
    "url": "https://github.com/scottcwru/ai-referee",
    "tag": "stage-1-submission",
}
