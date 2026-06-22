# Agent Loop

状态：single source of truth。
作用：规定每轮 agent 如何从证据走向 wiki 结论。

## 输入

每轮先读取：

1. [维护规则](maintenance.md)：仓库边界、证据规则、promotion 条件、质量门。
2. 当前专题入口，例如 [bitwise 专题](../curated/bitwise/README.md)。
3. 当前专题 next queue，例如 [bitwise 下一轮复核队列](../curated/bitwise/next.md)。
4. 当前专题 ledger，例如 [bitwise ledger](../candidates/bitwise_ledger.csv)。
5. 需要时读取本地 source layer，但不得把 raw evidence 全文、私有路径或隐私数据写入公开文档。

## 每轮目标

每轮选择 1-3 个 bounded item，优先级为：

1. `priority=high`
2. `risk_status=unresolved_review_risk`
3. `risk_status=include_with_boundary`
4. `risk_status=defer_blocked`

每轮必须产生一种实质变化：

- 新 insight 下沉到机制页。
- ledger 状态、阻塞原因或下一步更精确。
- `next.md` 队列被更新。
- 明确说明为什么不能 promotion。

## 精读要求

对每个对象尽量读取：

- issue body、comments、timeline。
- PR body、changed files、review comments、reviews。
- linked PR、commit、测试和 maintainer resolution。

精读后必须回答：

- 观察到的现象是什么？
- root cause 是否闭环？
- fix 是根因修复、workaround、support gate、test placement，还是尚未修复？
- exact test 覆盖了什么？
- 未覆盖的边界是什么？
- 现有机制分类是否自然容纳该 claim，还是存在硬塞风险？
- 该 claim 应该 `include`、`include_with_boundary`、`defer` 还是 `exclude`？

## 主线收敛规则

- 每条 claim 先定角色：主机制、boundary、defer、反例、验证风险五选一。
- 专题 README 只收稳定主机制；仍是 `include_with_boundary`、`defer` 或 `unresolved_review_risk` 的条目进入 `next.md` 或机制页边界段。
- `next.md` 默认拆成主线核心缺口和辅助边界队列。主线只放直接阻塞 bitwise 主机制闭环的项；warmup、test soundness、support gate、selector fallback、semantic-only 旁证进入辅助边界。
- `defer` 项若保留在主线队列，必须写清缺的是 direct linked fix、maintainer closure、changed files、regression test、version schema 还是 verification matrix。
- 同一 PR 若同时包含稳定核心和未闭环子结论，必须拆开写，不能整条 promotion。

## 输出

根据证据更新：

- `curated/<topic>/*.md`
- `curated/<topic>/next.md`
- `candidates/*.csv`
- `candidates/notes/*.md`

不要把 raw/generated/audit 材料提交到 GitHub。静态规则只改 [maintenance.md](maintenance.md)，术语只改 [glossary.md](glossary.md)。

## 结束检查

每轮结束前确认：

- validator 通过或记录失败原因。
- README 仍是入口，不承载专题细节。
- 专题 README 没有泄漏完整 defer/open PR 队列。
- 机制页代表证据没有混入缺 linked fix、缺 changed files 或仍 open/unmerged 的弱证据。
- raw/generated/private 目录未进入 Git。
- 本轮新增 insight、ledger 变化和下一轮队列变化可被人工复核。
