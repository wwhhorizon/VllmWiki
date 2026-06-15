# vllm-project/vllm#2396: batching and streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#2396](https://github.com/vllm-project/vllm/issues/2396) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> batching and streaming

### Issue 正文摘录

Hi! If i correctly understood code . Any type of entrypoints api with stream doesn't support batching . But LLMEngine has step() method for processing batch of requests and i can implement streaming with batch using step() or there any pitfalls here? For example how handle these multiple response streams

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pport batching . But LLMEngine has step() method for processing batch of requests and i can implement streaming with batch using step() or there any pitfalls here? For example how handle these multiple response streams

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
