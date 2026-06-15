# vllm-project/vllm#23641: [RFC]: Frequency and Cost Aware Eviction Policy for Prefix Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#23641](https://github.com/vllm-project/vllm/issues/23641) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Frequency and Cost Aware Eviction Policy for Prefix Caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Key Idea: For a prefix cache of size `size`, and access frequency `freq`, define: Retention Benefit of a prefix (over time T): T * freq * compute_cost. where compute_cost = cost_factor * cost_func(size) cost_func = size^alpha alpha is 2 and may be smaller with implementations such as FlashAttention. We should evict a prefix if its retention benefit is smallest, that is to say it has the minimum `freq * compute_cost`. In practice, T and cost_factor take no effect because we just use the benefit for comparing, so we can ignore it. Instead of evicting the Least Recently Used prefix, with this policy, the compute cost we save is ` freq * compute_cost - another_freq * another_compute_cost `. Where another_freq and another_compute_cost is the access frequency and compute cost of prefix cache selected by LRU. To compute the retention benefit, we need the fisrt generate time and total access count for each prefix cache. We can maintain these information for each prefix cache. If this is valuable, I am happy to write further design and implement this feature. If I am missing anything, please fell free to tell me. Hope to get your feedback and having...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: unc(size) cost_func = size^alpha alpha is 2 and may be smaller with implementations such as FlashAttention. We should evict a prefix if its retention benefit is smallest, that is to say it has the minimum `freq * comput...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: FC]: Frequency and Cost Aware Eviction Policy for Prefix Caching feature request;stale ### 🚀 The feature, motivation and pitch Key Idea: For a prefix cache of size `size`, and access frequency `freq`, define: Retention...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lpha alpha is 2 and may be smaller with implementations such as FlashAttention. We should evict a prefix if its retention benefit is smallest, that is to say it has the minimum `freq * compute_cost`. In practice, T and...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: request;stale ### 🚀 The feature, motivation and pitch Key Idea: For a prefix cache of size `size`, and access frequency `freq`, define: Retention Benefit of a prefix (over time T): T * freq * compute_cost. where compute...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: me and total access count for each prefix cache. We can maintain these information for each prefix cache. If this is valuable, I am happy to write further design and implement this feature. If I am missing anything, ple...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
