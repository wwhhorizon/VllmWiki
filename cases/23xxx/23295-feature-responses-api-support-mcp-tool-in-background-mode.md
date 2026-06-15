# vllm-project/vllm#23295: [Feature][Responses API] Support MCP tool in background mode

| 字段 | 值 |
| --- | --- |
| Issue | [#23295](https://github.com/vllm-project/vllm/issues/23295) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Responses API] Support MCP tool in background mode

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We raise an error when using MCP tool server and the request is in background mode. https://github.com/vllm-project/vllm/blob/c86af22f31838ee654c856279ac5110ae3fdb2cc/vllm/entrypoints/openai/serving_responses.py#L240-L247 The reason is we need to create a MCP session for each request and close the session when the request finishes. For normal cases, it can be achieved by a `with` statement here https://github.com/vllm-project/vllm/blob/c86af22f31838ee654c856279ac5110ae3fdb2cc/vllm/entrypoints/openai/serving_responses.py#L258-L272 In background mode, we need to figure out how to close the session cleanly. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][Responses API] Support MCP tool in background mode feature request ### 🚀 The feature, motivation and pitch We raise an error when using MCP tool server and the request is in background mode. https://github.com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
