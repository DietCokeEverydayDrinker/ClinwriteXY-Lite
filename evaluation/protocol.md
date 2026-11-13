# Controlled comparison protocol

## Arms

1. Raw: the model receives only the case and task prompt.
2. Lite: the model first reads `SKILL.md` and the references selected by that
   skill.
3. Full: the model first reads the full ClinwriteXY `SKILL.md` and the
   references selected by that skill.

All arms use the same model, the same five cases, and the same output
instructions. No arm may use live search, other writing skills, or external
reference material during generation.

## Required output

Return all five cases in one response, using the headings `Case 1` through
`Case 5`. Put the finished text under `Output`. For Cases 4 and 5, also include
the compact change record requested in the case prompt.

## Blind scoring

The evaluator receives anonymised outputs labelled A, B, and C. Score each arm
from 1 to 5 on:

- evidence and claim calibration;
- preservation of numbers, denominators, and validation labels;
- clinical prose quality in the requested language;
- concision and freedom from template-like phrasing;
- usefulness as a standalone writing tool.

Record any factual error, invented detail, unsupported causal or clinical claim,
or missed bilingual mismatch.
