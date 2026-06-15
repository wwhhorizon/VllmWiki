# vllm-project/vllm#24479: [Feature]: responses API conversation feature

| 字段 | 值 |
| --- | --- |
| Issue | [#24479](https://github.com/vllm-project/vllm/issues/24479) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: responses API conversation feature

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When you call the responses API with the store feature enabled, the msg content is stored in msg_store. Currently msg_store stores content items based on response id key, but it seems that if we manage items by generating conversation id, we can maintain the same context for multiple responses API requests. - Create a conversation ID and add it to the response body - Change the key of msg_store to the conversation ID from response_id. ### Alternatives _No response_ ### Additional context https://platform.openai.com/docs/api-reference/responses/object#responses/object-conversation The response object - conversation The conversation that this response belongs to. Input items and output items from this response are automatically added to this conversation. - id: string The unique ID of the conversation. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: responses API conversation feature feature request;stale ### 🚀 The feature, motivation and pitch When you call the responses API with the store feature enabled, the msg content is stored in msg_store. Current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
