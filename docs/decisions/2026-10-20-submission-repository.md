# The submission is a separate public repository, published from the working one

**Decided:** 2026-10-20 (David proposed; Scott approved each item).

- We submit a separate public repository, `scottcwru/ai-referee`, with no history from the working repository. The working repository stays private.
- It holds the code, the reviewer, the grader with its derivation record, the sample, the paper sources (*the proposal and the generated appendix are withheld since 2026-10-21; see `2026-10-21-journal-correspondence-private.md`*), `analysis/`, the settled decisions, the rules-agreement test, and the AI-use logs. The logs are edited to remove references to private correspondence and personal paths before they are published. *(Superseded on 2026-10-21: the logs are not published; a public summary, `docs/ai-use.md`, takes their place. See `2026-10-21-ai-use-summary.md`.)*
- On 2026-10-21 David added the October 4 BMJ Open pilot's codes, sample list, and collection and tally scripts, because the coding instructions cite the codes file; the pilot's write-up is not published.
- Changes flow one way. All edits happen in the working repository, and the public repository changes only when we publish with `ref publish`, which refuses on the checks listed in `src/referee/publish.py`. We publish only when both of us agree; David runs it, never as part of a sync.
- The last publish before submission, by October 28, is labeled `stage-1-submission`. The proposal and appendix link to that label, read from `config.PUBLIC_REPOSITORY`.
- The sample manuscript is posted with the journal's manuscript ID blanked on its cover page. Both fingerprints, the file the reviewers read and the file posted, are recorded in `sample/manuscript/fingerprints.json`; the reviews are not re-run.

**Why:** the working repository's history contains material that cannot be published, and removing it would mean rewriting shared history; it also holds working notes not written for editors.
