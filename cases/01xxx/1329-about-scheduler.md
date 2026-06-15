# vllm-project/vllm#1329: About scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#1329](https://github.com/vllm-project/vllm/issues/1329) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> About scheduler

### Issue 正文摘录

When providing services in stream mode, if a request is preempted in the scheduler in the form of recomputing, will it cause an error?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: About scheduler When providing services in stream mode, if a request is preempted in the scheduler in the form of recomputing, will it cause an error?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
