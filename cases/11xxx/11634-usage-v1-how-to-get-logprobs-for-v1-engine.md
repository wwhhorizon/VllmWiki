# vllm-project/vllm#11634: [Usage][V1]:  how to get logprobs for V1 engine?

| 字段 | 值 |
| --- | --- |
| Issue | [#11634](https://github.com/vllm-project/vllm/issues/11634) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage][V1]:  how to get logprobs for V1 engine?

### Issue 正文摘录

Getting an error when adding "logprobs":1 to the request. Does V1 not support log probs? Is there any way to obtain logprobs with the V1 engine?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: bs for V1 engine? usage Getting an error when adding "logprobs":1 to the request. Does V1 not support log probs? Is there any way to obtain logprobs with the V1 engine?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
