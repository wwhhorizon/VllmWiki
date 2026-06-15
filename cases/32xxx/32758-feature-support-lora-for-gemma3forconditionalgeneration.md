# vllm-project/vllm#32758: [Feature]: support lora for Gemma3ForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#32758](https://github.com/vllm-project/vllm/issues/32758) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support lora for Gemma3ForConditionalGeneration

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Although the current VLLM version shows that it supports LoRa of Gemma3ForConditionalGeneration, it can only load the language model part and cannot support the weight loading of the Vision Tower etc. ### Alternatives Based on the solutions for most models in this link(https://github.com/vllm-project/vllm/issues/31479), I think the following two functions can be added to support LoRa of Gemma3ForConditionalGeneration. ``` def get_num_mm_connector_tokens(self, num_vision_tokens: int) -> int: return num_vision_tokens def get_num_mm_encoder_tokens(self, num_image_tokens: int) -> int: return num_image_tokens*16 ``` Adding these two parameters allows me to fully load the gemma-3-12b LoRa adapter locally. But perhaps they should have a more scientific and logical calculation method, so hopefully someone can help improve it. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: quest ### 🚀 The feature, motivation and pitch Although the current VLLM version shows that it supports LoRa of Gemma3ForConditionalGeneration, it can only load the language model part and cannot support the weight loadi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: support lora for Gemma3ForConditionalGeneration help wanted;feature request ### 🚀 The feature, motivation and pitch Although the current VLLM version shows that it supports LoRa of Gemma3ForConditionalGenerat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: support lora for Gemma3ForConditionalGeneration help wanted;feature request ### 🚀 The feature, motivation and pitch Although the current VLLM version shows that it supports LoRa of Gemma3ForConditionalGenerat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re]: support lora for Gemma3ForConditionalGeneration help wanted;feature request ### 🚀 The feature, motivation and pitch Although the current VLLM version shows that it supports LoRa of Gemma3ForConditionalGeneration, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
