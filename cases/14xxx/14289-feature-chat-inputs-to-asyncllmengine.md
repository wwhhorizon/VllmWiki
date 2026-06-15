# vllm-project/vllm#14289: [Feature]: Chat inputs to AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#14289](https://github.com/vllm-project/vllm/issues/14289) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Chat inputs to AsyncLLMEngine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, only the `LLM` class meant for offline inference supports the `chat` [method](https://docs.vllm.ai/en/latest/models/generative_models.html#llm-chat). Are there any plans to implement a similar method for `AsyncLLMEngine`, besides the existing `generate`? Alternatively, is there any work on extending the `PromptType` acceptable by `generate` to include more prompt variants, such as chat conversations? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Chat inputs to AsyncLLMEngine feature request;stale ### 🚀 The feature, motivation and pitch Currently, only the `LLM` class meant for offline inference supports the `chat` [method](https://docs.vllm.ai/en/lat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ne inference supports the `chat` [method](https://docs.vllm.ai/en/latest/models/generative_models.html#llm-chat). Are there any plans to implement a similar method for `AsyncLLMEngine`, besides the existing `generate`?...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: offline inference supports the `chat` [method](https://docs.vllm.ai/en/latest/models/generative_models.html#llm-chat). Are there any plans to implement a similar method for `AsyncLLMEngine`, besides the existing `genera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
