# vllm-project/vllm#42734: [Bug]: UD-IQ2_M not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#42734](https://github.com/vllm-project/vllm/issues/42734) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: UD-IQ2_M not supported

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Error: ``` Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'unsloth/Qwen3.6-35B-A3B-GGUF:UD-IQ2_M' ``` Problem: Recent PR https://github.com/vllm-project/vllm/pull/39471 did not account that **is_valid_gguf_quant_type** should return true for UD-IQ2_M. It isn't one of the listed GGMLQuantizationTypes in gguf library's constants.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: environment ### 🐛 Describe the bug Error: ``` Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'unsloth/Qwen3.6-35B-A3B-GGUF:UD-IQ2_M' ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ub.com/vllm-project/vllm/pull/39471 did not account that **is_valid_gguf_quant_type** should return true for UD-IQ2_M. It isn't one of the listed GGMLQuantizationTypes in gguf library's constants.py ### Before submittin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ame cannot start or end with '-' or '.' and the maximum length is 96: 'unsloth/Qwen3.6-35B-A3B-GGUF:UD-IQ2_M' ``` Problem: Recent PR https://github.com/vllm-project/vllm/pull/39471 did not account that **is_valid_gguf_q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nnot start or end with '-' or '.' and the maximum length is 96: 'unsloth/Qwen3.6-35B-A3B-GGUF:UD-IQ2_M' ``` Problem: Recent PR https://github.com/vllm-project/vllm/pull/39471 did not account that **is_valid_gguf_quant_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
