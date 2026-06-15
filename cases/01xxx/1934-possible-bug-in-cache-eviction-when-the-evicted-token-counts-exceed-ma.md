# vllm-project/vllm#1934: Possible bug in cache eviction when the evicted token counts exceed `max_num_batched_tokens`

| 字段 | 值 |
| --- | --- |
| Issue | [#1934](https://github.com/vllm-project/vllm/issues/1934) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Possible bug in cache eviction when the evicted token counts exceed `max_num_batched_tokens`

### Issue 正文摘录

When a request is evicted, it is put into the waiting queue: https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L377 Note that the total counts of the evicted tokens is the sum of prompt and intermediate decode tokens. However, at https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L140-L154, the waiting queue is essentially treated as a prompt queue. So if a request whose total token counts is > `max_num_batched_tokens` is evicted and trying to be rescheduled, the condition https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L146 becomes true and such request is immediately canceled.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ion when the evicted token counts exceed `max_num_batched_tokens` When a request is evicted, it is put into the waiting queue: https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L377 Note that the tot...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
