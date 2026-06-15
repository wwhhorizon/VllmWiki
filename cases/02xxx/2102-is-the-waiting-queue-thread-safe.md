# vllm-project/vllm#2102: Is the waiting queue thread-safe?

| 字段 | 值 |
| --- | --- |
| Issue | [#2102](https://github.com/vllm-project/vllm/issues/2102) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is the waiting queue thread-safe?

### Issue 正文摘录

How to ensure thread safety, when `engine.add_request()` and `scheduler._schedule()` execute at the same time?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Is the waiting queue thread-safe? How to ensure thread safety, when `engine.add_request()` and `scheduler._schedule()` execute at the same time?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
