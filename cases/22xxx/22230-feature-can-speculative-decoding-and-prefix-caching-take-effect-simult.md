# vllm-project/vllm#22230: [Feature]: Can speculative decoding and prefix caching take effect simultaneously?

| 字段 | 值 |
| --- | --- |
| Issue | [#22230](https://github.com/vllm-project/vllm/issues/22230) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Can speculative decoding and prefix caching take effect simultaneously?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch INFO 08-05 11:33:17 [metrics.py:417] Avg prompt throughput: 1239.8 tokens/s, Avg generation throughput: 25.9 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 35.1%, CPU KV cache usage: 0.0%. INFO 08-05 11:34:35 [metrics.py:439] Speculative metrics: Draft acceptance rate: 0.675, System efficiency: 0.531, Number of speculative tokens: 4, Number of accepted tokens: 8485, Number of draft tokens: 12564, Number of emitted tokens: 8347. I don’t see the statistical information about the prefix caching hit ratio. The current version of vllm is 0.9.1. Does it not support the simultaneous activation of speculative decoding and prefix caching? Can speculative decoding and prefix caching take effect simultaneously? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Can speculative decoding and prefix caching take effect simultaneously? feature request;stale ### 🚀 The feature, motivation and pitch INFO 08-05 11:33:17 [metrics.py:417] Avg prompt throughput: 1239.8 tokens/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cs.py:439] Speculative metrics: Draft acceptance rate: 0.675, System efficiency: 0.531, Number of speculative tokens: 4, Number of accepted tokens: 8485, Number of draft tokens: 12564, Number of emitted tokens: 8347. I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e, motivation and pitch INFO 08-05 11:33:17 [metrics.py:417] Avg prompt throughput: 1239.8 tokens/s, Avg generation throughput: 25.9 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 35.1%...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t: 25.9 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 35.1%, CPU KV cache usage: 0.0%. INFO 08-05 11:34:35 [metrics.py:439] Speculative metrics: Draft acceptance rate: 0.675, System ef...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
