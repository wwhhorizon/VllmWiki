# vllm-project/vllm#40017: [Tracking Issue]: NIXL P/D Disaggregation for Hybrid Models

| 字段 | 值 |
| --- | --- |
| Issue | [#40017](https://github.com/vllm-project/vllm/issues/40017) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking Issue]: NIXL P/D Disaggregation for Hybrid Models

### Issue 正文摘录

### Hybrid Models - [x] Nemotron/Mamba2 - [x] Homogeneous TP — #36687 (merged) - [x] Heterogeneous TP (3-read conv state transfer) — #37635 (merged) - [x] DS conv state layout — #37416 (merged) - [ ] Gemma4 — #41169 (draft, need rebase, WIP) - [x] Qwen3.5/GDN — #41869 (merged) - [x] Bugfix: mismatched kernel-per-logical blocks in HMA transfer — #42097 (merged) - [x] CI: MTP + PD spec decode acceptance test — #42677 (open) ### Prefix Caching - [ ] Mamba prefix caching mode support — #42554 (open) ### Refactor - [x] Unify Transfer Topology — #39529 (merged) - [ ] ~~Factor model-specific logics clean; good for introducing new models — #40157 (WIP)~~ - [x] New transfer design — #40731 ### Known Issues - [ ] HMA hetero TP: `_align_hybrid_block_size` produces TP-dependent block sizes — #41037 - [ ] async scheduling (issue with SSM?: https://github.com/vllm-project/vllm/issues/37285)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Tracking Issue]: NIXL P/D Disaggregation for Hybrid Models ### Hybrid Models - [x] Nemotron/Mamba2 - [x] Homogeneous TP — #36687 (merged) - [x] Heterogeneous TP (3-read conv state transfer) — #37635 (merged) - [x] DS c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d) - [x] DS conv state layout — #37416 (merged) - [ ] Gemma4 — #41169 (draft, need rebase, WIP) - [x] Qwen3.5/GDN — #41869 (merged) - [x] Bugfix: mismatched kernel-per-logical blocks in HMA transfer — #42097 (merged) -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: TP (3-read conv state transfer) — #37635 (merged) - [x] DS conv state layout — #37416 (merged) - [ ] Gemma4 — #41169 (draft, need rebase, WIP) - [x] Qwen3.5/GDN — #41869 (merged) - [x] Bugfix: mismatched kernel-per-logi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t, need rebase, WIP) - [x] Qwen3.5/GDN — #41869 (merged) - [x] Bugfix: mismatched kernel-per-logical blocks in HMA transfer — #42097 (merged) - [x] CI: MTP + PD spec decode acceptance test — #42677 (open) ### Prefix Cac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ched kernel-per-logical blocks in HMA transfer — #42097 (merged) - [x] CI: MTP + PD spec decode acceptance test — #42677 (open) ### Prefix Caching - [ ] Mamba prefix caching mode support — #42554 (open) ### Refactor - [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
