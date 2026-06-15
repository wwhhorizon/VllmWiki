# vllm-project/vllm#21746: [Feature]: Add LoRA adapter support for Gemma3nForConditionalGeneration models

| 字段 | 值 |
| --- | --- |
| Issue | [#21746](https://github.com/vllm-project/vllm/issues/21746) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add LoRA adapter support for Gemma3nForConditionalGeneration models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM currently throws the following error when attempting to use LoRA adapters with Gemma3n models: ```text ERROR: ValueError: Gemma3nForConditionalGeneration does not support LoRA yet. ``` **Minimum Viable Implementation:** For now, LoRA support could be implemented for text-only inference streams, even if multimodal components (vision/audio) are being added or don't initially support LoRA. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Add LoRA adapter support for Gemma3nForConditionalGeneration models feature request;stale ### 🚀 The feature, motivation and pitch vLLM currently throws the following error when attempting to use LoRA adapters...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: LoRA adapter support for Gemma3nForConditionalGeneration models feature request;stale ### 🚀 The feature, motivation and pitch vLLM currently throws the following error when attempting to use LoRA adapters with Gemma3n m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Add LoRA adapter support for Gemma3nForConditionalGeneration models feature request;stale ### 🚀 The feature, motivation and pitch vLLM currently throws the following error when attempting to use LoRA adapters...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
