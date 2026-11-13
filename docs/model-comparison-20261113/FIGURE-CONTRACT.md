# Figure contract

## Core conclusion

ClinwriteXY Lite and Full close most of the blind-score gap between V4 Flash
and V4 Pro in short clinical-writing cases, while preserving critical cohort
sizes that the raw Flash model and all tested Pro conditions missed. Full adds
workflow coverage in advanced tasks, with a measurable output-length cost.

## Figure 1

Archetype: quantitative grid.

- Panel A: mean blind score across five basic writing cases.
- Panel B: case-level blind score for the six test conditions.
- Panel C: mean blind score across three advanced integration cases.
- Panel D: output-character volume for basic and advanced cases.

## Figure 2

Archetype: case-level score profile and failure-mode figure.

- Panel A: evidence and claim calibration across Cases 1-5.
- Panel B: number, denominator, endpoint, and validation-label preservation
  across Cases 1-5.
- Panel C: concision and template control across Cases 1-5.

## Export contract

- Backend: Python and matplotlib only.
- Output: 600 dpi PNG, editable-text SVG, and PDF.
- Source data: `data/scores.csv` and `data/case_scores.csv`.
- Figure labels use English to avoid font availability issues; captions are
  written in Chinese in the report.
- No patient data, private drafts, institutional files, or participant
  identifiers are present.

