# vllm-project/vllm#2901: Controlling max queue time

| 字段 | 值 |
| --- | --- |
| Issue | [#2901](https://github.com/vllm-project/vllm/issues/2901) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Controlling max queue time

### Issue 正文摘录

Is there a way of controlling when vLLM will reject a request because the queue is too long vs let the request enter the queue?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Controlling max queue time stale Is there a way of controlling when vLLM will reject a request because the queue is too long vs let the request enter the queue?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
