You are a coder for a study of referee reports. You will be shown one critique from a referee report of a manuscript submitted to the journal Organization Science, with one sentence of context on either side. Code the critique by the codebook and the coding instructions below. You do not see the manuscript or the rest of the report, and you are not told who wrote the report.

## Coding instructions

{{instructions}}

## Codebook

{{codebook}}

## Form rows

The journal's review form has these rows. Name the one row the critique bears on most directly, or "none" if it bears on none.

{{form_rows}}

## What to return

Return a single JSON object and nothing else:

```
{
  "dimension": "<a code from the codebook, e.g. MET.DES.SAMP, or NEW>",
  "proposed_label": "<only if dimension is NEW: a short label for the missing entry; otherwise empty>",
  "category": "<rigor | contribution | other>",
  "checkability": "<checkable error | omission | judgment>",
  "form_row": "<one of: {{row_ids}} | none>",
  "location": "<the manuscript location the critique names, or none>",
  "note": "<one line, only if the category departs from the entry's usual category or the coding was difficult; otherwise empty>"
}
```

## The critique

Context before: {{before}}

CRITIQUE: {{critique}}

Context after: {{after}}
