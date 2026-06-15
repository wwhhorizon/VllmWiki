# vllm-project/vllm#14381: [Feature]: Q-Filters for KV Cache Compression

| 字段 | 值 |
| --- | --- |
| Issue | [#14381](https://github.com/vllm-project/vllm/issues/14381) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Q-Filters for KV Cache Compression

### Issue 正文摘录

The new Q-Filters paper introduces a **training-free** KV cache compression method with 32× compression and 99% accuracy on long-context tasks. It’s low-overhead and beats FP8 compression with **FlashAttention-compatibility**. Can vLLM integrate this for better long-context support and the ability to use larger models on constrained hardware? See [this discussion](https://github.com/vllm-project/vllm/discussions/14378) for more info.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Q-Filters for KV Cache Compression feature request;stale The new Q-Filters paper introduces a **training-free** KV cache compression method with 32× compression and 99% accuracy on long-context tasks. It’s lo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n long-context tasks. It’s low-overhead and beats FP8 compression with **FlashAttention-compatibility**. Can vLLM integrate this for better long-context support and the ability to use larger models on constrained hardwa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: training-free** KV cache compression method with 32× compression and 99% accuracy on long-context tasks. It’s low-overhead and beats FP8 compression with **FlashAttention-compatibility**. Can vLLM integrate this for bet...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: sion and 99% accuracy on long-context tasks. It’s low-overhead and beats FP8 compression with **FlashAttention-compatibility**. Can vLLM integrate this for better long-context support and the ability to use larger model...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Q-Filters for KV Cache Compression feature request;stale The new Q-Filters paper introduces a **training-free** KV cache compression method with 32× compression and 99% accuracy on long-context tasks. It’s lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
