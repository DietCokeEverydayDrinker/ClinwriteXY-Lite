# ClinwriteXY model comparison

Date: 2026-11-13

This run compares DeepSeek V4 Pro and V4 Flash under three isolated conditions:

1. Raw: no ClinwriteXY files may be read.
2. Lite: read only `clinwritexy-lite/SKILL.md` and references selected by it.
3. Full: read only `clinwritexy/SKILL.md` and references selected by it.

All arms receive the same five cases from
`clinwritexy-lite/evaluation/test-cases.md`, the same output requirements, and
medium reasoning effort. No arm may use live search, another writing skill, or
external material.

The generation instructions are deliberately identical across arms. The only
intended difference is the assigned skill scope.

## Scoring

Each case is scored from 1 to 5 on:

- evidence and claim calibration;
- preservation of numbers, denominators, endpoints, and validation labels;
- clinical prose quality in the requested language;
- concision and freedom from template-like phrasing;
- standalone usefulness.

The report must also list every material factual error, invented detail,
unsupported causal or clinical claim, and missed bilingual mismatch.
