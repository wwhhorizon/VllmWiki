# VllmWiki Agent Loop

状态：Codex 自主迭代协议。  
作用：记录本项目从对话中形成的目标、边界、当前结构和后续 agent 工作方式。

## 项目背景

本项目的目标是把 `vllm-project/vllm` 的 issue / PR / comment / diff 炼化成中文工程 wiki。它参考的是 KernelWiki 的“source layer -> candidate ledger -> curated wiki”组织方式，而不是复制 KDA 的 kernel 自动优化方法论。

当前已经完成第一条专题线：deterministic / bitwise。后续它只作为 `curated/bitwise/` 下的一个专题存在，不再在根目录放多个 bitwise 入口文档。

本项目强调：

- 必须阅读原始内容，而不是只看表格分析。
- 必须区分现象、根因、修复、验证契约和适用边界。
- 证据不足的 claim 留在 ledger 或 next queue，不能强行 promotion。
- GitHub 仓库保存结论层；raw / generated / audit 过程材料保留在本地。

## 我们已经做过什么

1. 调研 KDA / KernelWiki，明确要效仿的是 wiki 构建方式，而不是 KDA 后续的算子优化流程。
2. 建立 VllmWiki 的结论层、候选账本、schema/tag/alias/version claim 和 validator。
3. 聚焦 deterministic / bitwise 主线，抓取 targeted GitHub evidence，包括 issue、PR、comments、timeline、changed files、review comments 和 reviews。
4. 形成 bitwise 机制页模板：问题定义、典型触发条件、代表证据、根因机制、修复方式、验证契约、适用边界、仍需补证。
5. 深读若干高价值对象并沉淀 insight：
   - `#40179`：prefix cache deterministic split 仍要关注 resumed request、block-aligned prompt、final-token scheduler 边界。
   - `#39591`：BlockTable 的核心契约是逻辑长度之后 tail 必须为零，而不只是写入当前 slice。
   - `#42240`：AITER FP8 `splitK=0` 是绕开 CK split-K atomic reduction 的 scoped workaround，不是通用 shape 修复。
   - `#43355`：bit-identical fused RoPE + KV cache write test 有价值，但 review comments 暴露 FP8 conversion、HND/NHD layout、key/value guard 风险。
   - `#38991`：更像 shared numpy buffer view + async cross-device copy + buffer lifetime 问题，缺 linked fix PR，保持 defer。
   - `#44250`：external KV key 缺 LoRA identity 的复现强，但缺上游 fix PR 和 regression test，保持 defer。
6. 曾短暂加入过一个 Python 循环复核脚本；后来确认这偏离“让 Codex 自主迭代”的目标，已经删除。保留的是 ledger 的调度字段，因为它们服务于 agent 自主选题。

## 当前项目结构

项目级入口：

- [README.md](README.md)：项目概览。
- [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)：维护规范、证据规则、质量门。
- [loop.md](loop.md)：Codex agent 自主迭代协议。

当前专题：

- [curated/bitwise/README.md](curated/bitwise/README.md)：bitwise 专题入口。
- [curated/bitwise/evidence_synthesis.md](curated/bitwise/evidence_synthesis.md)：第一轮 targeted evidence 综合。
- [curated/bitwise/next.md](curated/bitwise/next.md)：下一轮补证队列。
- [curated/bitwise/*.md](curated/bitwise/)：机制页。
- [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv)：bitwise claim 决策账本。

仓库外 source layer：

- `E:\Vllm-Issue\all\data\raw`
- `E:\Vllm-Issue\all\data\tables`
- `E:\Vllm-Issue\all\data\targeted\bitwise`

这些 raw / generated / audit 材料不进入 GitHub 结论层。

## Agent 角色

每轮迭代至少包含三个视角。

主 agent：

- 读取规则、账本和证据。
- 精读 issue / PR / comment / diff。
- 更新机制页、ledger、next queue。
- 运行质量门并提交。

质量分析员：

- 检查新增结论是否被证据支持。
- 检查是否把 review comment 风险误写成已修复事实。
- 检查 root cause、fix、verification、boundary 是否闭环。

监工：

- 检查本轮是否真的读了原始 evidence。
- 检查是否只做结构维护而没有产生 insight。
- 检查是否误提交 raw/generated/audit 材料。
- 检查 README 是否又开始承载专题细节。

## 每轮迭代流程

1. 读取 [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)，确认当前质量门和 promotion 规则。
2. 读取本文件，确认 agent loop 的工作边界。
3. 读取当前专题入口和 ledger。bitwise 专题对应：
   - [curated/bitwise/README.md](curated/bitwise/README.md)
   - [curated/bitwise/next.md](curated/bitwise/next.md)
   - [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv)
4. 从 ledger 选择有限数量的对象，优先级为：
   - `priority=high`
   - `risk_status=unresolved_review_risk`
   - `risk_status=include_with_boundary`
   - `risk_status=defer_blocked`
5. 对每个对象精读本地 targeted evidence。必须尽量覆盖：
   - issue body
   - issue comments
   - timeline
   - PR body
   - changed files / patch
   - review comments
   - reviews
   - commits 或 linked PR 线索
6. 对每个 claim 明确判断：
   - 是否有稳定 root cause。
   - fix 是根因修复、workaround、support gate、test placement，还是仅观察性讨论。
   - exact test 覆盖了什么。
   - 没覆盖的边界是什么。
   - 是否可以进入机制页。
7. 根据证据更新：
   - `curated/<topic>/*.md`
   - `candidates/*.csv`
   - `<topic>/next.md`
8. 运行 validator，并检查 raw/generated 文件没有进入 Git。
9. 提交并推送。
10. 最终回复必须说明：
    - 本轮新增 insight。
    - 哪些 claim 被 include / defer / boundary 化。
    - 哪些文件改变。
    - 下一轮最应该读什么。

## Promotion 规则

可以下沉到机制页的结论必须同时具备：

- 有明确 source：issue、PR、comment、review comment、diff 或本地 targeted JSON。
- 有 root cause，不只是现象描述。
- 有 fix pattern 或明确说明为什么只是 workaround / support gate。
- 有 verification contract。
- 有适用边界。

不能 promotion 的情况：

- 只有关键词命中。
- 只有 issue body，没有 linked fix / changed files / maintainer resolution。
- 只有 closed state。
- 只有 semantic answer 相似，不能证明 tensor / logits / token / KV identity。
- review comment 暴露风险但没有后续 patch 或 maintainer resolution。

## Ledger 字段含义

`decision`：

- `include`：可以进入结论层，或已经进入结论层。
- `defer`：相关但证据不足，不能 promotion。
- `exclude`：不适合当前专题。

`risk_status`：

- `stable`：已经稳定进入机制页。
- `include_with_boundary`：可以 include，但必须写清边界。
- `unresolved_review_risk`：PR 有价值，但 review comments 暴露的风险尚未闭环。
- `defer_blocked`：缺 linked fix / changed files / test / maintainer resolution。

`priority`：

- `high`：下一轮优先读。
- `medium`：有价值但不阻塞主线。
- `low`：背景或 umbrella。

`review_depth`：

- `curated`：已完成机制页沉淀。
- `followup_patch`：需要查后续 patch / review resolution。
- `linked_fix_search`：需要找 linked fix。
- `umbrella_split`：需要把大 issue 拆成具体 PR / 机制。

## 质量门

每轮结束前至少确认：

- validator 通过。
- README 没有变成专题长文档。
- bitwise 专题仍只在 `curated/bitwise/` 下维护。
- `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/`、review queue、generated audit 没有进入 Git。
- 新增内容为中文；上游标题、字段名、代码符号可保留英文。
- commit 信息说明本轮真实意图。

## 推荐给 Codex 的启动语

```text
按照 loop.md 自主执行一轮 VllmWiki 迭代。聚焦当前最高优先级专题，先读 WIKI_IMPLEMENTATION.md、loop.md、专题 README、next queue 和 ledger，再精读本地 targeted evidence。使用质量分析员和监工视角检查 promotion 是否过度。完成后运行 validator、确认 raw/generated 未进入 Git、提交并推送。最终说明本轮新增 insight 和下一轮队列变化。
```
