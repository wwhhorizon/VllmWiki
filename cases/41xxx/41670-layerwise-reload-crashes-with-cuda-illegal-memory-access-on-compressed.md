# vllm-project/vllm#41670: Layerwise reload crashes with CUDA illegal memory access on compressed-tensors channel-wise FP8 MoE

| 字段 | 值 |
| --- | --- |
| Issue | [#41670](https://github.com/vllm-project/vllm/issues/41670) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;moe;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;moe;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Layerwise reload crashes with CUDA illegal memory access on compressed-tensors channel-wise FP8 MoE

### Issue 正文摘录

# Layerwise reload crashes with CUDA illegal memory access on compressed-tensors channel-wise FP8 MoE ## Summary Identity `reload_weights` on a compressed-tensors channel-wise FP8 MoE model crashes with `CUDA error: an illegal memory access was encountered` when CUDA graphs are enabled. Works fine with `enforce_eager=True` or with the TRITON MoE backend. ## Root cause During layerwise reload, `_layerwise_process` calls `quant_method.process_weights_after_loading(layer)` which recreates the `moe_kernel` object (via `make_fp8_moe_kernel`). The new kernel allocates new device tensors for strides (`ab_strides1`, `ab_strides2`, etc.) and a new `moe_quant_config` referencing new scale tensors. Then `_place_kernel_tensors` restores the old weight/scale tensor data pointers (preserving CUDA graph references), but: 1. The `moe_quant_config._w1.scale` now points to the **new** (orphaned) scale tensor instead of the layer's actual parameter 2. The CUDA graph still holds pointers to the **old** kernel's stride tensors, but the old kernel object was replaced The TRITON backend doesn't hit this because `TritonExperts.__init__` doesn't allocate device tensors (strides are computed at dispatch ti...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: UDA graphs are enabled. Works fine with `enforce_eager=True` or with the TRITON MoE backend. ## Root cause During layerwise reload, `_layerwise_process` calls `quant_method.process_weights_after_loading(layer)` which re...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ashes with CUDA illegal memory access on compressed-tensors channel-wise FP8 MoE # Layerwise reload crashes with CUDA illegal memory access on compressed-tensors channel-wise FP8 MoE ## Summary Identity `reload_weights`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: (`ab_strides1`, `ab_strides2`, etc.) and a new `moe_quant_config` referencing new scale tensors. Then `_place_kernel_tensors` restores the old weight/scale tensor data pointers (preserving CUDA graph references), but: 1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: `make_fp8_moe_kernel`). The new kernel allocates new device tensors for strides (`ab_strides1`, `ab_strides2`, etc.) and a new `moe_quant_config` referencing new scale tensors. Then `_place_kernel_tensors` restores the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Identity `reload_weights` on a compressed-tensors channel-wise FP8 MoE model crashes with `CUDA error: an illegal memory access was encountered` when CUDA graphs are enabled. Works fine with `enforce_eager=True` or with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
