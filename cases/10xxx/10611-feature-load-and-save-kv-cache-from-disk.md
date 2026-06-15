# vllm-project/vllm#10611: [Feature]: load and save kv cache from disk

| 字段 | 值 |
| --- | --- |
| Issue | [#10611](https://github.com/vllm-project/vllm/issues/10611) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: load and save kv cache from disk

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For prefix cache, cache hits can significantly reduce FTT. However, kv cache occupies a large amount of storage space, and the space in CPU memory and GPU video memory is very expensive and limited, resulting in limited prefix cache and decreased hit probability. By caching the kv cache on disk/SSD, the kv-cache can be reused, greatly improving the hit rate. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Feature]: load and save kv cache from disk feature request;stale ### 🚀 The feature, motivation and pitch For prefix cache, cache hits can significantly reduce FTT. However, kv cache occupies a large amount of storage s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: load and save kv cache from disk feature request;stale ### 🚀 The feature, motivation and pitch For prefix cache, cache hits can significantly reduce FTT. However, kv cache occupies a large amount of storage s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: request;stale ### 🚀 The feature, motivation and pitch For prefix cache, cache hits can significantly reduce FTT. However, kv cache occupies a large amount of storage space, and the space in CPU memory and GPU video memo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
