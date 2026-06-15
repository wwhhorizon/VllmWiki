# vllm-project/vllm#9601: [RFC]: openai api response format

| 字段 | 值 |
| --- | --- |
| Issue | [#9601](https://github.com/vllm-project/vllm/issues/9601) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: openai api response format

### Issue 正文摘录

### Motivation. Here is example of my request using /v1/chat/completions. ``` { "id": "chat-36cf36c94fa746ffbee01440bbdcbf35", "object": "chat.completion", "created": 1729649934, "model": "", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "hello", "tool_calls": [] }, "logprobs": null, "finish_reason": "stop", "stop_reason": null } ], "usage": { "prompt_tokens": 1841, "total_tokens": 1849, "completion_tokens": 8 }, "prompt_logprobs": null, "messages": [ { "content": "hello", "role": "user" }, { "role": "assistant", "content": "xxx", "tool_calls": [] } ] } ``` I'm wondering if "messages" is from in openai api reference? ### Proposed Change. How to disable this extra part from output? ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: openai api response format RFC ### Motivation. Here is example of my request using /v1/chat/completions. ``` { "id": "chat-36cf36c94fa746ffbee01440bbdcbf35", "object": "chat.completion", "created": 1729649934, "m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: openai api response format RFC ### Motivation. Here is example of my request using /v1/chat/completions. ``` { "id": "chat-36cf36c94fa746ffbee01440bbdcbf35", "object": "chat.completion", "created": 1729649934, "model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
