# ClinwriteXY Lite

中文优先的临床论文段落写作与证据边界检查 Skill。它处理一段摘要、结果、讨论或
结论，在改善中英文表达的同时，保住数字、分母、引用、限定词和结论强度。

> 改得像论文，也保住数字和结论边界。

**在线实验页：** [ClinwriteXY 模型对比实验](https://dietcokeeverydaydrinker.github.io/ClinwriteXY-Lite/)

## 使用反馈

试过 Lite 后，可以在 Discussions 留下真实记录：

- [使用反馈](https://github.com/DietCokeEverydayDrinker/ClinwriteXY-Lite/discussions/categories/show-and-tell)：
  写清 Agent、模型、任务类型、实际效果和仍然不足的地方。
- [问题报告](https://github.com/DietCokeEverydayDrinker/ClinwriteXY-Lite/discussions/categories/q-a)：
  安装失败、脚本报错或输出异常时，提供版本、复现步骤和脱敏报错信息。
- [功能建议](https://github.com/DietCokeEverydayDrinker/ClinwriteXY-Lite/discussions/categories/ideas)：
  说明现有流程解决不了什么问题，以及希望 Lite 增加哪种能力。

反馈只使用合成、公开或充分脱敏的材料，不要粘贴患者信息、账号凭据、未发表稿件
或受限原始数据。GitHub Star 只表示收藏，不表示评分；真正使用后再 Star 即可。

## 项目缘起

ClinwriteXY 来自我自己的临床科研工作。过去半年，我把真实论文写作、返修、审稿回复、
数据核对和项目复盘持续沉淀进个人知识库，再从约数百页中英文材料中抽取可复用的规则。
后来发现，单段写作可以用一套较轻的流程完成，整篇论文还需要项目记忆和跨文件核对，
于是拆成开源 Lite 与买断完整版：Lite 保留最常用的单段写作能力，完整版保留更完整的
写作系统、证据链和项目流程。

## Lite 与 9.9 元完整版：上限差在哪里

| 工作环节 | 开源 Lite | 完整版 ClinwriteXY |
|---|---|---|
| 输入范围 | 一段中文或英文摘要、结果、讨论、结论 | 整篇 SCI 手稿、学位论文、多章综述和完整投稿包 |
| 写作系统 | 单段写作、证据冻结和数字保真 | 从约数百页个人科研知识库中抽象出的六层写作系统：论证、中文表达、英文护栏、章节动作、功能短语、双语等价 |
| 数据到正文 | 根据作者已提供的少量结果写一段 | 结果表、分析集、分母、模型参数和正文之间建立对应关系，并追踪版本 |
| 项目状态 | 每次任务独立处理 | 项目护照、权威文件、数据与结果版本、关键决策、待办和恢复卡 |
| 证据与引用 | 单段论点边界和双语口径检查 | 全篇论点证据表、四层引用完整性、报告规范映射和跨章节结论边界 |
| 复现链 | 机械检查数字、分母和常见引用标记 | 追踪结论、表、图、脚本、参数、数据版本和正文之间是否断链 |
| 返修 | 不覆盖完整返修流程 | 学位论文与投稿审阅、审稿意见逐条回复、真实修改位置映射和返修台账 |
| 汇报 | 不生成页面方案 | 按论证给出逐页目标、图表选择、文字示意和 speaker note |
| 协作成长 | 固定规则，不保存项目状态 | 可选协作偏好；新经验先进入本地候选，经用户确认后才可能形成工作包 |

完整版最核心的增量集中在写作与语言润色。它把中英文论文和学位论文中的论证顺序、
章节接口、中文去模板化、英文时态与动词强度、功能短语、限定词、引用口径和双语等价
拆成可调用规则，覆盖摘要、引言、方法、结果、讨论、结论、局限性、审稿回复等场景。
这些规则来自长期真实科研写作和反复修改，细化到段落动作、句子功能和常见误改边界。
相较于 GitHub 上多数偏通用或单段的开源写作 Skill，完整版把语言修改、证据边界、
数字分母、章节结构和项目记录放进同一条工作流，形成更直接、更细颗粒度的写作支持。

完整版的“上限提升”来自覆盖更多环节，不承诺把同一段文字再提高固定分数。本轮
5 个脱敏基础写作病例中，Lite 与 Full 同为 `122.5/125`；完整版的价值主要在短篇
分数没有覆盖的整篇论文、多文件核对、项目恢复和完整返修。实际效果取决于输入材料、
模型和人工复核。

完整版的详细增量见
[Lite 与完整版能力对照](https://github.com/DietCokeEverydayDrinker/ClinwriteXY-Lite#lite-与-99-元完整版上限差在哪里)；
需要整篇论文、多文献证据综合、跨文件结果核对、审稿回复或长期项目记录时使用完整版。

**完整版当前状态：爱发电认证审核中。** 认证完成前，可以通过
[我的小红书主页](https://www.xiaohongshu.com/user/profile/69666bf30000000003012a27)
查看商品和私信购买。完整版源码不公开，Lite 的开源许可不改变完整版的购买者授权。

## 模型对比结果

2026-11-13 使用 5 个基础写作病例和 3 个高阶综合病例，对比 DeepSeek V4 Pro、
V4 Flash 分别搭配 Raw、ClinwriteXY Lite 和 ClinwriteXY Full 的表现。

在 5 个基础病例中：

| 条件 | 盲评均值 |
|---|---:|
| Flash Raw | 109.5 / 125 |
| **Flash + Lite** | **122.5 / 125** |
| Flash + Full | 122.5 / 125 |
| Pro Raw | 118.0 / 125 |
| Pro Lite | 119.0 / 125 |
| Pro Full | 119.5 / 125 |

Flash + Lite 和 Flash + Full 保留了关键病例中的 `1,702` 与 `851` 两个队列
样本量，Pro 三种条件和 Flash Raw 均遗漏。本轮短篇写作证据支持：

> 使用 V4 Flash + ClinwriteXY Lite，以更低成本达到接近或略高于 V4 Pro Raw
> 的盲评水平。

这个结论只适用于本轮脱敏短篇写作病例，不能外推到所有论文、真实投稿或所有临床
亚专科。完整方法与评分锚点见
[模型对比实验](docs/model-comparison-20261113/README.md)；8 个病例的原始输入和
六种组合的 12 份完整文字输出可直接进入
[原始输入与六组输出索引](docs/RAW-DATA-INDEX.md)。

![模型总体表现](docs/model-comparison-20261113/assets/figure-1-overall-performance.png)

**English summary:** ClinwriteXY Lite is a small clinical-writing skill for one
Chinese or English abstract, results, discussion, limitation, or conclusion
paragraph. It drafts from supplied facts, calibrates claims to the available
evidence, aligns bilingual abstracts, and checks whether numeric or citation
tokens changed during editing.

## 适合谁

- 正在写临床 SCI 结果、讨论、摘要或学位论文段落的硕博研究生；
- 需要把中文医学文字改得更自然，同时不能改动数字、分母和结论强度的人；
- 想把英文摘要与中文结果逐项对齐，排查样本量、终点和验证层级错位的人；
- 想在交给导师或润色机构前，先做一次短段落证据边界检查的人。

## 独特之处

Lite 把四个环节压进一个小包：

1. **先冻结证据，再改语言**：先确认研究设计、分母、效应量、验证层级和结论类型。
2. **中文临床微编辑**：处理名词堆叠、长定语、空泛评价、机械转折和翻译腔。
3. **证据到语言映射**：把关联、预测、诊断、机制和临床效用分开处理。
4. **可运行的保真检查**：脚本可发现修改前后数字和常见引用标记的增删，减少肉眼漏看。

GitHub 上已有覆盖面很广的科研写作 Skill。Lite 的定位更窄：集中处理临床论文的
单个高风险段落，并让证据边界、中文表达和机械保真检查出现在同一条工作流里。

## Why Lite

通用写作 Skill 往往能润色语言，却容易漏掉临床写作里的高风险变化：

- 把关联写成因果；
- 把内部验证写成外部验证；
- 把 AUC 写成临床获益；
- 把统计显著写成临床重要；
- 改写时丢失分母、置信区间或限定词；
- 中英文摘要的人群、终点或结论强度不一致。

Lite 把这些问题压缩在单段工作流里。它比完整版轻，但可以独立完成实际工作，不依赖
完整版的提示词。

## What it does

- 从作者提供的分析结果起草一段正文；
- 修改一段中文或英文临床论文文字；
- 检查一段话的结论是否超过现有证据；
- 对齐中英文摘要中的人群、样本量、终点、效应方向和结论强度；
- 检查修改前后数字与引用标记是否被增删。

默认范围为一中文段落不超过 800 字，或一英文段落不超过 500 words。

## What it does not do

- 不搜索实时文献，不核验 DOI 是否存在；
- 不重新运行统计分析；
- 不审阅整篇学位论文或完整投稿包；
- 不处理 Word 修订、批注、目录、页码和复杂排版；
- 不生成成品 PPT；
- 不恢复长期项目状态；
- 不代替作者、导师、统计师、伦理委员会或期刊审稿人。

需要检索、文献管理、Word 修订、图表或完整论文流程时，请另装对应工具。

## Install

**不要直接把整个 GitHub 仓库装进 Agent。** 仓库中的 `docs/` 是公开评测证据，
包含 4 份 Full 条件的模型生成答案和图片，不属于 Lite 安装包。

从 [Releases](https://github.com/DietCokeEverydayDrinker/ClinwriteXY-Lite/releases)
下载 `ClinwriteXY-Lite-0.2.0-minimal.zip`。解压后应得到一个
`clinwritexy-lite/` 文件夹，其第一层包含 `SKILL.md`。该精简包不包含评测目录、
Full 条件输出、评分 JSON 或 Git 历史。

### Codex

把解压后的 `clinwritexy-lite` 文件夹整体放入：

```text
%USERPROFILE%\.codex\skills\clinwritexy-lite
```

macOS 或 Linux 通常放入：

```text
~/.codex/skills/clinwritexy-lite
```

重启或新开 Codex 会话，然后直接说明任务，或显式调用：

```text
Use $clinwritexy-lite to revise this clinical results paragraph.
```

### Claude Code or another SKILL.md host

把整个目录放入宿主约定的 skills 目录。也可以把目录附加给 Agent，并要求它先读取
`SKILL.md`。不要只复制 `SKILL.md`，因为语言规则、证据边界和摘要对齐规则位于
`references/`。

如果选择从源码手动安装，只需要：

```text
SKILL.md
VERSION
LICENSE
README.md
agents/
references/
scripts/check_preservation.py
scripts/test_check_preservation.py
```

`docs/`、`evaluation/` 和 `evals/` 可以留在仓库中供复核，无需放进 skills 目录。

只要宿主支持读取 `SKILL.md` 及目录内引用文件，就可以尝试使用。Codex 用户可以
直接安装；Claude Code、DeepSeek Harness、WorkBuddy 或其它 Agent 的具体安装目录
和触发方式，以各自当前版本的文档为准。

安装后先用一个不含患者信息的短段落测试。建议新开会话，确认模型确实读取了
`SKILL.md` 和所需 `references/`，再用于真实稿件。

## 30-second test

```text
使用 ClinwriteXY Lite 修改下面这段：

模型A的AUC为0.86，可准确预测患者预后并指导临床治疗。研究完成了内部验证，
未做外部验证，也未进行决策影响研究。

要求：保留全部数字和验证层级，不要新增引用或结果。
```

预期行为：保留 `0.86`、`内部验证` 和 `未做外部验证`，把“准确预测”和
“指导临床治疗”收回到证据能够支持的范围，并指出仍需补充校准、外部验证和临床
效用证据。

## Preservation check

安装后可运行：

```text
python scripts/check_preservation.py original.txt revised.txt
```

脚本检查数字和常见引用标记是否被增删。它只做机械诊断，不能判断引用是否真的支持
句子。发现差异后仍需人工核对上下文。

它也不能自动判断分母是否被换了研究对象、内部验证是否被写成了外部验证，或关联
是否被写成了因果。这些项目由 Skill 的审阅规则处理，仍需要作者最终确认。

运行内置测试：

```text
python -m unittest discover -s scripts -p "test_*.py"
python scripts/validate_evals.py evals/cases.jsonl
```

## Privacy

不要提交患者姓名、住院号、影像、联系方式、医院内部账号、未脱敏原始数据或受限
机构文件。使用云端模型时，材料会受所用 Agent 和模型服务的数据政策约束。公开示例
应保持合成内容。

真实稿件应先脱敏，并遵守所用 Agent、模型服务和机构的数据政策。Lite 不提供患者
诊疗建议，也不替代导师、统计师、伦理委员会或期刊审稿人。

## 免责声明

ClinwriteXY 提供科研写作、证据整理和信息核查辅助，不构成医疗诊断、治疗建议或
研究伦理审查意见。AI 输出可能出现遗漏、误读、错误引用或事实幻觉，使用者必须
核对原始数据、统计分析、文献全文、引用关系和所属机构要求，并对最终稿件负责。
Lite 与完整版均不承诺论文录用、盲审通过、查重结果或 AI 检测结果；第三方 Agent、
模型、API、文献检索和文献管理服务受各自条款与数据政策约束。

## License

本仓库使用 MIT License。完整版 ClinwriteXY 使用独立的购买者授权，不因 Lite 开源
而改变。

## Full version

完整版当前价格为 9.9 元，面向整篇论文、学位论文、多文献证据综合、审稿回复和
项目恢复。相对 Lite，额外包含：

- 中英文论文与学位论文写作、证据审计和结论校准；
- 多研究综述、临床与动物证据分层、逐句引用定位；
- 项目状态恢复、数据版本记录、跨文件结果核对；
- 审稿意见逐条回复、修改位置映射和返修台账；
- 论文或学位论文的逐页汇报设计；
- 个人科研知识库中关于中英文表达、逻辑接口和去模板化的六层规则，
  细化到段落动作、句子功能、常见误改边界和可执行示例；
- 可选协作偏好与受控成长候选机制。

**完整版当前由爱发电认证审核中，暂未把爱发电商品页作为主要入口。**

当前购买与咨询入口：

- [小红书主页：无糖可乐每日饮](https://www.xiaohongshu.com/user/profile/69666bf30000000003012a27)
- [Bilibili：无糖可乐每日饮](https://space.bilibili.com/198039978)

完整版为一次性买断，不包含固定频率更新、定制安装、一对一论文修改或无限期维护。
价格、当前交付版本和售后范围以小红书商品页说明为准。
