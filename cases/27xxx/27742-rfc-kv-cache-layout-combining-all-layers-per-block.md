# vllm-project/vllm#27742: [RFC]: KV cache layout combining all layers per block

| 字段 | 值 |
| --- | --- |
| Issue | [#27742](https://github.com/vllm-project/vllm/issues/27742) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: KV cache layout combining all layers per block

### Issue 正文摘录

### Motivation. High-level goal: optimize the transfer time of KV data from/to the vllm KV cache by reducing per-transfer fragmentation at the vllm KV cache side. The 2 main use-cases we're considering are: 1. NixlConnector 2. OffloadingConnector So our goal is to try and optimize the time each of these connectors spend for a single transfer (GPU->CPU of the offloading connector, and GPU->host_buffer/other agent for NixlConnector). The transfer unit is a block of KV-data corresponding to some aligned (default)16-tokens out of some request. We consider the case of simple models where all layers have the same layout (i.e. not using the Hybrid Memory Allocator), although this can be explored in the future. For this case, the current layout for the vllm KV cache is (roughly) this: As you can see, the KV data that needs to be transferred is breaked down to num_layers non-contiguous segments. This does not take into account the k_or_v and num_kv_heads dimensions which may further cause extra fragmentation. In this RFC, we propose a new KV cache layout that for each block, will place all KV data for all layers contiguously: This will reduce the number of fragments to copy by a factor of...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [RFC]: KV cache layout combining all layers per block RFC;stale ### Motivation. High-level goal: optimize the transfer time of KV data from/to the vllm KV cache by reducing per-transfer fragmentation at the vllm KV cach...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d (default)16-tokens out of some request. We consider the case of simple models where all layers have the same layout (i.e. not using the Hybrid Memory Allocator), although this can be explored in the future. For this c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: configured and, the KV connector class explicitly prefers (via a new classmethod) to use the new layout. ### Feedback Period. _No response_ ### CC List. @njhill @NickLucche @robertgshaw2-redhat @heheda12345 @LucasWilkin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: KV cache layout combining all layers per block RFC;stale ### Motivation. High-level goal: optimize the transfer time of KV data from/to the vllm KV cache by reducing per-transfer fragmentation at the vllm KV cach...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: KV cache layout combining all layers per block RFC;stale ### Motivation. High-level goal: optimize the transfer time of KV data from/to the vllm KV cache by reducing per-transfer fragmentation at the vllm KV cach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
