You are a coder for a study of referee reports. You will be shown one critique from a referee report of a manuscript submitted to the journal Organization Science, with one sentence of context on either side. Code the critique by the codebook and the coding instructions below. You do not see the manuscript or the rest of the report, and you are not told who wrote the report.

## Coding instructions

# Coding instructions: rigor, contribution, and other

Draft for Scott, revising the falsity test after the October 5 coding session

October 7, 2026

**Status:** draft for Scott’s review. Goes into the repository (grader/coding-instructions.md) once approved. **Implements:** the decisions of October 6 (docs/decisions/2026-10-06-*.md): rigor defined by subject, the four rulings, the new entries, and the split of the literature entry. **Companion files:** codebook_v9.md (the entries, each with its usual category) and rules-agreement-test.md (the proposed test before preregistration). **Questions for Scott** are collected in the last section. Everything else follows from the October 6 decisions or is marked *proposed*.

## What a coder records

A **critique** is one sentence or group of consecutive sentences in a report that asserts one defect in the manuscript. For each critique the coder records three things:

1. **Dimension:** the most specific entry in the codebook that fits (codebook_v9.md).
2. **Category:** rigor, contribution, or other.
3. **Checkability:** checkable error, omission, or judgment.

Category and checkability are separate judgments. The codebook gives each entry a *usual* category as a guide, but the coder decides the category for the critique in front of them; a critique coded to an entry against its usual category gets a one-line note.

## Category

**Rigor:** the critique says a claim in the manuscript is not adequately supported by its evidence, design, analysis, or reasoning, or that something the manuscript reports is wrong.

**Contribution:** the critique says the work does not add enough to the field: the question is not important, the answer is not new, the theory is not developed, the paper is not positioned against what is known, or the work would be more valuable with something added.

**Other:** the critique is about how the manuscript is written or presented and asserts no defect in its claims or its value. “Other” is the Writing family of the codebook (Mechanics and clarity; Figures, tables, or examples; Title, abstract, and keywords; Tone or terminology), with two exceptions that are rigor: reported numbers or facts that differ between passages (CON.INCON), and a title or abstract that states something the study did not do or does not show (CON.SHOWN). Other is reported but excluded from the rigor share.

**The rigor share** of a review is rigor critiques divided by rigor plus contribution critiques.

**The test to apply.** Ask what the critique is *about*, not whether it could be checked. “There may be an unobserved confounder” is rigor, although no one can settle it from the manuscript. “This result is already published” is contribution, although it can be checked against the earlier paper.

## The four rulings, with balanced examples

Each ruling is shown with critiques on both sides of its line. Examples are paraphrases of critiques in the October 4 pilots (docs/pilot-bmjopen-qual-2026-10-04-codes.csv); the identifier after each is the paper, report, and item. None comes from the 60 critiques of the October 5 session, and all are excluded from the sample for the agreement test. Examples marked *constructed* illustrate a case the pilots did not supply.

### Ruling 1. An omission of procedure is rigor

The line: an omission is rigor when the missing item is something a reader needs to judge whether the claims are supported (a procedure, data, materials, a result). It is contribution when the missing item is what the work means or adds, and other when the item is present but hard to read.

| Critique | Category | Why |
|:--|:--|:--|
| Interview questions are not provided (PMC11138289 R2, 2) | Rigor | Procedure needed to judge the findings |
| How the themes were constructed is not described (PMC11138289 R2, 3) | Rigor | Analytic procedure |
| How participants were identified and invited is unclear (PMC11535687 R1, 5) | Rigor | Sampling procedure |
| Recommendations for practice and future research are not explored (PMC10989111 R1, 24) | Contribution | What the work means, not how it was done |
| The contribution relative to existing literature is not explained (PMC10826535 R2, 6) | Contribution | Positioning |
| Table titles and abbreviations are unclear (PMC10806645 R1, 7) | Other | Present but hard to read |

### Ruling 2. A judgment that a design or analysis is inadequate is rigor

The line: the critique judges whether the study as designed and analyzed can support the claims it makes (rigor), or says a different or further study would add more (contribution). A judgment counts as rigor even when no one can settle it from the manuscript.

| Critique | Category | Why |
|:--|:--|:--|
| Only a single interview per caregiver (PMC11293397 R3, 1) | Rigor | Whether the design supports the findings |
| A claim of saturation at the fifteenth participant is questionable (PMC11293397 R2, 14) | Rigor | Sufficiency of the sample |
| The gap in men’s help-seeking may reflect gender rather than migration (PMC11647344 R1, 16) | Rigor | Rival explanation |
| Explore differences by interviewee role (PMC10936458 R2, 1) | Contribution | A further analysis that would add, not a flaw in the claims made |
| The experience of group care is already widely studied (PMC11308902 R2, 2) | Contribution | Novelty |

### Ruling 3. A citation that misreads its source is rigor

The line: the critique is about whether the paper uses a source accurately (rigor, LIT.SRC), or about whether it uses the right or enough sources (contribution, LIT.POS).

| Critique | Category | Why |
|:--|:--|:--|
| Literature on the exploitation of migrants is reported imprecisely (PMC11647344 R1, 13) | Rigor | A source is misrepresented |
| *Constructed:* the cited meta-analysis found no effect, not the positive effect the paper reports | Rigor | A source is misrepresented |
| Consult the literature on masculinities and migration (PMC11647344 R1, 20) | Contribution | Missing literature |
| Compare with studies from other African countries (PMC11293397 R3, 4) | Contribution | Positioning |

Ruled: a claim that needs a supporting citation is rigor, CON.SHOWN (“the claim that hegemonic masculinity is idealized needs a citation,” PMC11647344 R1, 23). Ruling 1.

### Ruling 4. Writing and clarity are other

The line: the critique is about the prose or presentation (other), or about whether something reported is true (rigor). A complaint about wording that is really a complaint about substance is coded by the substance (codebook boundary rules 2 and 8).

| Critique | Category | Why |
|:--|:--|:--|
| Grammar and spelling errors throughout (PMC11590845 R2, 1) | Other | Prose |
| Use “emergency department,” not “emergency room” (PMC11492942 R2, 9) | Other | Terminology |
| The abstract is repetitive; rewrite (PMC10773376 R1, 3) | Other | Presentation |
| A count is inconsistent between the text and the figure (PMC11492942 R2, 7) | Rigor | A reported number is wrong in one place (CON.INCON) |
| Population density is likely per km², not per m² (PMC11590845 R1, 1) | Rigor | A reported value is wrong on its face (CON.INCON) |
| “Purposive sampling” is applied to hospitals, not participants (PMC11590845 R2, 3) | Rigor | Misused technical term, coded to sample selection |

## Checkability

Checkability is recorded for every critique, in all three categories, at one of three levels.

**Checkable error.** The asserted defect can be settled by comparing the manuscript with its own evidence, a source it cites, a specific source the critique names, or an applicable rule (statistical, logical, or a named reporting standard). *Examples:* a count that differs between text and figure; a quotation that does not support the claim it is offered for (PMC11138289 R2, 7); a cited source misreported; a typo.

**Omission.** The critique says something is not reported or not done, and names what. Whether the item is there can be checked; whether it is needed may be a judgment. *Examples:* interview questions not provided; how themes were built not described; no member checking.

**Judgment.** Settling the defect requires weighing, not checking. *Examples:* one interview per caregiver is too few; a rival explanation may account for the result; the question is not important; the result is already widely studied (no source named).

Checkability is reported as an attribute of each rigor critique; the secondary outcome is defined in the proposal. Omissions are reported separately, so the result can be read under either a narrow or a broad view of checkability.

## Cases ruled by the subject definition

These follow directly from defining rigor by subject; listed so coders apply them the same way.

| Case | Category | Checkability |
|:--|:--|:--|
| A result already appears in earlier work | Contribution | Checkable error if the critique names the work; otherwise judgment |
| A counterexample from outside the manuscript (an institution the typology does not fit) | Rigor | Checkable error if specific and sourced; otherwise judgment |
| Extension suggested (a worthwhile further analysis) | Contribution | Usually judgment |
| An error in unit or level of analysis | Rigor | Usually judgment |

## Questions that were open, with the rulings that settled them

The rulings below settle each question; the lettered options are kept so that the ruling can be read against them.

Rulings (Scott Shane, October 9, 2026): 1. (a) Rigor, CON.SHOWN. 2. (a) Rigor, LIT.SRC. 3. (a) Rigor, MET.DES; no new entry. 4. (a) Rigor. 5. Falsifiability is rigor; Purpose of the research is contribution; Flaws remediable in revision is other. 6. The proposed definition stands: a specific source the critique names counts. 7. Category is coded per critique, as proposed.

1. **A claim that needs a supporting citation** (codebook v8, boundary rule 4, codes it LIT).
    - (a) Rigor: an unsupported claim (CON.SHOWN or LIT.SRC).
    - (b) Contribution: failing to credit prior work (LIT.POS), as rule 4 now reads.
2. **Fidelity to a source theorist** (a borrowed theory applied in a way its author would not recognize).
    - (a) Rigor: a source is misrepresented (LIT.SRC).
    - (b) Contribution: a matter of interpretation and positioning.
3. **A design critique of a paper with no data** (“the method is essentially an essay”; “no research question or methodology is stated”).
    - (a) Rigor (Appropriateness of Design). (b) Contribution. (c) A new entry for papers with no stated method or genre, which has two sightings and is pending under the counting rule.
4. **Concept clarity (THE.CONCEPT):** (a) rigor, as a defect of reasoning; (b) contribution, as a defect of theory development.
5. **Usual category of three existing entries:** Falsifiability (no testable predictions), Purpose of the research (aim unclear), and Flaws remediable in revision. Each could be rigor, contribution, or other.
6. **Sources for a checkable error.** The definition above counts a specific source the critique names (proposed), which makes “already published in Smith (2019)” checkable. The alternative counts only the manuscript, its cited sources, and rules.
7. **Category coded per critique (proposed) or derived from the entry.** Coding it per critique lets a coder depart from an entry’s usual category with a note; deriving it from the entry is simpler but carries every dimension disagreement (kappa 0.39 on October 5) into the rigor share.

## Codebook

# Codebook, version 9 (draft for Scott, 2026-10-07)

**Draft.** Built by build_codebook_v9.py from grader/codebook_v8.md, adding the entries decided on 2026-10-06 and a usual-category column (R rigor, C contribution, O other, ? question for Scott). The category is coded for each critique separately; the column is a guide, not a rule. Every change from v8 is marked “Added,” “Split,” “Moved,” or “proposed” in its row.

**About the usual-category column.** The column is new in v9 and is a proposal by David and Claude, not a result. Each entry’s definition was read against the definition of rigor decided on 2026-10-06 (docs/decisions/2026-10-06-rigor-defined-by-subject.md) and assigned R, C, or O by hand; entries the definition does not settle are marked ?. No coded data stands behind the values, and no earlier document assigns categories to these entries (the rigor and contribution labels in step1_scholarly_literature.md, step2_journal_forms.md, and step5_skeleton.md sort source criteria, not entries, mostly under the falsity test that the October 6 decision replaced; the six rigor dimensions named in the proposal were replaced by the derived list). The column needs Scott’s confirmation as a whole, not only for the entries marked ?.

The dimension list from step9_dimensions_v8.md, with a one-sentence definition for each place a critique can be coded, and the boundary rules Scott set (step7_meta_dimensions.md, step8_combined_dimensions.md). A critique is one sentence or group of consecutive sentences in a report that asserts one defect in the manuscript. Code each critique to the most specific entry that fits. An entry marked *(parent)* takes a critique only when none of its sub-dimensions fits.

## Methods *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| MET.DES | Appropriateness of Design *(parent)* | The design or the data cannot answer the research question, for a reason not listed below. | R |
| MET.DES.SAMP | Sample selection | How the sample (participants, cases, countries, studies, sources, journals) was chosen is unexplained, unjustified, or biased, or the sampling logic is misunderstood. When a study’s data are published literature, the literature search and the choice of journals are sample selection. | R |
| MET.ANA | Appropriateness of Analysis and Interpretation | The statistical analysis is wrong: the wrong analysis for the data or question, a model comparison that does not support the chosen model, inadequate power or sample size, a statistic misdescribed or misapplied (including a statistical term used for the wrong kind of test), an analytic choice or assumption not justified (transformations, thresholds, pooling), or the practical size of the effect not assessed. | R |
| MET.MEAS | Validity and reliability of measures *(parent)* | The study measures the phenomenon incorrectly, for a reason not listed below. | R |
| MET.MEAS.CON | Construct validity *(parent)* | The research operations do not represent the constructs they are claimed to represent (Shadish, Cook & Campbell: “inferences about the constructs that research operations represent”). | R |
| MET.MEAS.CON.MEAS | Construct validity of measures | A measure does not capture the construct it is named for, a claimed mechanism is never measured, or coding criteria are not shown to capture the concept. | R |
| MET.MEAS.CON.MANIP | Construct validity of manipulations | A manipulation, treatment, or proxy condition does not produce or represent the state it is meant to induce. Added after batch 02. | R |
| MET.MEAS.REL | Reliability | Reliability is unreported or low, including interrater reliability. | R |
| MET.MEAS.STATE | Participant state: order, practice, fatigue, or inattention | Participants’ order, practice, fatigue, or inattention distorts what is measured, including their behavior. | R |
| MET.MEAS.REACT | Reactive arrangements | Demand characteristics or social desirability distort participants’ responses. | R |
| MET.INT | Internal validity *(parent)* | A different explanation of the result cannot be ruled out, for a reason not listed below. | R |
| MET.INT.ALT | Alternative explanation or confound | A specific rival explanation, confound, or unobserved difference between units is not ruled out. | R |
| MET.INT.CAUSAL | Causal claim rests on a measured, not manipulated, variable | A causal claim is made from a variable that was measured rather than manipulated. | R |
| MET.PLAN | Analysis plan or model not specified | Model structure, parameters, a non-standard test, confirmatory versus exploratory analyses, or missing-data handling is not specified. | R |
| MET.ROB | Robustness | The result is not shown to survive other reasonable analytic choices (sensitivity analysis, researcher degrees of freedom, an artifact of a classification choice). | R |
| MET.DISC | Full disclosure *(parent)* | The paper does not report enough to see how the study was done or what it found, for a reason not listed below. | R |
| MET.DISC.PROC | Process or findings not described | A procedure, material, data source, or result is not reported in enough detail; data, code, or materials are unavailable or unusable; a referenced supplement or table is missing. | R |
| MET.DISC.PREREG | Preregistration | The study was not preregistered where it should have been, or its registration status or deviations from the registered plan are not transparent. | R |
| MET.DISC.ETH | Research ethics | Ethics approval or consent is not reported, or the research was not conducted ethically. | R |
| MET.QUAL | Qualitative methods *(parent)* | The qualitative procedure falls short of the standards for its method, for a reason not listed below. Added 2026-10-06. | R |
| MET.QUAL.DATA | Data structure (theme construction and interpretation) | Themes are not soundly built from the data: two themes are indistinguishable, a theme bundles unrelated content, or the path from codes to themes does not hold. Label: Gioia, Corley, and Hamilton (2013). | R |
| MET.QUAL.COH | Meaningful coherence (choice and fidelity of method) | The qualitative method is not justified for the question, or the study does not follow the method it claims (for example, it claims grounded theory or phenomenology but does not apply it). Label: Tracy (2010). | R |
| MET.QUAL.CRED | Credibility (trustworthiness strategies) | Steps that establish the trustworthiness of the analysis (member checking, triangulation, an audit trail, peer debriefing) were not taken or are inadequate. Label: Guba (1981); Tracy (2010). | R |
| MET.QUAL.SAT | Theoretical saturation | The sample is not shown to be sufficient, or a claim of saturation is not supported. Label: Eisenhardt (1989). | R |
| MET.QUAL.TRANS | Translation and transcription fidelity | Translation or transcription may not have preserved participants’ meaning, or how it did is not shown. Authors’ label. | R |
| MET.QUAL.REFLEX | Self-reflexivity | The researchers’ position and its influence on data collection and interpretation are not examined. Label: Tracy (2010). | R |

## Development of Theory *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| THE.GROUND | Theoretical grounding weak or narrow | The theory behind the hypotheses or mechanism is thin, narrow, weak, or never introduced. | C |
| THE.CONTRIB | Contribution to theory | The work does not test, create, or extend theory (a statement of importance about theory). | C |
| THE.UTIL | Utility of theory | The theory explains or predicts too little. | C |
| THE.COH | Consistency/Coherence of Conceptual Argument *(parent)* | The theoretical argument is not clear and logical. | R |
| THE.COH.ECO | Ecological validity | Realism: the theory or model rests on an assumption that is unrealistic for the agents or setting it describes, or the study’s setting or task lacks the real-world features the claims are about. Label from Scott; added after batch 04, widened to study settings after batch 05. | R |
| THE.COH.CONTRA | Internal contradictions | The theory says one thing (X causes Y) and another part of the paper says something incompatible (Y causes X, or X and Y are only correlated). | R |
| THE.LINK | Linkage between Conceptual Argument and Empirical Analysis | The hypotheses or the test do not follow from the argument, or an inductively built theory is not grounded in the data. | R |
| THE.FALS | Falsifiability | The paper states no research questions, hypotheses, or testable predictions. | R |
| THE.CONCEPT | Concept clarity | A theoretical concept is undefined, defined too narrowly or broadly, overlaps another concept, or is used in more than one sense. Authors’ label. Added 2026-10-06. | R |
| THE.UNIT | Unit or level of analysis | The argument or analysis treats its object at the wrong unit or level (for example, perspectives in the literature treated as kinds of real-world arrangement, or individual-level evidence used for claims about organizations). Authors’ label. Added 2026-10-06. | R |

## Research Questions and Goals *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| RQ.IMP | Importance of Problem | The paper does not argue why its question matters or how widely it applies. | C |
| RQ.FRAME | Framing of the argument | The way the paper sets up what it asks and why is wrong or unconvincing (distinct from positioning in the literature, which is Incorporation of Relevant Literature). Label from the proposal’s original list; added 2026-09-25. | C |
| RQ.PURP | Purpose of the research | What the study sets out to do (its aim, the gap it fills, its hypotheses, or its key concepts) is unclear. | C |

## Legitimacy of Conclusions *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| CON.SHOWN | Claim or conclusion not shown | A claim or conclusion is not shown by the evidence: never tested, tested without showing it, a difference claimed without a direct test, a result misread against its confidence interval, a generalization beyond the sample, or a conclusion about something never measured. | R |
| CON.ANOM | Anomalous or conflicting result not addressed | Part of the evidence cuts against the authors’ account and is left unexplained. | R |
| CON.UNDEV | Finding left undeveloped | The authors do not interpret what their own results show: an unexpected finding, a promised theme, or the plain reading of the results. | R |
| CON.NEUT | Neutrality | Results are presented selectively or as stronger or more settled than they are, or the findings reflect the investigator’s biases or interests. | R |
| CON.REPL | Replicability | The finding may not replicate. | R |
| CON.INCON | Reported results inconsistent | Numbers or facts differ between passages, tables, or figures, or a reported value is wrong on its face (for example, an impossible unit). Moved from Mechanics and clarity; proposed 2026-10-07. | R |

## Overall contribution *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| CONTRIB | Overall contribution *(parent)* | The paper adds too little to knowledge, for a reason not listed below. | C |
| CONTRIB.EXT | Extension suggested | A worthwhile further analysis or addition that would increase what the paper contributes. | C |
| CONTRIB.LEN | Contribution relative to length | The paper is too long, repetitive, or badly organized for what it contributes; material should be cut, merged, reordered, or moved to a supplement. | O |

## Writing Clarity and Organization *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| WRI.MECH | Mechanics and clarity | Typos, grammar, spelling, formatting, style, malapropisms, unclear prose, material that is present but explained unclearly. (Numbers that differ between passages move to CON.INCON.) | O |
| WRI.FIG | Figures, tables, or examples | Results should be shown more clearly through figures, tables, or examples. | O |
| WRI.TITLE | Title, abstract, and keywords | The title, abstract, or keywords do not convey or index the study well. A title or abstract that states something the study did not do or does not show is CON.SHOWN. Keywords added after batch 03. | O |
| WRI.TONE | Tone or terminology | Word choice or tone is inappropriate (not the misuse of a technical term). | O |

## Other dimensions

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| LIT | Incorporation of Relevant Literature *(parent)* | Prior literature is missing or mistreated, a citation is missing or inaccurate (failing to find and credit the work the paper builds on), or the findings are not compared with prior work. | — |
| LIT.SRC | Literature: a source is misrepresented | A cited source does not say what the paper says it says, or prior findings are reported inaccurately. Split from LIT 2026-10-06. | R |
| LIT.POS | Literature: positioning and coverage | Relevant prior work is missing, the paper is not positioned against it, or the findings are not compared with it. Split from LIT 2026-10-06. | C |
| SIL.PRAC | Implications for practice or policy | What the findings mean for practice, policy, or future research is not spelled out. | C |
| SIL.THEORY | Implications for theory | What the findings change in theory is not spelled out. | C |
| SIL.LIM | Limitations | Strengths and limitations are not stated clearly and frankly. | R |
| SIL.EXT | External validity | Whether the finding holds beyond the persons, settings, treatments, and outcomes studied is not addressed. | R |
| ORIG | Originality *(parent)* | The paper has not shown that it adds something new beyond what is known (novelty, originality, interestingness). | C |
| ORIG.BREADTH | Breadth of appeal | The work will interest too narrow an audience. | C |
| FIT | Relevance to Organization Science | The paper does not fit the journal it is submitted to. | C |
| FLAW | Flaws remediable in revision | The flaws cannot be remedied in a revision. | O |

## Dropped at the end of collection

Theories introduced inconsistently across sections (2 sightings, reports only) was still pending when collection stopped and is dropped as idiosyncratic under the stopping rule; its critiques are coded to THE.COH.

## Boundary rules

1. Code by the type of error the referee asserts, not by the part of the paper it concerns.
2. Misusing a technical term (for example, a statistical term for the wrong kind of test) is coded to that kind of error, not to Writing.
3. Something missing is MET.DISC.PROC; something present but explained unclearly is WRI.MECH.
4. “Claim lacks supporting citation” is CON.SHOWN: an unsupported claim (rigor). Ruled 2026-10-09.
5. If the evidence does not show the claim, code CON.SHOWN; if it shows the claim and a rival equally, code MET.INT.
6. A vague critique that says something is missing without naming it is coded by what the missing thing refers to, using its context in the report, and marked as inferred.
7. Do not force a critique into an entry that does not fit it. If nothing fits, code it NEW with a proposed label.
8. Code the substantive failure the referee asserts, read in context, not the rhetorical form of the complaint. “The limitations paragraph contradicts the argument for the sampling choice” is a failure of generalizability (SIL.EXT), not a contradiction (added after batch 04).
9. A qualitative step that is *not reported* is MET.DISC.PROC; a step that was *not taken or was done badly* goes to the MET.QUAL entry for it. Added 2026-10-07.


## Form rows

The journal's review form has these rows. Name the one row the critique bears on most directly, or "none" if it bears on none.

- Importance of Problem (row id: `importance`)
- Relevance to Organization Science (row id: `relevance`)
- Incorporation of Relevant Literature (row id: `literature`)
- Development of Theory (row id: `theory`)
- Appropriateness of Design (row id: `design`)
- Appropriateness of Analysis and Interpretation (row id: `analysis`)
- Legitimacy of Conclusions (row id: `conclusions`)
- Writing Clarity and Organization (row id: `writing`)

## What to return

Return a single JSON object and nothing else:

```
{
  "dimension": "<a code from the codebook, e.g. MET.DES.SAMP, or NEW>",
  "proposed_label": "<only if dimension is NEW: a short label for the missing entry; otherwise empty>",
  "category": "<rigor | contribution | other>",
  "checkability": "<checkable error | omission | judgment>",
  "form_row": "<one of: importance, relevance, literature, theory, design, analysis, conclusions, writing | none>",
  "location": "<the manuscript location the critique names, or none>",
  "note": "<one line, only if the category departs from the entry's usual category or the coding was difficult; otherwise empty>"
}
```

## The critique

Context before: {{before}}

CRITIQUE: {{critique}}

Context after: {{after}}
