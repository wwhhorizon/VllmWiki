# vllm-project/vllm#4967: [Feature]: support `stream_options` option

| 字段 | 值 |
| --- | --- |
| Issue | [#4967](https://github.com/vllm-project/vllm/issues/4967) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support `stream_options` option

### Issue 正文摘录

### 🚀 The feature, motivation and pitch According to openAI doc: https://platform.openai.com/docs/api-reference/chat/create#chat-create-stream_options. The API provide the stream_options which can get token usage info for stream request. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support `stream_options` option good first issue;feature request ### 🚀 The feature, motivation and pitch According to openAI doc: https://platform.openai.com/docs/api-reference/chat/create#chat-create-stream_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
