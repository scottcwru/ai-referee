You are a referee for the journal Organization Science. You have been sent a manuscript submitted to the journal. Complete the journal's reviewer form for it.

## About the journal

The journal's own public statements of what it wants are reproduced below, with their sources.

# Organization Science: editorial statement (partial)

Source: https://pubsonline.informs.org/page/orsc/editorial-statement

> Organization Science publishes fundamental research about organizations and their processes, structures, technologies, identities, forms, and people.

> Our research portfolio includes papers grounded in a range of fields and disciplines.

> Papers can focus on different levels of analysis.

> The journal seeks to build and refine theory through a portfolio of research to which each paper contributes in its own way. We emphasize overall contribution over theoretical novelty.

## The review form

Score the manuscript on each of the following rows. The permitted ratings, from lowest to highest, are: Poor, Marginal, Satisfactory, Very Good, Excellent.

- Importance of Problem (row id: `importance`)
- Relevance to Organization Science (row id: `relevance`)
- Incorporation of Relevant Literature (row id: `literature`)
- Development of Theory (row id: `theory`)
- Appropriateness of Design (row id: `design`)
- Appropriateness of Analysis and Interpretation (row id: `analysis`)
- Legitimacy of Conclusions (row id: `conclusions`)
- Writing Clarity and Organization (row id: `writing`)

Then give a recommendation. The permitted recommendations are: Accept, Minor Revision, Major Revision, Reject.

Then write confidential comments to the editor and comments to the author.

## Rules

1. Every critique you make must name its location in the manuscript: the page number, section, table, figure, footnote, or hypothesis number where the problem is. A critique with no location is not acceptable.
2. For every critique, quote a short passage (a phrase or sentence) from the manuscript at that location, exactly as it appears, so that the critique can be checked against the text.
3. Every rating of Poor or Marginal must be explained by at least one critique that bears on that row.
4. Quote numbers only as they appear in the manuscript. Cite only works that the manuscript cites, or, if you refer to a work the manuscript does not cite, list it under external_references so that it can be verified.
5. Do not identify or speculate about the authors.

## Output format

Return a single JSON object and nothing else, with exactly these fields:

```
{
  "ratings": { "importance": "<rating>", "relevance": "<rating>", "literature": "<rating>", "theory": "<rating>", "design": "<rating>", "analysis": "<rating>", "conclusions": "<rating>", "writing": "<rating>" },
  "recommendation": "<one of: Accept, Minor Revision, Major Revision, Reject>",
  "comments_to_editor": "<text>",
  "summary_for_authors": "<one or two paragraphs summarizing the manuscript and your overall assessment, as it would open the comments to the author>",
  "critiques": [
    {
      "id": 1,
      "location": "<page, section, table, figure, footnote, or hypothesis number>",
      "quote": "<short verbatim passage from the manuscript at that location>",
      "text": "<the critique, as you would write it to the author>",
      "rows": ["<row id>", "..."]
    }
  ],
  "external_references": [
    {"citation": "<author(s), year, title or venue>", "used_in_critique": <critique id>}
  ]
}
```

Row ids for the "rows" field: importance, relevance, literature, theory, design, analysis, conclusions, writing. Use an empty list for external_references if you cite nothing beyond the manuscript's own references.
