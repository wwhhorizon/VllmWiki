# vllm-project/vllm#14937: [Feature]:Slim Attention (lossless 2x reduction in KV cache size)

| 字段 | 值 |
| --- | --- |
| Issue | [#14937](https://github.com/vllm-project/vllm/issues/14937) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:Slim Attention (lossless 2x reduction in KV cache size)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Feature Description** Slim attention can reduce KV cache size by a factor of 2 without a loss of accuracy as it's lossless: https://arxiv.org/pdf/2503.05840 **Motivation** Allows you to run with larger context sizes at the same (V)RAM usage or allows you to cram the same context into less (V)RAM. Furthermore, it improves performance at long context sizes. **Possible Implementation** No response

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]:Slim Attention (lossless 2x reduction in KV cache size) feature request;stale ### 🚀 The feature, motivation and pitch **Feature Description** Slim attention can reduce KV cache size by a factor of 2 without a l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: im attention can reduce KV cache size by a factor of 2 without a loss of accuracy as it's lossless: https://arxiv.org/pdf/2503.05840 **Motivation** Allows you to run with larger context sizes at the same (V)RAM usage or...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]:Slim Attention (lossless 2x reduction in KV cache size) feature request;stale ### 🚀 The feature, motivation and pitch **Feature Description** Slim attention can reduce KV cache size by a factor of 2 without a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: im attention can reduce KV cache size by a factor of 2 without a loss of accuracy as it's lossless: https://arxiv.org/pdf/2503.05840 **Motivation** Allows you to run with larger context sizes at the same (V)RAM usage or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
