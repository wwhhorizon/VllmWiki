# 方法论

## 源数据层

- 原始 issue 正文：`all/data/raw/issues_raw.jsonl`
- 原始 PR 正文：`all/data/raw/prs_raw.jsonl`
- 分类提示：`all/data/tables/cases.csv` 与 `all/data/tables/prs.csv`
- Issue-PR 链接提示：`all/data/tables/issue_pr_links.csv`

## 抽取原则

本 wiki 将证据和推断分开。

- 证据：标题/正文摘录、PR 描述、linked PR 证据字符串、URL。
- 路由提示：category、work area、symptom、root-cause hint、hardware scope、operator keywords。
- 推断：候选优化 pattern、代表性 case 排名、领域级 lesson。

## 为什么第一版使用候选 Pattern

本地数据集包含 issue 和 PR 正文，但没有讨论评论正文。很多最终 resolution 存在于评论里，所以生成器会把依赖评论的 case 标记为不完整，而不是假装已经知道最终根因。

## 迭代计划

1. 从所有原始 issue 和 PR 构建 source-backed 骨架。
2. 优先处理有 linked PR、高评论数、高 pattern 分数或 manual-review 标记的 case。
3. 抓取/阅读讨论评论和 PR review 上下文。
4. 只有在源证据确认根因与修复后，才把候选 pattern 提升为 curated lesson。
5. 保留 `evidence/pattern_evidence.csv` 作为所有提升结论的审计 ledger。
