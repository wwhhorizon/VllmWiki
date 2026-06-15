# vllm-project/vllm#3058: Is there a mecanism of priorities when sending a new request 

| 字段 | 值 |
| --- | --- |
| Issue | [#3058](https://github.com/vllm-project/vllm/issues/3058) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there a mecanism of priorities when sending a new request 

### Issue 正文摘录

The goal would be to get faster answers for some requests than others, it could be handled by a priority queue feeding the engine, but I could not find such a thing.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Is there a mecanism of priorities when sending a new request stale The goal would be to get faster answers for some requests than others, it could be handled by a priority queue feeding the engine, but I could not find...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Is there a mecanism of priorities when sending a new request stale The goal would be to get faster answers for some requests than others, it could be handled by a priority queue feeding the engine, but I could not find...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
