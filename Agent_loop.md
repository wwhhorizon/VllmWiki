# Agent Loop

状态：Codex 自主迭代规划。
作用：规定每轮 agent 如何从证据走向 wiki 结论。

## 输入

每轮先读取：

1. [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)：仓库边界、证据规则、质量门。
2. 当前专题入口。例如 bitwise 专题为 [curated/bitwise/README.md](curated/bitwise/README.md)。
3. 当前专题 next queue。例如 [curated/bitwise/next.md](curated/bitwise/next.md)。
4. 当前专题 ledger。例如 [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv)。
5. 仓库外 targeted evidence，由本地 source layer 提供；公开文档不记录机器绝对路径。

## 每轮目标

每轮只选择 1-3 个 bounded item，优先级：

1. `priority=high`
2. `risk_status=unresolved_review_risk`
3. `risk_status=include_with_boundary`
4. `risk_status=defer_blocked`

每轮必须产出一种实质变化：

- 新 insight 下沉到机制页；
- 或 ledger 状态、阻塞原因、下一步更精确；
- 或 next queue 被更新；
- 或明确说明为什么不能 promotion。

## 精读要求

对每个对象尽量读取：

- issue body
- issue comments
- timeline
- PR body
- changed files / patch
- review comments
- reviews
- linked PR / commit 线索

精读后必须回答：

- 观察到的现象是什么？
- root cause 是否闭环？
- fix 是根因修复、workaround、support gate、test placement，还是尚未修复？
- exact test 覆盖了什么？
- 未覆盖的边界是什么？
- 该 claim 应该 `include`、`include_with_boundary`、`defer` 还是 `exclude`？

## Promotion 规则

可以进入机制页的结论必须同时具备：

- source evidence；
- root cause；
- fix pattern 或明确 workaround/scope gate；
- verification contract；
- applicable boundary。

不能 promotion：

- 只有关键词命中；
- 只有 closed state；
- 只有 issue body，没有 linked fix / patch / maintainer resolution；
- review comment 暴露风险但没有后续闭环；
- 只能证明 semantic answer 相似，不能证明 tensor / KV / logits / token identity。

## 输出

根据证据更新：

- `curated/<topic>/*.md`
- `candidates/*.csv`
- `curated/<topic>/next.md`

不要把 raw/generated/audit 材料提交到 GitHub。

## 质量门

每轮结束前确认：

- validator 通过；
- README 仍是项目概览，不承载专题细节；
- 当前专题文档只在对应 `curated/<topic>/` 下维护；
- raw/generated 目录未进入 Git；
- 新增文档为中文；
- commit message 说明本轮真实意图。

## 推荐启动语

```text
按照 Agent_loop.md 自主执行一轮 VllmWiki 迭代。先读 WIKI_IMPLEMENTATION.md、当前专题 README、next queue 和 ledger，再精读本地 targeted evidence。使用质量分析员和监工视角检查 promotion 是否过度。完成后运行 validator、确认 raw/generated 未进入 Git、提交并推送。最终说明本轮新增 insight 和下一轮队列变化。
```
