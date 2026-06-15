# vllm-project/vllm#23161: [RFC]: Support Layer-Specific KV-Cache Dtype & Layout in V1 Engine for Hybrid Models

| 字段 | 值 |
| --- | --- |
| Issue | [#23161](https://github.com/vllm-project/vllm/issues/23161) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Layer-Specific KV-Cache Dtype & Layout in V1 Engine for Hybrid Models

### Issue 正文摘录

### Motivation. ### Problem Statement Currently, V1’s ConstantCacheManager enforces: Uniform KV-cache dtype across all layers (e.g., cannot mix BF16 for Linear attention’s shortconv + FP32 for recurrent-cache). FlashInfer-only layout ([num_blocks, 2, ...]), which breaks MLA (block_size=64) unless FLASHINFER backend is used. This prevents hybrid models with layer-specific requirements from running efficiently. ### Motivation We are developing an internal HybridModel that combines a custom Linear-attention variant (with a short convolution path) with Multi-head Latent Attention (MLA). And we successfully integrate our model to v0 engine. After merging Minimax’s V1-engine updates from last week, we discovered that the current cache manager is too rigid for this topology. Specifically: We need BF16 KV-cache for the Linear-attention layers (driven by a short-convolution kernel), but FP32 KV-cache for the recurrent / MLA layers. The V1 engine presently allocates a single, uniform dtype for the entire model, forcing us to over-allocate memory when we default everything to FP32. The engine also hard-codes the FlashInfer layout [num_blocks, 2, …] and the same block size for every layer. As...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: t mix BF16 for Linear attention’s shortconv + FP32 for recurrent-cache). FlashInfer-only layout ([num_blocks, 2, ...]), which breaks MLA (block_size=64) unless FLASHINFER backend is used. This prevents hybrid models wit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [RFC]: Support Layer-Specific KV-Cache Dtype & Layout in V1 Engine for Hybrid Models RFC ### Motivation. ### Problem Statement Currently, V1’s ConstantCacheManager enforces: Uniform KV-cache dtype across all layers (e.g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [RFC]: Support Layer-Specific KV-Cache Dtype & Layout in V1 Engine for Hybrid Models RFC ### Motivation. ### Problem Statement Currently, V1’s ConstantCacheManager enforces: Uniform KV-cache dtype across all layers (e.g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ift the single-block-size requirement so that different attention mechanisms can select page sizes that match their kernels (e.g., 64 for MLA vs. 1008 for Linear). Avoid mandating FLASHINFER for all layers when only a s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: Support Layer-Specific KV-Cache Dtype & Layout in V1 Engine for Hybrid Models RFC ### Motivation. ### Problem Statement Currently, V1’s ConstantCacheManager enforces: Uniform KV-cache dtype across all layers (e.g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
