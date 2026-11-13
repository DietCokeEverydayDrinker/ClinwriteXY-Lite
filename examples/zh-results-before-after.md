# Chinese Results Paragraph: Synthetic Example

## Input

> 本研究共纳入126例患者，干预组62例，对照组64例。干预组主要终点发生率为19.4%，
> 对照组为31.3%。模型分析显示干预与主要终点风险降低相关（HR 0.68，95% CI
> 0.49-0.94）。因此，该干预可有效预防主要终点，应作为所有患者的常规方案。

## Problem diagnosis

- The outcome name and follow-up window are absent.
- The percentage lacks an explicit event count.
- The design is not stated.
- `风险降低相关` is upgraded to `有效预防` and a universal recommendation.
- The HR and confidence interval must remain unchanged.

## Candidate revision

> 本研究纳入接受[研究场景与纳入条件]的126例患者，其中干预组62例、对照组64例。
> 在[随访时间]内，干预组有[事件数]例发生主要终点（19.4%），对照组有[事件数]例
> 发生主要终点（31.3%）。模型分析显示，干预与主要终点风险降低相关（HR 0.68，
> 95% CI 0.49-0.94）。该结果来自[研究设计]，尚不足以证明干预能够预防主要终点，
> 也不能据此形成面向所有患者的常规推荐。

## Preservation record

- Numbers preserved: 126, 62, 64, 19.4%, 31.3%, 0.68, 95%, 0.49, 0.94.
- Missing denominator labels remain explicit placeholders.
- Association remains association.
- The unsupported universal recommendation is removed.
