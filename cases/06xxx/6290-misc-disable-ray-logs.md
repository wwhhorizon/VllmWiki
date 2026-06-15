# vllm-project/vllm#6290: [Misc]: Disable ray logs

| 字段 | 值 |
| --- | --- |
| Issue | [#6290](https://github.com/vllm-project/vllm/issues/6290) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Disable ray logs

### Issue 正文摘录

### How to disable ray logs files generate. The vllm service running in the k8s cluster that has ephemal-stroage limitation, `Evict` event occur on the vllm's pod due to the large log files in the `/tmp` directory. How to disable to generate those logs files?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Disable ray logs stale ### How to disable ray logs files generate. The vllm service running in the k8s cluster that has ephemal-stroage limitation, `Evict` event occur on the vllm's pod due to the large log file...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
