# vllm-project/vllm#11255: [Feature]: LoRA support for qwen2-vl Models

| 字段 | 值 |
| --- | --- |
| Issue | [#11255](https://github.com/vllm-project/vllm/issues/11255) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LoRA support for qwen2-vl Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I fine-tuned a qwen2-vl-7b model using llama factory, deployed it with AsyncLLMEngine, and loaded the LoRA adapter using lora_request. However, the inference results are significantly worse compared to the merged model. It would be great if we can have the support for LoRA for multimodal models as our team wants to use multiple LoRAs and merging the LoRA adapters to original model weights is not feasible for us. We are short on time for this project and as far as I can tell no other framework supports LoRA in this way. Also we need outlines for structured generation so vLLM (being the most user friendly, stable and mature framework ) is our best bet now. Can we get a timeline when will this be supported ? Also are there any workarounds possible until this feature is officially supported ? Thank you for your adaptation. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked quest...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: LoRA support for qwen2-vl Models feature request;stale ### 🚀 The feature, motivation and pitch I fine-tuned a qwen2-vl-7b model using llama factory, deployed it with AsyncLLMEngine, and loaded the LoRA adapte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: LoRA support for qwen2-vl Models feature request;stale ### 🚀 The feature, motivation and pitch I fine-tuned a qwen2-vl-7b model using llama factory, deployed it with AsyncLLMEngine, and loaded the LoRA adapte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rted ? Also are there any workarounds possible until this feature is officially supported ? Thank you for your adaptation. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
