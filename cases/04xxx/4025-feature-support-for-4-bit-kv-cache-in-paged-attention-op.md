# vllm-project/vllm#4025: [Feature]: Support for 4-bit KV Cache in paged-attention op

| 字段 | 值 |
| --- | --- |
| Issue | [#4025](https://github.com/vllm-project/vllm/issues/4025) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;fp8;kernel;operator;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support for 4-bit KV Cache in paged-attention op

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Summary We would like to support the 4-bit KV cache for the decoding phase. The purpose of this feature is to reduce the GPU memory usage of the KV cache when processing long texts. By implementing a 4-bit KV cache, it would allow us to handle more and longer texts in situations where GPU memory is limited. Although VLLM currently has an implementation for fp8, utilizing int4 can further reduce GPU memory usage and allow for usage on devices that do not support the fp8 data format, such as A100. # methods Regarding the specific implementation, we propose the development of three operations: 1. Develop an operation to calculate the scale and zero point required for quantizing the KV cache and convert the existing fp16/bf16 KV cache to the int4 format. 2. Provide support for storing 4-bit KV cache in the "write_to_paged_cache" operation. 3. Enhance the paged-attention operation to support calculations with int4 KV cache: - Add optional inputs: k_scale, k_zeropoint, v_scale, and v_zeropoint to the paged-attention operation. - In the paged-attention kernel, if quantization-related parameters are detected, read the int4 KV cache stored in the G...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: PU memory is limited. Although VLLM currently has an implementation for fp8, utilizing int4 can further reduce GPU memory usage and allow for usage on devices that do not support the fp8 data format, such as A100. # met...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: Support for 4-bit KV Cache in paged-attention op feature request ### 🚀 The feature, motivation and pitch # Summary We would like to support the 4-bit KV cache for the decoding phase. The purpose of this featu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t support the fp8 data format, such as A100. # methods Regarding the specific implementation, we propose the development of three operations: 1. Develop an operation to calculate the scale and zero point required for qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ow for usage on devices that do not support the fp8 data format, such as A100. # methods Regarding the specific implementation, we propose the development of three operations: 1. Develop an operation to calculate the sc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ry usage and allow for usage on devices that do not support the fp8 data format, such as A100. # methods Regarding the specific implementation, we propose the development of three operations: 1. Develop an operation to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
