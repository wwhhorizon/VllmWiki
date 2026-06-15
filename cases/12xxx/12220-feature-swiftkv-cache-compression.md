# vllm-project/vllm#12220: [Feature]: SwiftKV cache compression

| 字段 | 值 |
| --- | --- |
| Issue | [#12220](https://github.com/vllm-project/vllm/issues/12220) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: SwiftKV cache compression

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, Thanks for the awesome work on VLLM. SwiftKV is a cache compression technique which reuses KV cache across layers with reduction in computation, latency and improving throughput. They already have a forked VLLM implementation at this [repo](https://github.com/Snowflake-Labs/vllm/tree/swiftkv/examples/swiftkv). I was wondering if this could be merged into VLLM. Thanks ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nique which reuses KV cache across layers with reduction in computation, latency and improving throughput. They already have a forked VLLM implementation at this [repo](https://github.com/Snowflake-Labs/vllm/tree/swiftk...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: SwiftKV cache compression feature request;stale ### 🚀 The feature, motivation and pitch Hi, Thanks for the awesome work on VLLM. SwiftKV is a cache compression technique which reuses KV cache across layers wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: SwiftKV cache compression feature request;stale ### 🚀 The feature, motivation and pitch Hi, Thanks for the awesome work on VLLM. SwiftKV is a cache compression technique which reuses KV cache across layers wi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
