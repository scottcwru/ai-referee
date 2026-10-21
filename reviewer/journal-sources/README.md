# The journal's public statements

The reviewer prompt quotes the journal's own public statements of what it wants (decision of 2026-09-17; Scott's v4 plan, Stage 1). Each statement is one markdown file in this folder with its source URL and retrieval date at the top. `src/referee/form.py` assembles every `.md` file here except this README into the prompt, in filename order, after removing HTML comments (which hold provenance notes).

| File | Statement | Status |
|:--|:--|:--|
| `author-guidelines.md` | Submission guidelines | Complete. Copied by Scott Shane on 2026-10-17 from https://www.informs.org/Pubs/OrgSci/Submission-Guidelines; navigation, contact details, and form lists removed |
| `editorial-statement.md` | Editorial statement, which is the journal's statement of aims and scope | Complete. Copied by Scott Shane on 2026-10-17 from https://www.informs.org/Pubs/OrgSci/Editorial-Statement |
| (reviewer guidelines) | — | None found. INFORMS publishes no reviewer guidelines for this journal that a search located on 2026-10-17; its ethics page covers reviewer conduct |

The journal's pages at pubsonline.informs.org serve a bot check to automated readers, so these texts were copied by hand. The run manifest records the SHA-256 of the assembled prompt, so runs made before and after this folder was completed can be told apart: the run of 2026-10-17T102639Z used a partial editorial statement and no submission guidelines.
