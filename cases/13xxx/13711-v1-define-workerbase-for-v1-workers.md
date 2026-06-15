# vllm-project/vllm#13711: [V1] Define WorkerBase for V1 Workers

| 字段 | 值 |
| --- | --- |
| Issue | [#13711](https://github.com/vllm-project/vllm/issues/13711) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1] Define WorkerBase for V1 Workers

### Issue 正文摘录

We need to have a base class for the workers, so that we can reduce this part of duplicate code right now i just change both of them, but we need to do the unification in the future. _Originally posted by @youkaichao in https://github.com/vllm-project/vllm/pull/13642#discussion_r1964714152_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [V1] Define WorkerBase for V1 Workers stale We need to have a base class for the workers, so that we can reduce this part of duplicate code right now i just change both of them, but we need to do the unification in the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
