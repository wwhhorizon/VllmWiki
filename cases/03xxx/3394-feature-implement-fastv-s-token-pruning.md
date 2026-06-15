# vllm-project/vllm#3394: [Feature] Implement FastV's Token Pruning

| 字段 | 值 |
| --- | --- |
| Issue | [#3394](https://github.com/vllm-project/vllm/issues/3394) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Implement FastV's Token Pruning

### Issue 正文摘录

Hi, I hope to merge the [FastV](https://github.com/pkunlp-icler/FastV) inference acceleration method with vLLM. It requires removing some tokens after certain layer to reach inference acceleation and lower GPU usage. Do you have any idea on how to implement this? Many thanks,

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature] Implement FastV's Token Pruning stale Hi, I hope to merge the [FastV](https://github.com/pkunlp-icler/FastV) inference acceleration method with vLLM. It requires removing some tokens after certain layer to rea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
