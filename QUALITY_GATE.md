# 质量门

## 覆盖率门

- 原始 issue 覆盖目标：15,818 个 issue 出现在 `indexes/issues.csv` 中。
- Operator/kernel case 覆盖目标：7,239 个去重 case 有生成 case 页或索引行。
- PR 覆盖目标：8,931 个 PR 出现在 `indexes/prs.csv` 中。
- `indexes/issues.csv` 的每一行都必须有存在的 `wiki_page`。

## 证据门

一个 wiki lesson 被视为 curated 前，必须具备：

- 至少一个源 issue 或 PR URL。
- 来自 issue body、PR body 或已抓取评论的源正文摘录。
- 明确的抽取来源：raw body、PR body、comment 或 manual review。
- 置信状态：candidate、reviewed 或 curated。
- 清楚地区分 symptom、suspected root cause、confirmed root cause 和 fix。

## 防偷懒门

- 不要把只来自表格的结论提升为 curated lesson。
- 没有源证据时，不要把 `root_cause_hint` 当成根因。
- 不要只根据 `closed` 状态推断修复。
- 对有评论的 issue，在评论正文抓取完成或明确标记不可用前，不要总结成完整结论。
- 不要因为共享关键词就合并无关 issue family。
- 除非页面明确写着 `reviewed` 或 `curated`，否则把本 wiki 内容视为 `candidate`。

## 采样门

每轮迭代中，每个领域页都应：

- 复核分数最高的 20 个 case。
- 至少复核 10 个 linked-PR case。
- 至少复核 10 个 open issue。
- 至少复核 10 个高评论数但缺失评论正文的 issue。
- 记录 false positive 并更新 pattern 规则。

## 完整性标签

- `candidate`：由 raw body 和表格提示生成。
- `reviewed`：人类/agent 已阅读完整源 issue 和 linked PR body。
- `curated`：在 reviewed 基础上检查了评论或 maintainer resolution，并写成稳定 lesson。
- `blocked`：需要源评论或外部数据，但当前缺失。
