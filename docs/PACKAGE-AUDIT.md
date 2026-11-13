# Lite 安装包与仓库内容审计

## 结论

ClinwriteXY Lite 的公开仓库包含两类内容：

1. 可安装的 Lite Skill；
2. 用于模型对比、评分复核和图表复现的公开评测材料。

完整版 ClinwriteXY 的规则文件、项目管理模板、跨文件审计模块、审稿回复模块和
脚本没有进入 Lite 安装包。

公开评测目录保留了两项可能被误认为“完整版内容”的材料：

- `Flash + Full` 和 `Pro + Full` 在 8 个公开病例上的模型生成答案，共 4 份；
- 六种条件的评分与图表材料。

这些内容是测试输出和评测数据，不包含完整版 `SKILL.md`、写作参考全文、项目模板
或内部工作流源码。它们保留在仓库中用于复现公开结论，交付给用户的 minimal ZIP
不包含这些文件。

## 安装包内容

minimal ZIP 只包含运行 Lite 所需的文件：

```text
clinwritexy-lite/
  SKILL.md
  VERSION
  LICENSE
  README.md
  PACKAGE-MANIFEST.txt
  agents/openai.yaml
  references/*.md
  scripts/check_preservation.py
  scripts/test_check_preservation.py
```

它不包含：

- `docs/` 下的模型评测、病例原文、Full 条件输出和图片；
- `evaluation/` 与 `evals/`；
- Git 历史；
- 完整版 ClinwriteXY 的任何文件。

## 体积说明

GitHub 仓库包含评测图片、PDF、SVG、评分 JSON、12 份组合输出和 Git 历史，因此
下载整个仓库会明显大于完整版 Skill 文件夹。Lite 的运行核心约 37 KiB；主要体积
来自 `docs/` 与 `.git/`。

用户安装时应下载 Release 中的 `ClinwriteXY-Lite-<version>-minimal.zip`，不要直接
把整个 GitHub 仓库复制进宿主 Agent 的 skills 目录。
