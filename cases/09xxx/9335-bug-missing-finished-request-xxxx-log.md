# vllm-project/vllm#9335: [Bug]: missing 'Finished request xxxx' log

| 字段 | 值 |
| --- | --- |
| Issue | [#9335](https://github.com/vllm-project/vllm/issues/9335) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: missing 'Finished request xxxx' log

### Issue 正文摘录

'Finished request xxxx' log is missing in multiprocessing engine.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: missing 'Finished request xxxx' log bug;stale 'Finished request xxxx' log is missing in multiprocessing engine.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
