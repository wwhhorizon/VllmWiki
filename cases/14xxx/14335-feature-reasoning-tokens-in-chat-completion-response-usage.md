# vllm-project/vllm#14335: [Feature]: `reasoning_tokens` in Chat Completion Response `usage`

| 字段 | 值 |
| --- | --- |
| Issue | [#14335](https://github.com/vllm-project/vllm/issues/14335) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `reasoning_tokens` in Chat Completion Response `usage`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now we support reasoning outputs, but we do not show the metadata `reasoning_tokens` in Chat Completion Response `usage` ```json { "id": "chatcmpl-123456", "object": "chat.completion", "created": 1728933352, "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Hi there! How can I assist you today?", "refusal": null }, "logprobs": null, "finish_reason": "stop" } ], "usage": { "completion_tokens_details": { "reasoning_tokens": 0, } }, } ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: `reasoning_tokens` in Chat Completion Response `usage` feature request;unstale ### 🚀 The feature, motivation and pitch Now we support reasoning outputs, but we do not show the metadata `reasoning_tokens` in Ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tion and pitch Now we support reasoning outputs, but we do not show the metadata `reasoning_tokens` in Chat Completion Response `usage` ```json { "id": "chatcmpl-123456", "object": "chat.completion", "created": 17289333...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
