# vllm-project/vllm#37319: [RFC]: Extensible Per-Token Quantized KV Cache Scale Infrastructure

| 字段 | 值 |
| --- | --- |
| Issue | [#37319](https://github.com/vllm-project/vllm/issues/37319) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Extensible Per-Token Quantized KV Cache Scale Infrastructure

### Issue 正文摘录

VLLM already supports FP8 quantization for the KV cache. This path reduces the memory footprint and allows keeping more tokens in cache, but it relies on per-tensor scales that either come from the checkpoint or are calculated during calibration. The quality cost is quite bounded and easy to reason about because the scheme already exists and its assumptions are well known. The INT8 per-token proposal shifts this balance. K and V still occupy one byte per element, just like in FP8, but instead of reusing a global per-tensor scale, a dynamic per-token scale is computed at the time of writing into the cache. This improves independence from the checkpoint, but also introduces an extra cost: besides the quantized tensor, auxiliary float32 buffers must be allocated to store these scales. Therefore, it is not enough to "discover" these buffers at runtime; they must be included from the beginning in profiling and memory planning. ## Motivation The main idea is to offer a more memory-efficient KV cache option that requires no additional configuration. Compared to storing the cache in bf16 or fp16, K and V take up approximately half the space. And unlike FP8, there is no need for the model...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [RFC]: Extensible Per-Token Quantized KV Cache Scale Infrastructure RFC VLLM already supports FP8 quantization for the KV cache. This path reduces the memory footprint and allows keeping more tokens in cache, but it rel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: bout a semantic mode, not string prefixes. `get_kv_quant_mode()` handles mapping the text dtype to this enum, checking suffixes before prefixes to avoid future ambiguities. From there, the legacy `is_quantized_kv_cache(...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: cache_dtype="int8_per_token"` and the rest should be resolved within the backend. This zero-config behavior is a significant part of the proposal's value, not just an implementation detail. ## Design ### 1. Enum dispatc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ffer a more memory-efficient KV cache option that requires no additional configuration. Compared to storing the cache in bf16 or fp16, K and V take up approximately half the space. And unlike FP8, there is no need for t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: FP4` could request block-scales and global-scales without requiring core architectural rewrites. ## Memory and Scope ### Realistic memory accounting Once explicit auxiliary buffers exist, they also need to be properly a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
