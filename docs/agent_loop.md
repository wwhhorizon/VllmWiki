# Agent Loop

状态：single source of truth。
作用：规定每轮 agent 如何从证据走向 wiki 结论，以及多角色协作与质量闸门。

## 角色定义

每轮迭代涉及四个 subagent 角色（可由单个模型顺序扮演，也可由专用模型分工）：

- **planner**：选题与优先级排序。从 ledger / next.md 中选出 1-3 个 bounded item，按 priority 和 risk_status 排序。
- **researcher**：精读上游 issue / PR。读取 body、comments、timeline、changed files、review comments、tests，回答精读七问。
- **writer**：写入机制页或 candidate note。确保每条 stable evidence bullet 包含 upstream id / status / claim level / direct evidence / boundary 五字段。
- **verifier**：judge gate。对本轮产出执行下面定义的七问审查，通过后方可合入。

## 输入

每轮先读取：

1. [维护规则](maintenance.md)：仓库边界、证据规则、promotion 条件、质量门。
2. 当前专题入口，例如 [bitwise 专题](../curated/bitwise/README.md)。
3. 当前专题 next queue，例如 [bitwise 下一轮复核队列](../curated/bitwise/next.md)。
4. 当前专题 ledger，例如 [bitwise ledger](../candidates/bitwise_ledger.csv)。
5. 环境快照：vLLM commit、PyTorch version、CUDA version、GPU arch、attention backend、compile/enforce_eager、cudagraph mode、quant dtype、CUBLAS_WORKSPACE_CONFIG、torch.use_deterministic_algorithms、seed 策略。环境差异可能导致跨版本/跨平台结论偏移，PyTorch 和 cuBLAS 官方均不保证跨平台 bitwise reproducibility。

## 每轮目标

每轮选择 1-3 个 bounded item，优先级为：

1. ` priority=high `
2. ` isk_status=unresolved_review_risk `
3. ` isk_status=include_with_boundary `
4. ` isk_status=defer_blocked `

每轮必须产生一种实质变化：

- 新 insight 下沉到机制页。
- ledger 状态、阻塞原因或下一步更精确。
- ` 
ext.md ` 队列被更新。
- 明确说明为什么不能 promotion。

## 精读要求

对每个对象尽量读取：

- issue body、comments、timeline。
- PR body、changed files、review comments、reviews。
- linked PR、commit、测试和 maintainer resolution。

精读后必须回答（七问）：

1. 观察到的现象是什么？
2. root cause 是否闭环？
3. fix 是根因修复、workaround、support gate、test placement，还是尚未修复？
4. exact test 覆盖了什么？
5. 未覆盖的边界是什么？
6. 现有机制分类是否自然容纳该 claim，还是存在硬塞风险？
7. 该 claim 应该 ` include `、` include_with_boundary `、` defer ` 还是 ` exclude `？

## Judge Gate（verifier 审查）

每轮 writer 产出后，verifier 必须用以下七问执行 gate：

1. 这条 claim 是 stable、boundary、defer，还是 counterexample？
2. 它是否拥有两类以上异质证据？
3. 它是否真的属于当前机制页，而不是另一个机制页或 next.md？
4. 它是否把 open PR / review risk 误写成 landed lesson？
5. 它是否把 issue body 推断成 maintainer 定性？
6. 它的 verification contract 是否写明？
7. 它的 boundary 是否足够限制外推？

任一问不通过则退回 writer 修改，全部通过方可合入主分支。

## Gold Eval 与 Shadow Run

**Gold eval**：维护一组已知正确答案的 gold cases（在 ` data/gold_cases.json ` 中），每条 gold case 包含 upstream id、预期 classification、预期 mechanism 和预期 boundary。每次模型变更或 agent loop 逻辑变更后，运行 gold eval 验证决策一致性。

**Shadow run**：当 primary model 升级时，同一轮迭代由 shadow model 独立运行 researcher + writer，verifier 对比两者的 decision output。若 decision_diff_count 超过阈值，触发人工复核后合入。

**迭代日志**：每轮迭代记录结构化日志到 ` udit/ `（不进 Git），包含 iteration_id、repo_sha、topic、primary_model、shadow_model、upstream_items、gold_eval_version、decision_diff_count、judge_result、files_written。

## 主线收敛规则

- 每条 claim 先定角色：主机制、boundary、defer、反例、验证风险五选一。
- 专题 README 只收稳定主机制；仍是 ` include_with_boundary `、` defer ` 或 ` unresolved_review_risk ` 的条目进入 ` 
ext.md ` 或机制页边界段。
- ` 
ext.md ` 默认拆成主线核心缺口和辅助边界队列。主线只放直接阻塞 bitwise 主机制闭环的项；warmup、test soundness、support gate、selector fallback、semantic-only 旁证进入辅助边界。
- ` defer ` 项若保留在主线队列，必须写清缺的是 direct linked fix、maintainer closure、changed files、regression test、version schema 还是 verification matrix。
- 同一 PR 若同时包含稳定核心和未闭环子结论，必须拆开写，不能整条 promotion。

## 写入规则（硬约束）

- 稳定证据区禁止出现 open PR / defer / include_with_boundary；此类对象仅可进入"边界与反例"段或 next.md。
- 每条稳定证据 bullet 必须包含五个字段：upstream id、upstream status、claim level、direct evidence、oundary。
- comment-level claim 无 comment permalink 的，不得进入 stable page；comment clue 最多写入 appendix。
- candidate note 的 Why not promoted + Evidence summary 合计不超过 350 汉字；note 职责是"导航和状态"，不是"替代机制页"。

## 输出

根据证据更新：

- ` curated/<topic>/*.md `
- ` curated/<topic>/next.md `
- ` candidates/*.csv `
- ` candidates/notes/*.md `

不要把 raw/generated/audit 材料提交到 GitHub。静态规则只改 [maintenance.md](maintenance.md)，术语只改 [glossary.md](glossary.md)。

## 结束检查

每轮结束前确认：

- validator 通过或记录失败原因。
- README 仍是入口，不承载专题细节。
- 专题 README 没有泄漏完整 defer/open PR 队列。
- 机制页代表证据没有混入缺 linked fix、缺 changed files 或仍 open/unmerged 的弱证据。
- raw/generated/private 目录未进入 Git。
- 本轮新增 insight、ledger 变化和下一轮队列变化可被人工复核。
- gold eval 通过且 shadow run（如适用）无超标 diff。
