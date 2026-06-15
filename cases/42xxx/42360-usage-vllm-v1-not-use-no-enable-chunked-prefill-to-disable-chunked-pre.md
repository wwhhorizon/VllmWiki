# vllm-project/vllm#42360: [Usage]: vllm v1 not use `--no-enable-chunked-prefill` to disable chunked prefill.

| 字段 | 值 |
| --- | --- |
| Issue | [#42360](https://github.com/vllm-project/vllm/issues/42360) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm v1 not use `--no-enable-chunked-prefill` to disable chunked prefill.

### Issue 正文摘录

Can vllm v1 not use `--no-enable-chunked-prefill` to disable chunked prefill? I am using the ai-dynamo framework with vLLM as the backend. Is there a way to disable chunked prefill?

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: le chunked prefill? I am using the ai-dynamo framework with vLLM as the backend. Is there a way to disable chunked prefill?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm v1 not use `--no-enable-chunked-prefill` to disable chunked prefill. usage Can vllm v1 not use `--no-enable-chunked-prefill` to disable chunked prefill? I am using the ai-dynamo framework with vLLM as the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
