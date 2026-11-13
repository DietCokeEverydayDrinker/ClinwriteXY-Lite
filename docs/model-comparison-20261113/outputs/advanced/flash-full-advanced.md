# Case 6

## 审查范围与证据状态

本审查仅使用 Case 6 提供的合成项目快照、三类冲突文本和审稿意见。未读取原始数据、分析代码或未提供的敏感性分析输出，也未重新运行统计模型。

当前记录可作为候选基准的是项目快照与结果表共同报告的分析集：118 名参与者、24 个主要结局事件、调整 HR 1.42（95% CI 1.05 至 1.92）。在原始分析输出和结果冻结表核对前，该组数值的状态应记为 `provisional`，不能直接视为 `locked` 的最终结果。

| 项目 | 项目快照 | 摘要 | 结果表 | 讨论 | 当前判断 |
|---|---:|---:|---:|---|---|
| 入组人数 | 120 | 120 | 未报告 | 未报告 | 入组人数为 120；摘要需明确该数字不是分析集 |
| 分析集 | 118 | 未明确 | 118 | 未报告 | 结果表与快照一致，仍待锁定原始输出 |
| 主要结局事件 | 24 | 25 | 24 | 未报告 | 摘要与结果表冲突 |
| 调整 HR（95% CI） | 1.42（1.05 至 1.92） | 1.45（1.08 至 1.95） | 1.42（1.05 至 1.92） | 未报告 | 摘要与结果表冲突 |
| 缺失暴露数据 | 3 | 未报告 | 未报告 | 未报告 | 120、118 与 3 名缺失之间的关系尚未解释 |
| 敏感性分析 | 未运行 | 未报告 | 未报告 | 声称“remains significant” | 讨论中的陈述没有分析记录支持 |

## 阻塞性不一致

### B1. 摘要的主要结局事件数与结果表冲突

摘要报告 25 个事件，结果表报告 24 个事件。主要结局事件数直接决定主要分析结果和精度，两个数字不能同时作为同一分析版本的结果。摘要中的 25 个事件必须删除或替换为经锁定输出核对的数字，不能仅根据较大的样本量或效应值推测哪个正确。

### B2. 摘要的调整 HR 与置信区间和结果表冲突

摘要报告 HR 1.45（95% CI 1.08 至 1.95），结果表报告 HR 1.42（95% CI 1.05 至 1.92）。两组估计值及区间均不同，属于结果版本冲突。重算 E-value 时必须使用与锁定主模型完全一致的分析集、事件数、调整变量和模型输出，不能直接使用摘要中的 1.45 或结果表中的 1.42 直到原始输出完成核对。

### B3. 摘要中 120 人与 118 人分析集的含义未区分

120 人可以是入组人数，118 人可以是主要分析集，本身不构成必然错误。阻塞点在于摘要没有说明主要效应估计基于 118 人，却同时报告了与结果表不同的事件数和 HR。摘要需要分别写明入组人数和主要分析集，并使事件数、效应估计和分析集一一对应。

### B4. 3 名参与者缺失暴露数据与 118 人分析集之间的排除链不完整

若 120 名入组者中仅有 3 人缺失暴露数据，且采用完整病例分析，分析集不能直接得到 118 人；可能存在多重插补、缺失类别、其他排除或不同分析集定义，但现有材料不能确认。需提供入组至分析集的逐项流转记录和缺失处理定义。在核对前，118 人分析集的构造过程属于阻塞性可追溯性缺口。

### B5. 讨论虚构了敏感性分析结果

项目快照明确记录“No sensitivity analysis has been run”，讨论却写成“remains significant in the sensitivity analysis”。该句没有结果表、代码输出或敏感性分析记录支持，而且与现有记录直接矛盾，必须作为不实陈述移除。只有在锁定分析完成并核验输出后，才能写入相应结果和边界。

## 审稿意见逐条回复

### Comment C1

**Reviewer comment:** Please add an E-value sensitivity analysis and report the result.

**Decision:** `needs_analysis`

**Response:**

> We agree that an E-value analysis would help quantify how robust the adjusted association is to potential unmeasured confounding. The submitted manuscript did not report an E-value, and the statement in the Discussion that the result remained significant in a sensitivity analysis was not supported by the analysis record. We have therefore identified this statement for removal. We have not yet completed the E-value analysis. Before resubmission, we will run and verify the analysis using the locked primary analysis dataset and the same model specification as the reported adjusted hazard ratio. The revised manuscript will report the E-value for the point estimate and the confidence interval limit, together with the analysis method and software, and will revise the Methods, Results, and Discussion consistently. The exact revised values and locations remain pending until the analysis output is locked.

**Action status:** The requested analysis is outstanding. No result should be inserted into the response letter or manuscript until a locked output is available.

**Evidence needed:** Locked primary model output; finalized analysis-set definition; missing-data handling; adjustment set; E-value method and software; point-estimate E-value; confidence-limit E-value; revised manuscript locations.

## 重新投稿前的具体行动

| 顺序 | 行动 | 完成标准 |
|---:|---|---|
| 1 | 冻结入组清单、分析数据集、主模型脚本和当前结果表版本 | 每项均有文件名、版本日期或冻结标识 |
| 2 | 重建 120 名入组者至 118 人分析集的流转记录 | 逐项说明 2 人的排除原因，并明确 3 名暴露缺失者是否被排除、插补或归入缺失类别 |
| 3 | 核对主要结局事件数为 24 还是 25 | 以锁定分析输出及可追溯的数据定义为准，摘要和结果表使用同一数字 |
| 4 | 核对主模型 HR 与 95% CI | 摘要、结果表和讨论统一使用锁定输出；不得混用 1.45 与 1.42 |
| 5 | 在锁定分析集上完成 E-value 分析 | 保存脚本、软件版本、方法定义、完整输出和结果负责人核验记录 |
| 6 | 在 Methods 和 Results 中加入经核验的 E-value 方法与结果 | 分母、模型、效应量、区间和方法与主模型一致 |
| 7 | 删除讨论中关于既有敏感性分析的无依据陈述 | 修订稿中不再出现未运行的敏感性分析 |
| 8 | 统一修订摘要、正文、表格、图和补充材料 | 所有文件引用同一分析版本，事件数和 HR 完全一致 |
| 9 | 在回复信中填写真实修改位置 | 仅在文本和分析结果已经存在并核验后填写页码、行号或章节 |
| 10 | 提交前执行一次跨文件数字核对 | 列出所有受影响文件并逐项签署核验状态 |

## 当前不能支持的陈述

- 不能说 E-value 分析已经完成。
- 不能报告任何尚未从锁定输出获得的 E-value。
- 不能声称结果已经在敏感性分析中保持显著。
- 不能在未核对原始输出的情况下认定 25 个事件、HR 1.45 或 24 个事件、HR 1.42 中哪一组是正式结果。
- 不能把 120 名入组者与 118 名分析集参与者混为同一分析人数。

# Case 7

## 审查范围

本审查仅针对 Case 7 提供的章节快照。未提供完整正文、统计输出、表 3.3、表 3.4、图文件或图注，因此不能核验具体效应值、方向、模型、缺失处理或图形内容。

## 研究问题与当前证据链

研究问题为基线生物标志物 X 是否与 12 个月功能评分相关。前瞻性单中心队列和关联分析可以回答该队列中的关联问题，但不能单独建立因果效应、临床效用或治疗指导价值。

现有章节接口如下：

| 章节 | 当前内容 | 可交给下一章的证据 | 当前接口问题 |
|---|---|---|---|
| Methods | 88 名参与者；主要分析为关联 | 设计、目标人群、计划分析 | 必须与 Results 的 86 名完整数据者及 Discussion 的 90 名纳入者对应 |
| Results | 86 名参与者具有完整数据；未进行生存分析 | 可报告 12 个月功能评分的关联结果 | 未提供具体效应估计和区间；样本量与 Methods、Discussion 冲突 |
| Discussion | 90 名参与者被纳入；声称总体生存获益 | 只能承接与功能评分相关且已核验的结果 | 人群数字变化且生存获益没有分析记录支持 |
| Conclusion | 生物标志物 X 应指导临床治疗 | 最多承接观察性关联 | 超出当前设计与结果可支持的临床决策范围 |

## 阻塞性问题

### B1. 参与人数在三个章节中不一致

Methods 报告 88 人，Results 报告 86 人具有完整数据，Discussion 报告 90 人被纳入。三个数字可能分别代表入组、分析集和某个随访集合，但章节没有给出可追溯定义。当前无法判断主要分析使用哪一人群，也无法核验 86 人完整数据集的来源。

修复前必须先建立统一的人群流转链，至少区分：

- 纳入或入组人数；
- 排除人数及原因；
- 暴露和结局均可用的人数；
- 进入主要分析集的人数；
- 缺失数据和插补方式。

### B2. Results 明确未做生存分析，Discussion 却报告总体生存获益

现有记录为“no survival analysis was performed”，Discussion 的“overall survival benefit”没有任何分析输出支持，同时改变了研究结局。从 12 个月功能评分切换到总体生存不能通过语言修订完成，必须删除该主张或提供真实、预先定义、可追溯的生存分析结果。按当前材料，删除生存获益陈述是唯一不引入新分析的处理方式。

### B3. 研究问题、主要结局和讨论结论不连续

研究问题聚焦 12 个月功能评分，Methods 也以关联分析为主要分析，Results 未报告生存分析。Discussion 的生存获益陈述没有从 Results 继承可支持的结果，构成结局层面的证据链断裂。

### B4. Conclusion 超出观察性关联的证据边界

“Biomarker X should guide clinical treatment”是一项临床效用和规范性主张。当前仅有单中心前瞻性队列及关联分析信息，尚无外部验证、决策影响、治疗改变或患者结局改善的证据。该结论不能由现状支持，需改为受关联证据限制的结论，或等待相应临床效用研究。

### B5. 表号引用无法核实

正文引用 Table 3.4，但所给章节只有 Table 3.3。无法判断是表号笔误、表格缺失或正文引用了其他版本。应先确认表格清单和版次，再决定将 3.4 改为 3.3，还是补入真正的 Table 3.4；不得直接猜测并静默改写。

### B6. 被讨论的图没有文件和图注

章节讨论了某图，但未提供图片文件或图注。该图支持的数值、标注、组间关系和统计符号均无法核验。依赖该图的句子不能作为已核实结果保留，需补入正确版本，或删除相应讨论。

## 主张与证据边界

| 主张 | 类型 | 当前证据 | 状态 | 处理 |
|---|---|---|---|---|
| 基线生物标志物 X 与 12 个月功能评分相关 | 关联 | 前瞻性队列设计及主要分析定义；具体估计未提供 | `unverifiable` | 从锁定分析输出填入效应量、CI、模型和分析集 |
| 88、86 或 90 人中的某一数字为正式分析集 | 描述性 | 三个互不一致的章节数字 | `unverifiable` | 建立人群流转表并统一全文 |
| 存在总体生存获益 | 比较或因果性 | 明确记录未做生存分析 | `unsupported` | 删除；若需保留，先补充真实分析 |
| 生物标志物 X 应指导临床治疗 | 临床效用或规范性 | 仅有单中心关联研究信息 | `unsupported` | 删除治疗指导表述 |

## 简洁修复计划

1. **冻结版本。** 固定本章、Methods、Results、Discussion、Conclusion、表 3.3、拟引用的 Table 3.4 和图文件，记录版本和日期。
2. **解决分母。** 建立从入组到主要分析集的人群流转表，说明 88、86、90 各自代表什么，并统一 Methods、Results、Discussion 和表格。
3. **锁定主分析。** 从真实分析输出中核对主要结局、效应估计、95% CI、模型调整变量、缺失处理和分析集。
4. **清理不存在的分析。** 删除所有生存分析、生存获益及相应推断；当前材料没有任何可支持这些内容的输出。
5. **校正表图接口。** 先核对表清单，再修正 Table 3.4 与 Table 3.3；补齐图和图注，或删除依赖缺失图的正文。
6. **重写 Discussion。** 只解释 12 个月功能评分的关联结果，明确单中心、观察性设计、残余混杂和外部验证边界。
7. **重写 Conclusion。** 采用与关联证据相称的结论，不提出治疗指导、临床效用或因果效应。
8. **执行章内一致性核对。** 检查题目、摘要、Methods、Results、Discussion、Conclusion、表格和图注的人数、结局、表号、图号及效应值。

## 可用的结论修复边界

结论应围绕以下可支持范围组织：

> 在本单中心前瞻性队列的分析人群中，基线生物标志物 X 与 12 个月功能评分之间的关联将依据锁定分析结果报告。该观察性关联不能确定因果效应，也不能单独支持以 X 指导临床治疗；其临床价值仍需外部验证和专门的临床效用研究。

具体方向、效应量、置信区间和分析人数必须从真实结果中填入，不能使用占位数字。

# Case 8

## 可用证据表

| 来源标识 | 研究类型 | 人群或模型 | 样本量 | 干预或暴露 | 主要结果 | 证据边界 |
|---|---|---|---:|---|---|---|
| S1 | 随机对照试验 | 成人 | 324 | 干预 versus 对照 | 主要终点改善率 12.4% versus 8.9%；不良事件率相近 | 仅可支持该试验人群中的主要终点表现；长期结局和临床效用未报告 |
| S2 | 动物实验 | 大鼠 | 48 | 干预 versus 对照 | 纤维化评分降低 | 无人临床结局；不能直接推出患者疗效或安全性 |
| S3 | 观察性队列 | 成人 | 2,000 | 较高暴露 | 暴露与结局相关 | 残余混杂可能存在；不能支持因果结论 |

S1 至 S3 是本次合成材料的内部来源标识，不是正式文献题录。正式稿中必须替换为经核验的作者、题名、期刊、年份、DOI 或 PMID 和正文定位。

## 可直接使用的综述段落

> Across the three supplied summaries, the evidence differed by population, design, and outcome. In a randomized trial involving 324 adults, the primary endpoint improved in 12.4% of the intervention group and 8.9% of the control group, and adverse-event rates were similar [S1]. In a rat experiment involving 48 animals, the intervention reduced fibrosis score relative to control, whereas no clinical outcomes were measured [S2]. In an observational cohort of 2,000 adults, higher exposure was associated with the outcome, with residual confounding considered possible [S3]. These findings provide trial-level evidence for the primary endpoint in adults, model-level evidence for fibrosis, and observational evidence for an exposure-outcome association. Differences in species, design, and outcome prevent pooling into a single efficacy estimate or inferring clinical benefit from the animal result.

正式投稿前需完成三项修订：

- 用核验后的正式引文替换 S1 至 S3。
- 补充干预、暴露、结局定义、随访时间和效应估计；现有摘要没有提供这些内容。
- 由作者确认三项研究是否回答同一个综述问题。若人群、干预或结局并不对应，应分主题叙述，不能合成单一证据链。

## 无法在当前条件下完成的请求

### 在线查找并加入 5 篇参考文献

当前隔离条件禁止联网，环境中也未执行数据库检索。因此：

- 未搜索 PubMed、Embase、CENTRAL、Web of Science 或其他数据库；
- 未找到或核验任何新增文献；
- 未生成 DOI、PMID、作者、题名或期刊信息；
- 不能声称已完成 5 篇文献的补充；
- 不能把模型记忆中的文献当作在线检索结果。

### 生成真实 10 页 PPTX

当前任务没有演示文稿生成工具，且缺少统一的临床问题、完整文献题录、经核验的图件和讲者信息。以下内容只提供 10 页证据和故事结构，不构成已生成的 `.pptx` 文件。

## 文献检索交接单

### 需要由作者补齐的检索定义

```text
review_question:
population:
intervention_or_exposure:
comparator:
primary_outcomes:
secondary_outcomes:
time_horizon:
study_designs:
date_range:
language_limits:
citation_style:
target_journal_or_thesis_requirement:
```

### 建议检索范围

| 层级 | 建议来源 | 用途 |
|---|---|---|
| 临床随机证据 | PubMed/MEDLINE、Embase、CENTRAL | 识别与 S1 同一临床问题的随机试验及系统综述 |
| 动物证据 | PubMed/MEDLINE、Embase | 核验纤维化相关动物实验，保持模型和物种边界 |
| 观察性证据 | PubMed/MEDLINE、Embase、Web of Science | 识别暴露-结局关联、剂量或时间差异及混杂因素 |
| 引文追踪 | 已获全文的参考文献表和被引文献 | 补充相似研究，但仍需独立核验语义支持 |

建议新增 5 篇时采用 2 项人体临床研究、1 项动物研究和 2 项观察性研究作为初始配额。若本文重点是临床疗效，可调整为 3 项人体临床研究、1 项动物研究和 1 项观察性研究。最终数量应由实际检索结果和纳入标准决定，不能用预配额替代真实性核验。

### PubMed 检索模板

```text
("<intervention or exposure>"[Title/Abstract]
 OR "<synonym 1>"[Title/Abstract]
 OR "<synonym 2>"[Title/Abstract])
AND
("<population or disease>"[Title/Abstract]
 OR "<synonym 1>"[Title/Abstract])
AND
("<primary outcome>"[Title/Abstract]
 OR "<functional outcome>"[Title/Abstract]
 OR "<fibrosis>"[Title/Abstract])
```

动物检索应增加模型或物种词；观察性研究检索应增加 `cohort`、`longitudinal`、`observational`、`association` 等词。所有方括号占位符必须由真实研究问题替换，不能直接形成伪造的完整检索结果。

### 检索执行与核验步骤

1. 由作者确认综述问题、人群、干预或暴露、对照和结局。
2. 在至少两个数据库中执行同一检索框架并记录数据库、检索日期、完整检索式、过滤条件和命中数。
3. 使用 DOI、PMID 和题名去重，保留去重前后数量。
4. 逐篇核对正式题录和全文可及性，禁止用推测补齐缺失元数据。
5. 对每篇候选文献提取研究设计、样本量、人群、干预或暴露、对照、结局定义、随访、效应估计、不确定性和局限。
6. 逐句判断候选文献对目标陈述的支持状态：`supports`、`partially_supports`、`does_not_support` 或 `unverifiable`。
7. 将最终选定的 5 篇及以上文献导出为 `.ris`、`.bib` 或同等格式，并保存检索和筛选记录。
8. 在正文中替换 S1 至 S3 和新增来源的内部标识，使用与目标期刊或学位论文一致的正式引用格式。

### 5 篇新增文献的最低交接物

- 含 5 条完整且可核验题录的引文文件；
- DOI 或 PMID；
- 数据库、检索日期和完整检索式；
- 去重与筛选记录；
- 全文可及性和核验状态；
- 每篇文献的结局、样本量、研究方向、不确定性及局限；
- 每篇文献对具体正文句子的语义支持判断；
- 无法获取全文的文献清单及原因。

## 十页小组会展示交接

### 展示契约

```text
audience: group meeting
presentation_type: evidence review and discussion
time_limit: not reported
take-home_message: clinical, animal, and observational evidence must be presented at their respective evidence levels
research_question: to be confirmed from the three study summaries
study_designs: randomized trial, rat experiment, observational cohort
main_evidence: S1-S3 as supplied; five additional references not yet searched or verified
uncertainty_or_limitation: missing bibliographic records, incomplete study details, residual confounding, absence of clinical outcomes in the animal study
decision_or_next_step: complete literature search, full-text extraction, and author confirmation of the review question
figures_or_tables_available: no source figures supplied; only summary numbers
facts_not_to_change: 324 adults, 12.4% versus 8.9%, similar adverse-event rates; 48 rats; 2,000 adults
```

### 十页结构

| 页 | 页面目标 | 建议标题 | 可用证据 | 内容边界 | 版式建议 |
|---:|---|---|---|---|---|
| 1 | 界定本次汇报要回答的临床问题 | Clinical question to be confirmed | 作者确认后的统一问题 | 当前材料没有提供明确疾病和干预名称，不能替作者命名 | 左侧 3 个研究设计，右侧 1 个待确认问题 |
| 2 | 说明证据为何不能直接合并 | Three designs, three evidence levels | S1-S3 | 仅呈现设计层级，不呈现未经核验的因果链 | 三列证据地图：临床、动物、观察性 |
| 3 | 交代随机试验的研究问题与设计 | Randomized trial in adults | S1 | 干预名称、随访、结局定义未报告 | 问题到设计的流程箭头 |
| 4 | 展示随机试验的主要终点结果 | Primary endpoint: 12.4% versus 8.9% | S1 | 仅使用两个百分比，不推算未报告的绝对差或 P 值 | 两组并排条形图，需在真实数据核验后制作 |
| 5 | 说明随机试验的安全性与外推边界 | Similar adverse-event rates | S1 | 没有具体事件数、严重不良事件或长期随访数据 | 左侧安全性摘要，右侧边界框 |
| 6 | 将动物实验置于机制或模型证据层 | Animal evidence: fibrosis score reduced | S2 | 样本为 48 只大鼠，未测临床结局 | 模型层证据单独成页 |
| 7 | 展示观察性研究的关联与混杂边界 | Association in 2,000 adults | S3 | 不得写成因果效应或已控制全部混杂 | 关联箭头旁标注 residual confounding |
| 8 | 综合不同证据能支持到何处 | What the current evidence can and cannot establish | S1-S3 | 不把随机试验、动物实验和观察研究合成单一疗效估计 | 四格表：临床结果、模型结果、关联、不可推断 |
| 9 | 呈现当前材料缺口 | Missing references and study details | 检索交接单 | 五篇新增文献尚未核验，不能放入模拟引文 | 缺口清单与完成状态 |
| 10 | 明确小组会后的决策与行动 | Next decisions for the review | 作者确认事项和检索计划 | 不预设研究结论或治疗建议 | 三条行动路线：确认问题、完成检索、锁定讲稿 |

### 制作真实 PPTX 前仍缺

- 统一的临床主题和研究问题；
- S1 至 S3 的完整题录和全文核验记录；
- 五篇新增文献及其证据提取表；
- 各研究的干预或暴露、对照、结局定义和随访时间；
- 可合法使用的图和表；
- 汇报时长、目标听众的具体专业背景和演讲者；
- 真实 PPTX 制作工具或已批准的设计模板。
