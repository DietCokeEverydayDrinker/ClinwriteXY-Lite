# Case 6

## Reconcile the three artefacts

Authoritative snapshot: 120 enrolled; 118 analysed; 24 events in the analysis
set; adjusted HR 1.42 (95% CI 1.05 to 1.92); 3 participants with missing
exposure; no sensitivity analysis run.

| Item | Snapshot | Abstract | Results table | Discussion |
|---|---|---|---|---|
| Participants | 120 enrolled; 118 analysed | 120 (set not stated) | 118 | not stated |
| Events | 24 | 25 | 24 | not stated |
| Adjusted HR (95% CI) | 1.42 (1.05 to 1.92) | 1.45 (1.08 to 1.95) | 1.42 (1.05 to 1.92) | not stated |
| Sensitivity analysis | none run | not stated | not stated | "remains significant in the sensitivity analysis" |

Blocking inconsistencies:

1. Event count: abstract reports 25 events; the analysis set and table report
   24. The abstract number is not supported by the supplied analysis set.
2. Effect estimate: abstract reports HR 1.45 (95% CI 1.08 to 1.95); the table
   reports HR 1.42 (95% CI 1.05 to 1.92). Two different estimates exist for the
   same primary analysis, and no source explains which is current.
3. Denominator arithmetic: 120 enrolled minus 3 with missing exposure gives 117,
   not the stated 118 analysed. The path from enrolled to analysed cannot be
   reproduced from the supplied numbers.
4. Sensitivity claim: the Discussion states the result "remains significant in
   the sensitivity analysis," but no sensitivity analysis exists in the supplied
   record. This claim is unsupported and unverifiable.

The abstract's "120 participants" also needs an explicit set label: if it means
enrolled, it must also state the analysed n; if it means analysed, it conflicts
with the 118 in the table.

## Point-by-point reviewer reply

Comment C1

Reviewer comment: "Please add an E-value sensitivity analysis and report the
result."

Decision: needs_analysis.

Response:

We agree that an E-value sensitivity analysis would strengthen the
interpretation of the adjusted HR. This analysis has not yet been performed in
the current project record, so we cannot yet report an E-value or its threshold.
We will first reconcile the enrolled and analysed sample sizes, the event count,
and the final HR and CI across the abstract, table, and discussion. We will then
compute the E-value and report the result and threshold in the Results and
Discussion, with the corresponding revised manuscript location.

Action taken: none for the analysis itself; the request is recorded as pending a
verified result.

Evidence: supplied snapshot (120 enrolled, 118 analysed, 24 events, HR 1.42,
95% CI 1.05 to 1.92; no sensitivity analysis).

## Next actions before resubmission

1. Reconcile the denominator path: confirm 120 enrolled to 118 analysed and
   explain the 3 missing-exposure participants against the 120 minus 118 gap.
2. Freeze one event count and one HR with CI, then propagate them to the
   abstract, results table, and discussion.
3. Remove or reclassify the Discussion's sensitivity claim until an E-value is
   computed and verified.
4. Perform the E-value sensitivity analysis and report the E-value and threshold
   with the same denominator and uncertainty discipline.
5. Re-run the consistency check from claim to table to analysis version before
   resubmission.

Files reviewed: supplied project snapshot, abstract, results table, discussion.
Files missing: any sensitivity-analysis output or script supporting the
Discussion claim.

# Case 7

## Blocking issues

1. Sample size contradiction: Methods states 88 participants; Results states 86
   with complete data; Discussion states 90 participants were included. There is
   no single reproducible analysis set.
2. Unsupported survival claim: Discussion describes "an overall survival
   benefit," but Results states no survival analysis was performed. The claim is
   unsupported and outside the chapter's question.
3. Conclusion overreach: "biomarker X should guide clinical treatment" is a
   treatment-guidance claim not supported by a single-centre association study
   of a 12-month functional score.
4. Table cross-reference: the text cites Table 3.4, but the supplied chapter
   contains Table 3.3.
5. Missing figure: a figure is discussed but no figure file or legend is
   supplied.

## Question and section interfaces

Question: whether baseline biomarker X is associated with 12-month functional
score. Design: prospective single-centre cohort; primary analysis of
association. This supports an association claim only.

Results can hand to the Discussion an association estimate in 86 participants
with complete data. Results cannot hand over a survival benefit or a treatment
recommendation, because no survival analysis was performed and clinical utility
was not evaluated.

## Repair plan

1. Freeze the chapter version and determine the correct sample size among 88,
   86, and 90; document exclusions; propagate one number through Methods,
   Results, tables, and Discussion.
2. Remove the survival-benefit sentence or replace it with what was actually
   measured. If a survival analysis was intended but not run, record it as a
   missing analysis, not a result.
3. Reword the conclusion to the association boundary: biomarker X was
   associated with 12-month functional score; treatment guidance requires
   external validation and decision-impact evidence.
4. Correct the Table 3.4 reference to Table 3.3 and align every table and
   figure callout.
5. Supply the missing figure and legend, or remove the figure discussion. Do
   not invent the figure or its analysis.
6. Re-run the chapter-interface audit after the fixes.

# Case 8

## Defensible review paragraph

In adults, the intervention is supported by evidence of different designs and
endpoints. In a randomised trial of 324 adults comparing intervention with
control, the primary endpoint improved in 12.4% of participants versus 8.9%,
with similar adverse-event rates; the supplied summary does not report a
confidence interval for this difference. In a 48-animal rat experiment, the
intervention reduced the fibrosis score versus control, but no clinical outcomes
were measured, so this result supports only a model-level or mechanistic effect.
In an observational cohort of 2,000 adults, higher exposure was associated with
the outcome, but residual confounding was possible, so this result reflects
association rather than causation. The randomised trial reports a higher
proportion with primary-endpoint improvement in the intervention arm; the animal
experiment offers a mechanistic direction; and the observational study offers an
association that requires cautious interpretation. These sources do not
establish clinical benefit from the animal evidence or a causal effect from the
observational evidence.

## Evidence table

| Source | Design | Population or model | n | Comparison | Result | Boundary |
|---|---|---|---|---|---|---|
| Study 1 | Randomised trial | Adults | 324 | Intervention vs control | Primary endpoint 12.4% vs 8.9%; adverse events similar | Clinical efficacy; CI not reported |
| Study 2 | Animal experiment | Rats | 48 | Intervention vs control | Reduced fibrosis score; no clinical outcomes | Model or mechanism only |
| Study 3 | Observational cohort | Adults | 2,000 | Higher vs lower exposure | Higher exposure associated with outcome | Association; residual confounding |

## What cannot be done from the supplied materials

The five additional online references cannot be found or added. No live database
search was run, and no citations should be fabricated. A real 10-slide PPTX
cannot be built here; this mode returns a slide outline, not a file. Clinical
benefit cannot be inferred from the animal experiment, and a causal claim cannot
be inferred from the observational cohort.

## Handoff for the literature search

Hand this minimum request to an installed external search workflow such as
nature-academic-search:

- review_question: effect of the intervention on the relevant clinical outcome
  in adults
- population_or_material: adults
- exposure_or_intervention: the intervention
- comparator: control or standard care
- outcomes: primary endpoint, adverse events, patient-important outcomes
- study_designs: randomised trials first, then observational studies with
  explicit confounding control
- databases, search_date, search_strings, deduplication_method, eligibility
  criteria: to be executed and recorded by the search workflow
- deliverable: five verified references with identifiers, accessed text or
  abstract, locators, and a per-sentence support judgment before insertion

## Handoff for the presentation

A 10-slide outline for a group meeting, without an actual PPTX and without
invented figures:

1. Clinical problem and gap.
2. Study question.
3. Design and populations across the three sources.
4. Randomised trial result (12.4% vs 8.9%; adverse events similar).
5. Animal experiment result (fibrosis score; no clinical outcome).
6. Observational result and residual confounding.
7. Evidence-level comparison: trial, animal, observational.
8. What the evidence supports and what it does not.
9. Limitations.
10. Bounded conclusion and next step.

Each slide should answer one question, and the speaker note should carry the
interpretation. A real PPTX requires a presentation-generation tool such as
ppt-master after the five references are verified.
