# vllm-project/vllm#26114: [Performance]: Scheduler.update_from_output optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#26114](https://github.com/vllm-project/vllm/issues/26114) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Scheduler.update_from_output optimization

### Issue 正文摘录

### Proposal to improve performance Scheduler.update_from_output is running on critical path which blocks new batch to run and GPU stays idle during the run. Currently, the operations are quite small and fragmented. We will explore more to see how we could further bring down the cost. ## Action Items / Potential Opportunities - [TODO] Benchmark to measure overhead - [TODO] Better breakdown analysis for output processing - BlockHasher - [WIP] Early stop in request_block_hasher (https://github.com/vllm-project/vllm/pull/26112) - [TODO] Direct block_hash append instead of creating new list in request_block_hasher - [TODO] For spec decoding, kick off request_block_hasher only once - [TODO] Update finished_reason along with status update (while currently finished_reason is derived per read) - [TODO] Maybe Fuse append_output_token_ids and check_stop ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentat...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Scheduler.update_from_output optimization performance;stale ### Proposal to improve performance Scheduler.update_from_output is running on critical path which blocks new batch to run and GPU stays idle du...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: down the cost. ## Action Items / Potential Opportunities - [TODO] Benchmark to measure overhead - [TODO] Better breakdown analysis for output processing - BlockHasher - [WIP] Early stop in request_block_hasher (https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: and GPU stays idle during the run. Currently, the operations are quite small and fragmented. We will explore more to see how we could further bring down the cost. ## Action Items / Potential Opportunities - [TODO] Bench...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: formance Scheduler.update_from_output is running on critical path which blocks new batch to run and GPU stays idle during the run. Currently, the operations are quite small and fragmented. We will explore more to see ho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
