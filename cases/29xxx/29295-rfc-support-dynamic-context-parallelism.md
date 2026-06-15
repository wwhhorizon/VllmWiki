# vllm-project/vllm#29295: [RFC]: Support Dynamic Context Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#29295](https://github.com/vllm-project/vllm/issues/29295) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;moe;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;moe |
| 症状 | slowdown |
| 根因提示 | memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Support Dynamic Context Parallelism

### Issue 正文摘录

### Motivation. The DP-attention + EP (Expert Parallelism) hybrid has become the de-facto standard for scaling MoE models.Nevertheless, production traffic frequently breaks the uniform-workload assumption across DP-attention shards: 1. Existing context-parallel strategies restrict tensor slicing to the intra-DP domain, so workload imbalance across DP-attention replicas remains unresolved. 2. When prefill and decode are colocated (PD colocation), the single-DP prefill phase serializes the attention computation and stalls all other DP workers, leaving GPUs idle and lowering overall utilization. 3. Under PD disaggregation, a surge of long prompts in the decode cluster abruptly inflates the KV-cache working set, prolonging the attention computation on the affected shard and creating a straggler that skews the load balance across DP-attention replicas. ![Image](https://github.com/user-attachments/assets/326dc749-dedc-4cd9-ac5d-376785446a73) ### Proposed Change. Our work primarily aims to realize request-level heterogeneous parallelism: for long-sequence requests, both the prefill and decode phases are handled cooperatively by multiple DP attention replicas (CP > 1), thereby mitigating...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [RFC]: Support Dynamic Context Parallelism RFC ### Motivation. The DP-attention + EP (Expert Parallelism) hybrid has become the de-facto standard for scaling MoE models.Nevertheless, production traffic frequently breaks...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: kload imbalance across DP-attention replicas remains unresolved. 2. When prefill and decode are colocated (PD colocation), the single-DP prefill phase serializes the attention computation and stalls all other DP workers...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ating more convenient aggregation and processing of attention scores and LSE vectors. To ensure the seamless applicability of CUDA Graph during the decode phase, a two-dimensional CUDA Graph capture strategy is currentl...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ion, a surge of long prompts in the decode cluster abruptly inflates the KV-cache working set, prolonging the attention computation on the affected shard and creating a straggler that skews the load balance across DP-at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ert Parallelism) hybrid has become the de-facto standard for scaling MoE models.Nevertheless, production traffic frequently breaks the uniform-workload assumption across DP-attention shards: 1. Existing context-parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
