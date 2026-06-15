# vllm-project/vllm#33314: [RFC] [Feature]: Apply RFC #8913 to Quantized Linear Methods (Decouple Kernels from Checkpoint Layout)

| 字段 | 值 |
| --- | --- |
| Issue | [#33314](https://github.com/vllm-project/vllm/issues/33314) |
| 状态 | open |
| 标签 | feature request;RFC |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] [Feature]: Apply RFC #8913 to Quantized Linear Methods (Decouple Kernels from Checkpoint Layout)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Context RFC #8913 proposes decoupling checkpoint formats from kernel integrations by standardizing how weights are represented at runtime and allowing kernel-specific repacking/preprocessing as a separate concern. This RFC scopes that same idea specifically to quantized linear methods (e.g., GPTQ/AWQ/FP8/FP4 linear integrations) where kernel selection is currently constrained by checkpoint packing/layout assumptions.​ ### Problem Many quantized linear “methods” implicitly encode checkpoint layout requirements in their weight-loading paths (often via specialized create_weights implementations), so the checkpoint format effectively selects the kernel. This causes: - Duplicated create_weights logic across methods that differ only by kernel/backend. - Kernel integrations that are hard to mix-and-match with alternate checkpoint layouts. - Layout/packing details leaking into create_weights rather than `process_weights_after_loading` concern. - The Kernel abstraction(#27814, #11785) is already largely format-agnostic in spirit: kernel selection is based on a kernel/layer configuration. However, weight-loading still bakes in checkpoint packing/l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [RFC] [Feature]: Apply RFC #8913 to Quantized Linear Methods (Decouple Kernels from Checkpoint Layout) feature request;RFC ### 🚀 The feature, motivation and pitch ### Context RFC #8913 proposes decoupling checkpoint for...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: RFC #8913 to Quantized Linear Methods (Decouple Kernels from Checkpoint Layout) feature request;RFC ### 🚀 The feature, motivation and pitch ### Context RFC #8913 proposes decoupling checkpoint formats from kernel integr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tivation and pitch ### Context RFC #8913 proposes decoupling checkpoint formats from kernel integrations by standardizing how weights are represented at runtime and allowing kernel-specific repacking/preprocessing as a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uplicated create_weights logic across methods that differ only by kernel/backend. - Kernel integrations that are hard to mix-and-match with alternate checkpoint layouts. - Layout/packing details leaking into create_weig...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ndardizing how weights are represented at runtime and allowing kernel-specific repacking/preprocessing as a separate concern. This RFC scopes that same idea specifically to quantized linear methods (e.g., GPTQ/AWQ/FP8/F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
