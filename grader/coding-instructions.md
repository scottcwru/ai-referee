# Coding instructions: rigor, contribution, and other

**Implements:** the decisions of October 6 (the six files in docs/decisions dated 2026-10-06): rigor defined by subject, the four rulings, the new entries, and the split of the literature entry, with Scott's rulings of October 9 on the questions they left open (last section). **Companion files:** codebook_v9.md (the entries, each with its usual category) and docs/rules-agreement-test.md (the agreement test, which runs after selection by the decision of 2026-10-09).

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

## Questions for Scott

Each needs a ruling before the agreement test. Options are listed without a recommendation.

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
