# vllm-project/vllm#4537: [Tracking issue] [Help wanted]: Deprecate BlockManagerV1

| 字段 | 值 |
| --- | --- |
| Issue | [#4537](https://github.com/vllm-project/vllm/issues/4537) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking issue] [Help wanted]: Deprecate BlockManagerV1

### Issue 正文摘录

### Anything you want to discuss about vllm. We recently refactored the block allocation and management subsystem to improve its testability (PR https://github.com/vllm-project/vllm/pull/3492). We can replace the old implementation once the V2 is feature-complete and performant. This is a tracking issue for the remaining work. Missing items: * Prefix caching https://github.com/vllm-project/vllm/issues/3667 * CPU swapping https://github.com/vllm-project/vllm/issues/3666 * Sliding window support https://github.com/vllm-project/vllm/issues/3665 * Profile and optimize block manager V2 https://github.com/vllm-project/vllm/issues/4536

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: refactored the block allocation and management subsystem to improve its testability (PR https://github.com/vllm-project/vllm/pull/3492). We can replace the old implementation once the V2 is feature-complete and performa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Tracking issue] [Help wanted]: Deprecate BlockManagerV1 stale ### Anything you want to discuss about vllm. We recently refactored the block allocation and management subsystem to improve its testability (PR https://git...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Tracking issue] [Help wanted]: Deprecate BlockManagerV1 stale ### Anything you want to discuss about vllm. We recently refactored the block allocation and management subsystem to improve its testability (PR https://git...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
