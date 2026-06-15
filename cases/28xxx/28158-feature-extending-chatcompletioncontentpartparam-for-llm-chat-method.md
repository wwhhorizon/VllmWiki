# vllm-project/vllm#28158: [Feature]: extending `ChatCompletionContentPartParam` for `LLM.chat()` method

| 字段 | 值 |
| --- | --- |
| Issue | [#28158](https://github.com/vllm-project/vllm/issues/28158) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: extending `ChatCompletionContentPartParam` for `LLM.chat()` method

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello VLLM Team, thank you for you amazing work. We're currently utilizing VLLM to serve llms that support multimodal conversations through `LLM.chat()` method. I noticed that message content must adhere to a strict structure defined in `ChatCompletionContentPartParam` (for `CustomChatCompletionMessageParam` message implementation, not OpenAI or Harmony) (link to message content options [here](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L205)). Do you have any plans on extending list of accepted types and parameters to allow passing video or audio as binary file, or as torch/numpy array? This way, models can process richer forms of user input without losing performance. I can submit a PR to help with implementing the feature. ### Alternatives The possible alternative I have come up with is to save received binary to a temporary file, then send it to model via its URL (as in `file:// `). However, multiple disk read/write operations may unnecessarily overload the server and increase processing time. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: amazing work. We're currently utilizing VLLM to serve llms that support multimodal conversations through `LLM.chat()` method. I noticed that message content must adhere to a strict structure defined in `ChatCompletionCo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tending `ChatCompletionContentPartParam` for `LLM.chat()` method feature request;stale ### 🚀 The feature, motivation and pitch Hello VLLM Team, thank you for you amazing work. We're currently utilizing VLLM to serve llm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tCompletionMessageParam` message implementation, not OpenAI or Harmony) (link to message content options [here](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L205)). Do you have any plans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
