# vllm-project/vllm#25815: [Performance]: PD Disaggregate deployment  performance issue

| 字段 | 值 |
| --- | --- |
| Issue | [#25815](https://github.com/vllm-project/vllm/issues/25815) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: PD Disaggregate deployment  performance issue

### Issue 正文摘录

### Issue For Prefill Decode Disaggregate case, on Decode node, if the KV cache of a request hit the full of HBM, the scheduler will trigger recalculation and put it into the waiting queue, and the KV cache will be released. This will cause prefill calculation to be performed in the next iteration on decode node, resulting in serious performance degradation. ### Solution Currently, we have 3 possible way: 1. address V0 scheduler swap queue to V1. While it maybe break the design for V1 scheduler 2. Sent the failure request back to Prefill node to regenerate kv cache. While it maybe cant solve the problem fundamentally 3. combine scheduler with cpu offload feature. While the cpu offload feature is not ready in vLLM and the scheduler logic still need update. What do you think? is there any better solution?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Performance]: PD Disaggregate deployment performance issue performance;stale ### Issue For Prefill Decode Disaggregate case, on Decode node, if the KV cache of a request hit the full of HBM, the scheduler will trigger...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ### Issue For Prefill Decode Disaggregate case, on Decode node, if the KV cache of a request hit the full of HBM, the scheduler will trigger recalculation and put it into the waiting queue, and the KV cache will be rele...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
