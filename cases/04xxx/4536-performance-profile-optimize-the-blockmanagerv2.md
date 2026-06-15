# vllm-project/vllm#4536: [Performance]: Profile & optimize the BlockManagerV2

| 字段 | 值 |
| --- | --- |
| Issue | [#4536](https://github.com/vllm-project/vllm/issues/4536) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Profile & optimize the BlockManagerV2

### Issue 正文摘录

### Proposal to improve performance We've recently rewritten the block management subsystem for better testability. We need to profile it under real load to make sure it is performant enough to replace the block manager V1, and fix any issues. We should do this once the block manager v2 is feature complete (still missing a few items). Known issue: * Prefix caching `num_total_tokens` is O(N^2) instead of O(N) (see https://github.com/vllm-project/vllm/pull/4142#discussion_r1585245813)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: Profile & optimize the BlockManagerV2 performance;stale ### Proposal to improve performance We've recently rewritten the block management subsystem for better testability. We need to profile it under real...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Performance]: Profile & optimize the BlockManagerV2 performance;stale ### Proposal to improve performance We've recently rewritten the block management subsystem for better testability. We need to profile it under real...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Profile & optimize the BlockManagerV2 performance;stale ### Proposal to improve performance We've recently rewritten the block management subsystem for better testability. We need to profile it under real...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
