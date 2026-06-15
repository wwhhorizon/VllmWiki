# vllm-project/vllm#28836: Using os.sched_yield() releases the CPU so quickly that it causes 100% CPU utilization.

| 字段 | 值 |
| --- | --- |
| Issue | [#28836](https://github.com/vllm-project/vllm/issues/28836) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Using os.sched_yield() releases the CPU so quickly that it causes 100% CPU utilization.

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/d64429bb369d4087f9f91609e7275c4901d65aea/vllm/distributed/utils.py#L47

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: yield() releases the CPU so quickly that it causes 100% CPU utilization. stale https://github.com/vllm-project/vllm/blob/d64429bb369d4087f9f91609e7275c4901d65aea/vllm/distributed/utils.py#L47

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
