# vllm-project/vllm#23222: [Feature][Responses API] Stream Function Call

| 字段 | 值 |
| --- | --- |
| Issue | [#23222](https://github.com/vllm-project/vllm/issues/23222) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Responses API] Stream Function Call

### Issue 正文摘录

### 🚀 The feature, motivation and pitch External function call invocation is not streamed right now. This functions do not have ways to handle it https://github.com/vllm-project/vllm/blob/c32e6ad1f63631fd8033f0cca3a35d5e48ccfc7f/vllm/entrypoints/openai/serving_responses.py#L781 and therefore the function call isn't streamed to users. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][Responses API] Stream Function Call feature request;stale ### 🚀 The feature, motivation and pitch External function call invocation is not streamed right now. This functions do not have ways to handle it https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
