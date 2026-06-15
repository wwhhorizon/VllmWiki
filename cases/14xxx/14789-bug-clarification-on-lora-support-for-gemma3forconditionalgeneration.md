# vllm-project/vllm#14789: [Bug]: Clarification on LoRA Support for Gemma3ForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#14789](https://github.com/vllm-project/vllm/issues/14789) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Clarification on LoRA Support for Gemma3ForConditionalGeneration

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hey vLLM Team, I’d like to clarify the LoRA support for `Gemma3ForConditionalGeneration`. The [supported models documentation](https://docs.vllm.ai/en/latest/models/supported_models.html) states that this model supports LoRA, but after reviewing the code, it doesn’t seem to have LoRA support implemented. Could you confirm if LoRA is indeed supported for this model, or if the documentation needs an update? Thanks! ![Image](https://github.com/user-attachments/assets/5e6a0a7c-5720-4814-bf2c-5fe5eb6c0d20) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Clarification on LoRA Support for Gemma3ForConditionalGeneration bug ### Your current environment ### 🐛 Describe the bug Hey vLLM Team, I’d like to clarify the LoRA support for `Gemma3ForConditionalGeneration`. T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Clarification on LoRA Support for Gemma3ForConditionalGeneration bug ### Your current environment ### 🐛 Describe the bug Hey vLLM Team, I’d like to clarify the LoRA support for `Gemma3ForConditionalGeneration`. T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: eration`. The [supported models documentation](https://docs.vllm.ai/en/latest/models/supported_models.html) states that this model supports LoRA, but after reviewing the code, it doesn’t seem to have LoRA support implem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
