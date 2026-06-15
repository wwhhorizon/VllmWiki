# vllm-project/vllm#2556: GPU utilization decrease during long-term running

| 字段 | 值 |
| --- | --- |
| Issue | [#2556](https://github.com/vllm-project/vllm/issues/2556) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU utilization decrease during long-term running

### Issue 正文摘录

When using vLLM for offline batch prediction, I found a significant decrease in GPU utilization during long-term running. As shown in the graph below, the utilization rate is around 60-70% at 00:00, but it drops to 50-60% by 15:00. What could be the reason for this? Is there a plan to fix it? Currently, I suspect that there are too many GPU memory fragments, and I am trying to alleviate this problem by periodically restarting the system.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: there a plan to fix it? Currently, I suspect that there are too many GPU memory fragments, and I am trying to alleviate this problem by periodically restarting the system.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: GPU utilization decrease during long-term running stale When using vLLM for offline batch prediction, I found a significant decrease in GPU utilization during long-term running. As shown in the graph below, the utilizat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
