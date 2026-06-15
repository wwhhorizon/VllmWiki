# vllm-project/vllm#6206: [Usage]: The GPU KV cache usage is still small (below 20% most of time) though I turned the enable_prefix_caching on as well as modified the block_size from 16 to 32. How could I numerally increase the KV cache for the Radix prefix caching?

| 字段 | 值 |
| --- | --- |
| Issue | [#6206](https://github.com/vllm-project/vllm/issues/6206) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The GPU KV cache usage is still small (below 20% most of time) though I turned the enable_prefix_caching on as well as modified the block_size from 16 to 32. How could I numerally increase the KV cache for the Radix prefix caching?

### Issue 正文摘录

### Current environment Rtx 4090 Ti ### Logs [2024-07-08 15:17:34] INFO 07-08 07:17:34 metrics.py:334] Avg prompt throughput: 6501.4 tokens/s, Avg generation throughput: 69.1 tokens/s, Running: 4 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 15.6%, CPU KV cache usage: 0.0%

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: The GPU KV cache usage is still small (below 20% most of time) though I turned the enable_prefix_caching on as well as modified the block_size from 16 to 32. How could I numerally increase the KV cache for the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: The GPU KV cache usage is still small (below 20% most of time) though I turned the enable_prefix_caching on as well as modified the block_size from 16 to 32. How could I numerally increase the KV cache for the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: me) though I turned the enable_prefix_caching on as well as modified the block_size from 16 to 32. How could I numerally increase the KV cache for the Radix prefix caching? usage;stale ### Current environment Rtx 4090 T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ld I numerally increase the KV cache for the Radix prefix caching? usage;stale ### Current environment Rtx 4090 Ti ### Logs [2024-07-08 15:17:34] INFO 07-08 07:17:34 metrics.py:334] Avg prompt throughput: 6501.4 tokens/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ogs [2024-07-08 15:17:34] INFO 07-08 07:17:34 metrics.py:334] Avg prompt throughput: 6501.4 tokens/s, Avg generation throughput: 69.1 tokens/s, Running: 4 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 15.6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
