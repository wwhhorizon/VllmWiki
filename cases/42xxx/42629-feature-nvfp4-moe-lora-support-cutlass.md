# vllm-project/vllm#42629: [Feature]: NVFP4 MoE LoRA support (Cutlass)

| 字段 | 值 |
| --- | --- |
| Issue | [#42629](https://github.com/vllm-project/vllm/issues/42629) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: NVFP4 MoE LoRA support (Cutlass)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Feature Proposal & Motivation** Can we add support for NVFP4 MoE models with LoRA adapters in vLLM. Currently, there are issues tracking MoE + LoRA for models like Qwen3.5, but there is no Lora NVFP4 quantization support. Current NVFP4 lora support only uses the Marlin kernel which does not do native FP4 computation on supported hardware. Motivation: - NVFP4 improves throughput on latest hardware. - Lora allow for efficient fine-tuned models. ### Alternatives _No response_ ### Additional context - Related vLLM issues: #40005, #38520, #40038 - Relevant model families: Qwen3.6-MoE - NVFP4 formats available via HuggingFace and quantization libraries - Happy to help with test cases, model links, and validation if needed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tch **Feature Proposal & Motivation** Can we add support for NVFP4 MoE models with LoRA adapters in vLLM. Currently, there are issues tracking MoE + LoRA for models like Qwen3.5, but there is no Lora NVFP4 quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: NVFP4 MoE LoRA support (Cutlass) feature request ### 🚀 The feature, motivation and pitch **Feature Proposal & Motivation** Can we add support for NVFP4 MoE models with LoRA adapters in vLLM. Currently, there...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: on: - NVFP4 improves throughput on latest hardware. - Lora allow for efficient fine-tuned models. ### Alternatives _No response_ ### Additional context - Related vLLM issues: #40005, #38520, #40038 - Relevant model fami...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ive FP4 computation on supported hardware. Motivation: - NVFP4 improves throughput on latest hardware. - Lora allow for efficient fine-tuned models. ### Alternatives _No response_ ### Additional context - Related vLLM i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: NVFP4 MoE LoRA support (Cutlass) feature request ### 🚀 The feature, motivation and pitch **Feature Proposal & Motivation** Can we add support for NVFP4 MoE models with LoRA adapters in vLLM. Currently, there...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
