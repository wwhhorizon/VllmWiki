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
- 现有机制分类是否自然容纳该 claim，还是存在硬塞风险？
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

## 主线收紧规则

- 每条 claim 先定角色：`主机制 / boundary / defer / 反例 / 验证风险` 五选一；不要把同一条同时写成“已知主机制”又“仍需补证”。
- 专题 `README` 主表只收稳定主机制：至少要能直接解释 `token/logprob/KV/tensor/metadata identity` 的变化，并且已有 patch、test 或 maintainer resolution 闭环。
- 专题 `README` 主表中的每个条目都必须能在 ledger 中对应到 `risk_status=stable`；如果 ledger 仍是 `include_with_boundary`、`defer` 或 `unresolved_review_risk`，优先修 ledger 判断或把主表条目降回边界。
- 专题 `next.md` 默认拆成两层：`主线核心缺口` 和 `辅助边界队列`。前者只放直接阻塞 bitwise 主机制闭环的项，例如 cache identity、adapter/version identity、prefix-cache equivalence、kernel geometry、dispatch/reduction root cause；后者才放 warmup、test soundness、support gate、selector fallback、semantic-only 旁证。
- `辅助边界队列` 不追求穷尽所有 open item；只保留仍可能改变主线判断、或下一轮需要专门防错的边界项。已经 stable 的长期 coverage 扩展默认回到机制页或 ledger，不单列占用 queue。
- 每轮优先从 `主线核心缺口` 取 1-3 项；只有当核心缺口暂时没有新增证据窗口，或某个辅助边界会直接影响主线判断时，才处理 `辅助边界队列`。
- `defer` 项若继续保留在主线队列，必须写清它到底缺的是哪一种闭环：`direct linked fix / maintainer closure / changed files / regression test / version schema / verification matrix`。如果缺口只剩一般性的“继续观察”，应降到辅助边界。
- 机制页的 `代表证据` 只放闭环证据：必须同时支撑现象、root cause、fix/workaround 和 verification。open PR、unresolved review risk、support gate、selector fallback、warmup、test soundness、semantic-only 结果，默认降到 `适用边界` 或 `仍需补证`。
- 反例和排除项单独写，不与正向主机制混排。
- 同一 PR 若同时包含稳定核心和未闭环子结论，必须拆开写；不能整条 promotion。
- `open/unmerged + unresolved review risk` 只能进入 `next.md` 或机制页边界段，不能进入专题总览主表。
- 每次 promotion 都要声明保护对象：`bit-identical / strict numeric tolerance / logprob ranking / token equality / KV identity / metadata identity / semantic only`。
- 每次 promotion 都要做分类压力检查：如果现有机制不能自然解释 root cause、fix pattern 和 verification contract，先保持 `defer` 并在 ledger 写明分类缺口；不要为了维持目录稳定把 claim 硬塞进旧机制。新增机制分类的静态条件见 [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)。

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
- 专题 README 主表没有泄漏 `boundary / defer / 反例 / 验证风险`；
- 专题 `next.md` 已区分 `主线核心缺口` 与 `辅助边界队列`，且本轮处理对象确实来自优先层；
- 机制页 `代表证据` 没有混入缺 linked fix、缺 changed files 或仍 open/unmerged 的弱证据；
- 当前专题文档只在对应 `curated/<topic>/` 下维护；
- raw/generated 目录未进入 Git；
- 新增文档为中文；
- commit message 说明本轮真实意图。

## 推荐启动语

```text
按照 Agent_loop.md 自主执行一轮 VllmWiki 迭代。先读 WIKI_IMPLEMENTATION.md、当前专题 README、next queue 和 ledger，再精读本地 targeted evidence。使用质量分析员和监工视角检查 promotion 是否过度。完成后运行 validator、确认 raw/generated 未进入 Git、提交并推送。最终说明本轮新增 insight 和下一轮队列变化。
```
