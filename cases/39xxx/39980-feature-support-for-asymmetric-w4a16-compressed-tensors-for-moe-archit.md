# vllm-project/vllm#39980: [Feature]: Support for Asymmetric W4A16 (compressed-tensors) for MoE Architectures (Qwen3.5-122B)

| 字段 | 值 |
| --- | --- |
| Issue | [#39980](https://github.com/vllm-project/vllm/issues/39980) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Asymmetric W4A16 (compressed-tensors) for MoE Architectures (Qwen3.5-122B)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I tried to infer the AWQ quantized (using llmcompressor) **Qwen3.5-122B** model using vllm, I am getting the following error, "AssertionError: Only symmetric quantization is supported for MoE" **Recipe used:** recipe = [ AWQModifier( scheme="W4A16_ASYM", targets=["Linear"], ignore=[ "lm_head", "re:.*visual.*", "re:.*linear_attn.*", "re:.*self_attn.*", ], ) ] **Inference Environment:** - **vllm version** : 0.19.0 - **Transformers version** : 5.6.0.dev0 - **Model** : Qwen3.5-122B-A10B - **Quantization Tool**: llm-compressor May I know if there is a plan to support asymmetric quantization? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: "AssertionError: Only symmetric quantization is supported for MoE" **Recipe used:** recipe = [ AWQModifier( scheme="W4A16_ASYM", targets=["Linear"], ignore=[ "lm_head", "re:.*visual.*", "re:.*linear_attn.*", "re:.*s
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support for Asymmetric W4A16 (compressed-tensors) for MoE Architectures (Qwen3.5-122B) feature request ### 🚀 The feature, motivation and pitch When I tried to infer the AWQ quantized (using llmcompressor) **Qwen3.5-122B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t ### 🚀 The feature, motivation and pitch When I tried to infer the AWQ quantized (using llmcompressor) **Qwen3.5-122B** model using vllm, I am getting the following error, "AssertionError: Only symmetric quantization i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Support for Asymmetric W4A16 (compressed-tensors) for MoE Architectures (Qwen3.5-122B) feature request ### 🚀 The feature, motivation and pitch When I tried to infer the AWQ quantized (using llmcompressor) **Q...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support for Asymmetric W4A16 (compressed-tensors) for MoE Architectures (Qwen3.5-122B) feature request ### 🚀 The feature, motivation and pitch When I tried to infer the AWQ quantized (using llmcompressor) **Q...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
