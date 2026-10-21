# How we used AI assistants in building this repository

Covers sessions through 2026-10-21.

We, David Clingingsmith and Scott Shane, used AI coding and research assistants throughout this project. This page summarizes what they did and what we checked and decided. It is written from a log we keep of every working session: who worked, which tool and model, what the assistant did, and what the person checked. Those working logs stay with our private working repository because they refer to correspondence and working notes not written for publication; this summary is the public record.

The AI referee itself, two reviewer models and a grader from a third model family, is the subject of the study, not an assistant. Its models, versions, settings, prompts, and costs are recorded in each run's manifest under `sample/`.

## Tools and models

| Tool | Models | Used by | Sessions |
|:--|:--|:--|--:|
| Claude Code | Claude Opus 5, Claude Opus 5.5 | David | 5 |
| Claude Code (desktop app) | Claude Opus 5, Claude Fable 5, Claude Fable 5.1 | Scott | 4 |
| Codex | GPT-6 | David | 6 |

Fifteen sessions between September 18 and October 21, 2026.

## What the assistants did

**Setting up the repository and the way we work.** Built the repository's structure, the agent instructions both assistants follow, the folder of dated decisions (`docs/decisions/`), and the session log. Set up Scott's laptop for the work, installing Git and the GitHub command-line tool from their official releases; Scott signed in to GitHub himself, and no assistant saw or handled a password or token. API keys are kept outside the repository and are never printed or logged.

**The proposal and technical appendix.** Drafted revisions of the proposal and the appendix plan at our direction, checked the cited research and removed interpretations it did not support, computed the power arithmetic (the minimum detectable paired effect of 0.28 for 100 manuscripts), and checked the word count. Carried our edits from Word back into the markdown sources, which are the single source of truth. The appendix is assembled by code from the repository's files, so no prompt, table, or number in it is typed by hand. The proposal's prose is ours: Scott led it, and David reviewed and edited it.

**Deriving the codebook's dimensions.** Searched the scholarly literature on rigor and contribution (36 logged queries; criteria and definitions extracted from 24 works with page numbers), collected the reviewer criteria of 15 journals with public forms, and assembled a corpus of 337 published referee reports from open-review venues. Every entry traces to a retrieved page, PDF, or API response, not to model memory, and the gaps (sites that blocked automated access, forms that are not public) are recorded in `grader/`. Two pilots tested the draft dimensions on published referee reports: 472 critiques from BMJ Open reviews of qualitative studies and 82 from PCI Organization Studies. Their codes and tally scripts are in `docs/`. Scott spot-checked the corpus against the live pages, and the codebook's content was settled by us in the dated decisions.

**The coding rules.** An assistant coded a sample of 60 pilot critiques blind while David coded the same 60 by hand; the comparison showed where the rules were ambiguous. Scott ruled on the open questions and David made the follow-up calls; both are recorded as decisions. The assistant then drafted revised coding instructions with paraphrased examples, which David reviewed in Word and Scott adopted.

**The prototype.** Wrote the code in `src/referee/`: the reviewer, the mechanical checks, the grader, the numbers, the appendix, and the publishing step. Ran both AI reviewers and the grader on the sample article and recorded each run. The journal's website blocks automated readers, so Scott copied the journal's public statements in by hand. Scott confirmed the model prices against their sources, confirmed that a cited work exists, reviewed the rendered appendix, and listed seven corrections, which were made. The two items the fabrication check flagged were verified by hand as genuine.

**Preparing this public repository.** Checked the working repository's full history for material unfit to publish, which led us to publish this separate repository. Blanked the journal's manuscript ID on the sample manuscript and recorded both fingerprints. Separated the substantive content and coded results of the sample's referee reports and decision letter, which are private communications, so that they appear only in the technical appendix submitted to the journal. David clarified that report and critique counts and processing metadata may be published; the rule protects the substance of the correspondence. Built `ref publish`, which refuses to publish if it finds a key-like string, a personal path, a confidential file, or a coded journal review.

A separate Codex review checked the publication export, installed it in a clean environment, reproduced the public sample numbers from the recorded codes, and checked the prompts, fingerprints, codebook build, and mechanical checks. At David's direction it then fixed recognition of new reviews of the posted sample PDF, strengthened credential redaction, added a public-specific ignore file, and clarified the documentation of text-matching checks and historical codebook wording. Local regression tests cover those fixes without paid model calls. Historical run records were preserved and nothing was published.

David subsequently authorized publishing the checked public copy with the `stage-1-submission` label and verifying its public link.

## What we decided and checked

Every decision in `docs/decisions/` was made by one or both of us; an assistant drafted some of the files. We chose the sample article and obtained its co-authors' consent, supplied the journal's statements, made the coding rulings, coded critiques by hand to test the rules, and checked prices and sources. Scott reviewed the rendered appendix, and we both reviewed the proposal. No assistant sent a message, submitted anything, or published to this repository on its own; each of those steps was taken by one of us.

## Where the assistants went wrong

The logs also record what failed. The first grader run failed because its output limit was too small; it is kept with its own record (`sample/grader/2026-10-17T121446Z/`). One reviewer run failed for lack of API credits and was re-run. Gemini's Pro models refused or were overloaded, so the grader ran on Gemini 3.8 Flash; the grader is not yet validated against human coders.
