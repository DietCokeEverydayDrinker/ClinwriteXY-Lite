# First-round comparison summary

This is a small, one-run developer check, not a formal benchmark. It used
`deepseek-v4-pro` through Codex, the same public-fact prompts, and a blind
evaluator.

## Single-paragraph cases

| Arm | Blind score (out of 25) | Observed result |
|---|---:|---|
| Raw model | 23.0 | Strong prose, but omitted the 1,702-patient Swiss cohort and 851-patient UK cohort sizes in Case 1. |
| Lite | 24.5 | Preserved all supplied counts and validation labels; delivered compact Chinese and English prose. |
| Full | 24.5 | Also preserved the supplied counts and validation labels; no material single-paragraph advantage over Lite in this run. |

The blind evaluator found no decisive difference between Lite and Full when both
were limited to one paragraph. Lite's useful distinction sat in its narrow,
repeatable claim-and-preservation workflow. The full version's stronger
difference appeared when the task crossed manuscript sections and administrative
artefacts.

## Multi-document workflow case

| Arm | Scope behaviour |
|---|---|
| Raw model | Produced a complete package, with a useful claim table, revised text, reviewer replies, and change map. Cross-document traceability was less systematic. |
| Lite | Correctly declined the whole-manuscript and reviewer-response package, then contributed focused paragraph-level claim checks and revisions. |
| Full | Produced an itemised claim-evidence matrix, revised abstract and discussion, point-by-point response, change map, and next project decisions. |

## Product interpretation

- Lite is viable as a standalone free skill for a Chinese or English clinical
  paragraph.
- Raw DeepSeek-V4-Pro is already strong on ordinary paragraphs. Lite should be
  judged by consistent preservation and claim discipline, not by promising that
  every sentence will sound better.
- Full ClinwriteXY provides a wider workflow. Use Lite for a paragraph; use Full
  for whole-manuscript coordination, reviewer responses, and project records.

These results should be repeated with more models, more prompts, and independent
users before making broad comparative claims.
