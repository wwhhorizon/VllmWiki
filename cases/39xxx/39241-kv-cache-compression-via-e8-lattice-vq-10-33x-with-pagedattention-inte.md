# vllm-project/vllm#39241: KV cache compression via E8 lattice VQ — 10-33x with PagedAttention integration

| 字段 | 值 |
| --- | --- |
| Issue | [#39241](https://github.com/vllm-project/vllm/issues/39241) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cache;quantization |
| 症状 |  |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> KV cache compression via E8 lattice VQ — 10-33x with PagedAttention integration

### Issue 正文摘录

Hey folks, I've been working on a KV cache compression library called NexusQuant and wanted to share some results that might be interesting for vLLM users dealing with long-context memory pressure. The basic idea: instead of keeping the full FP16 KV cache in memory, we score which tokens actually matter (using attention weights), evict the unimportant ones, and quantize the rest down to 2-3 bits using E8 lattice vector quantization. No training or calibration needed — it's a drop-in that works with any transformer. We just finished validating across 3 models on A100 and A10: - **Mistral-7B**: 9x compression at essentially zero quality loss (+0.00% PPL with our real attention scorer at 35% eviction). At 80% eviction: 33x at only +0.66%. - **Phi-3-mini** (head_dim=96, non-standard): 9x at +0.59%. E8 VQ handles non-power-of-2 dims via padding. - **Qwen2.5-7B**: Needs boundary layer protection (first/last 2 layers at FP16) — without it, symmetric quantization catastrophically breaks the model. With boundary: works at +7.9%. One finding that might be relevant for vLLM's architecture: **asymmetric K/V quantization matters a lot.** 3-bit keys + 2-bit values gives 6x better quality than s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: folks, I've been working on a KV cache compression library called NexusQuant and wanted to share some results that might be interesting for vLLM users dealing with long-context memory pressure. The basic idea: instead o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks with any transformer. We just finished validating across 3 models on A100 and A10: - **Mistral-7B**: 9x compression at essentially zero quality loss (+0.00% PPL with our real attention scorer at 35% eviction). At 80%...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: (`NexusQuantPagedAttention`) that stores compressed KV natively in paged blocks and decompresses on-the-fly during attention. Would love to get feedback on whether the approach makes sense with vLLM's current block mana...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n that works with any transformer. We just finished validating across 3 models on A100 and A10: - **Mistral-7B**: 9x compression at essentially zero quality loss (+0.00% PPL with our real attention scorer at 35% evictio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rboQuant+ folks found independently. I've written a vLLM PagedAttention backend (`NexusQuantPagedAttention`) that stores compressed KV natively in paged blocks and decompresses on-the-fly during attention. Would love to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
