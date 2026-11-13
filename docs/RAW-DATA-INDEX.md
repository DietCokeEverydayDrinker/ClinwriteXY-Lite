# 原始输入与六组输出索引

本页把模型对比实验的原始材料直接展开到文件级。所有输入均为公开事实摘要或明确
标注的合成项目快照，不包含患者标识、真实病历、医院内部文件或未公开课题。

## 原始输入

每个输入文件都保留病例事实、任务要求和必须遵守的边界，六种条件使用完全相同的
输入文本。

- [基础病例 1–5：原文、已知事实和任务](model-comparison-20261113/cases/BASIC-CASES.md)
- [高阶病例 6–8：跨文件审计、学位论文接口和多研究综合](model-comparison-20261113/cases/ADVANCED-CASES.md)

## 六种组合的完整文字输出

每个链接都是原始 Markdown 文件。基础输出文件包含病例 1–5 的完整回答，高阶输出
文件包含病例 6–8 的完整回答。

| 条件 | 基础病例 1–5 | 高阶病例 6–8 |
|---|---|---|
| DeepSeek V4 Flash Raw | [完整输出](model-comparison-20261113/outputs/basic/flash-raw.md) | [完整输出](model-comparison-20261113/outputs/advanced/flash-raw-advanced.md) |
| DeepSeek V4 Flash + Lite | [完整输出](model-comparison-20261113/outputs/basic/flash-lite.md) | [完整输出](model-comparison-20261113/outputs/advanced/flash-lite-advanced.md) |
| DeepSeek V4 Flash + Full | [完整输出](model-comparison-20261113/outputs/basic/flash-full.md) | [完整输出](model-comparison-20261113/outputs/advanced/flash-full-advanced.md) |
| DeepSeek V4 Pro Raw | [完整输出](model-comparison-20261113/outputs/basic/pro-raw.md) | [完整输出](model-comparison-20261113/outputs/advanced/pro-raw-advanced.md) |
| DeepSeek V4 Pro + Lite | [完整输出](model-comparison-20261113/outputs/basic/pro-lite.md) | [完整输出](model-comparison-20261113/outputs/advanced/pro-lite-advanced.md) |
| DeepSeek V4 Pro + Full | [完整输出](model-comparison-20261113/outputs/basic/pro-full.md) | [完整输出](model-comparison-20261113/outputs/advanced/pro-full-advanced.md) |

## 评分、核对点与复现文件

- [基础病例核对点](model-comparison-20261113/EXPECTED-CHECKS.md)
- [高阶病例核对点](model-comparison-20261113/ADVANCED-EXPECTED.md)
- [测试协议](model-comparison-20261113/PROTOCOL.md)
- [评分 JSON 与盲评映射](model-comparison-20261113/scores)
- [图表源数据](model-comparison-20261113/data)
- [输出检查脚本](model-comparison-20261113/check_outputs.py)
- [绘图脚本](model-comparison-20261113/make_figures.py)

## 已知边界

这是一项内部合成评测，不是临床有效性研究，也不是人类同行评审。病例数量有限，
不能证明论文接收率、盲审通过率或 AI 检测率会变化。短篇分数也不能替代整篇论文、
真实返修、统计复算和作者人工复核。
