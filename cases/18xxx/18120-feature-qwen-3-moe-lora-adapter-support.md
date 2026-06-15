# vllm-project/vllm#18120: [Feature]: Qwen 3 MoE Lora adapter support.

| 字段 | 值 |
| --- | --- |
| Issue | [#18120](https://github.com/vllm-project/vllm/issues/18120) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen 3 MoE Lora adapter support.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #### Feature Proposal: Support for **Qwen 3 MoE LoRA (Low-Rank Adaptation)** adapter in vLLM to enable efficient fine-tuning and inference. #### Motivation: The Qwen 3 MoE model offer very good capabilities and performance. However, current vLLM do not support integration with LoRA adapters for fine-tuning and serving multiple finetuned models. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen 3 MoE Lora adapter support. feature request ### 🚀 The feature, motivation and pitch #### Feature Proposal: Support for **Qwen 3 MoE LoRA (Low-Rank Adaptation)** adapter in vLLM to enable efficient fine-t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: **Qwen 3 MoE LoRA (Low-Rank Adaptation)** adapter in vLLM to enable efficient fine-tuning and inference. #### Motivation: The Qwen 3 MoE model offer very good capabilities and performance. However, current vLLM do not s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Qwen 3 MoE Lora adapter support. feature request ### 🚀 The feature, motivation and pitch #### Feature Proposal: Support for **Qwen 3 MoE LoRA (Low-Rank Adaptation)** adapter in vLLM to enable efficient fine-t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Qwen 3 MoE Lora adapter support. feature request ### 🚀 The feature, motivation and pitch #### Feature Proposal: Support for **Qwen 3 MoE LoRA (Low-Rank Adaptation)** adapter in vLLM to enable efficient fine-t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
