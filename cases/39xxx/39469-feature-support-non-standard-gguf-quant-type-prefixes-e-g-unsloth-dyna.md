# vllm-project/vllm#39469: [Feature]: Support non-standard GGUF quant type prefixes (e.g. Unsloth Dynamic UD-IQ1_S )

| 字段 | 值 |
| --- | --- |
| Issue | [#39469](https://github.com/vllm-project/vllm/issues/39469) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support non-standard GGUF quant type prefixes (e.g. Unsloth Dynamic UD-IQ1_S )

### Issue 正文摘录

### 🚀 The feature, motivation and pitch GGUF models with non-standard quant type prefixes like Unsloth Dynamic 2.0 (UD-) cannot be loaded via repo_id:quant_type format. ```bash vllm serve unsloth/Qwen3-0.6B-GGUF:UD-IQ1_S --tokenizer Qwen/Qwen3-0.6B huggingface_hub.errors.HFValidationError: Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'unsloth/Qwen3-0.6B-GGUF:UD-IQ1_S'. ``` Currently, is_remote_gguf() validates quant types against GGMLQuantizationType members and a hardcoded suffix list (_M, _S, _L, etc.). Prefixed types like `UD-IQ1_S` are rejected, and the model string falls through to HuggingFace Hub as a plain repo ID. Since quant_type is only used for glob file matching (*-{quant_type}.gguf) and not for actual quantization logic (read from GGUF binary headers), accepting non-standard prefixed names is safe. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: UD-IQ1_S ) feature request ### 🚀 The feature, motivation and pitch GGUF models with non-standard quant type prefixes like Unsloth Dynamic 2.0 (UD-) cannot be loaded via repo_id:quant_type format. ```bash vllm serve unsl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n3-0.6B huggingface_hub.errors.HFValidationError: Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'unsloth/Qwen3-0.6B-GGUF:UD-IQ1_S'. ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Support non-standard GGUF quant type prefixes (e.g. Unsloth Dynamic UD-IQ1_S ) feature request ### 🚀 The feature, motivation and pitch GGUF models with non-standard quant type prefixes like Unsloth Dynamic 2....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Support non-standard GGUF quant type prefixes (e.g. Unsloth Dynamic UD-IQ1_S ) feature request ### 🚀 The feature, motivation and pitch GGUF models with non-standard quant type prefixes like Unsloth Dynamic 2....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
