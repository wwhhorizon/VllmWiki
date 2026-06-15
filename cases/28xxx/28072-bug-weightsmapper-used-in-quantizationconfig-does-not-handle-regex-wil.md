# vllm-project/vllm#28072: [Bug]: WeightsMapper used in QuantizationConfig does not handle regex/wildcard paths

| 字段 | 值 |
| --- | --- |
| Issue | [#28072](https://github.com/vllm-project/vllm/issues/28072) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: WeightsMapper used in QuantizationConfig does not handle regex/wildcard paths

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM model structure may be different from HuggingFace model structure so a remapping is used (WeightsMapper) when loading models. The remapping is defined in model executor logic, e.g. the [Qwen2.5 VL defines it here](https://github.com/vllm-project/vllm/blob/2d977a7a9ead3179fde9ed55d69393ef7b6cec47/vllm/model_executor/models/qwen2_5_vl.py#L1096-L1105) In quantized models, in addition to the model weights, there may be extra configs such as to describe what modules are not quantized. For example, the compressed-tensors has an "ignore" in the config as a list of modules that shall be treated as not quantized; the Nvidia ModelOpt has an "exclude_modules" also in the config as a list of modules that shall be treated as not quantized. The issue is that these configs may not be simple module path/prefix names, they may be regex (in compressed-tensors) or wildcards (in Nvidia ModelOpt). Take compressed-tensors as an example given it's also a vLLM owned project. An item in the ignore list may be a regex pattern such as "re:vision_tower.*" to exclude the whole vision encoder in a VLM. One random example quantized model that I find on HF...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: WeightsMapper used in QuantizationConfig does not handle regex/wildcard paths bug;nvidia ### Your current environment ### 🐛 Describe the bug vLLM model structure may be different from HuggingFace model structure...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: WeightsMapper used in QuantizationConfig does not handle regex/wildcard paths bug;nvidia ### Your current environment ### 🐛 Describe the bug vLLM model structure may be different from HuggingFace model structure...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: WeightsMapper used in QuantizationConfig does not handle regex/wildcard paths bug;nvidia ### Your current environment ### 🐛 Describe the bug vLLM model structure may be different from HuggingFace model structure...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: model structure may be different from HuggingFace model structure so a remapping is used (WeightsMapper) when loading models. The remapping is defined in model executor logic, e.g. the [Qwen2.5 VL defines it here](https...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ple quantized model that I find on HF: https://huggingface.co/gaunernst/gemma-3-27b-it-qat-compressed-tensors In it's config, it has the ignore list of: "ignore": [ "lm_head", "re:vision_tower.*" ], When vLLM loads the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
