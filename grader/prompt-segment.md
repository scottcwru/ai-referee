You are preparing a referee report for coding. Your task is to split the report into critiques. You do not judge or code the critiques here.

## Definition

A critique is one sentence or group of consecutive sentences in a report that asserts one defect in the manuscript. Praise, summary of the manuscript, pleasantries, and procedural remarks are not critiques. A sentence that asserts two separate defects is two critiques; a defect that is asserted and then elaborated over several consecutive sentences is one critique. A suggestion that implies a defect ("the authors should report X") is a critique.

## Rules

1. Copy each critique's text verbatim from the report. Do not paraphrase, shorten, or correct it. If a critique spans several sentences, copy them all.
2. Keep the report's order.
3. If the critique names where in the manuscript the defect is (page, section, table, figure, footnote, hypothesis), copy that location into the location field; otherwise write "none".
4. Do not skip a critique because it is minor or repeats an earlier one. Repeats are listed again.

## Output format

Return a single JSON object and nothing else:

```
{
  "critiques": [
    {"id": 1, "text": "<verbatim text>", "location": "<location as named, or none>"}
  ]
}
```

## The report

{{report}}
