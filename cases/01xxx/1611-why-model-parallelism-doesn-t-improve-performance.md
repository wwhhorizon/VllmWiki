# vllm-project/vllm#1611: Why model parallelism doesn't improve performance

| 字段 | 值 |
| --- | --- |
| Issue | [#1611](https://github.com/vllm-project/vllm/issues/1611) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Why model parallelism doesn't improve performance

### Issue 正文摘录

If I parallelize an OPT-13b model into two A100 GPUs, the throughput of the serving is worse than using a single A100, eventhough you are doubling the number of GPU blocks available for the KV cache.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Why model parallelism doesn't improve performance If I parallelize an OPT-13b model into two A100 GPUs, the throughput of the serving is worse than using a single A100, eventhough you are doubling the number of GPU bloc...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: , eventhough you are doubling the number of GPU blocks available for the KV cache. performance attention_kv_cache;model_support cache slowdown If I parallelize an OPT-13b model into two A100 GPUs, the throughput of the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: than using a single A100, eventhough you are doubling the number of GPU blocks available for the KV cache. performance attention_kv_cache;model_support cache slowdown If I parallelize an OPT-13b model into two A100 GPUs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Why model parallelism doesn't improve performance If I parallelize an OPT-13b model into two A100 GPUs, the throughput of the serving is worse than using a single A100, eventhough you are doubling the number of GPU bloc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ve performance If I parallelize an OPT-13b model into two A100 GPUs, the throughput of the serving is worse than using a single A100, eventhough you are doubling the number of GPU blocks available for the KV cache. perf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
