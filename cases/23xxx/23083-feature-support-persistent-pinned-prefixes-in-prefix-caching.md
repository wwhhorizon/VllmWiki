# vllm-project/vllm#23083: [Feature]: Support Persistent/Pinned Prefixes in Prefix Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#23083](https://github.com/vllm-project/vllm/issues/23083) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Persistent/Pinned Prefixes in Prefix Caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm writing to propose a feature enhancement for the Prefix Caching mechanism. Currently, vllm uses an LRU (Least Recently Used) eviction policy for prefix caching: when the cache reaches its capacity limit, the least recently accessed prefixes are evicted to make space for new ones. This works well for general use cases, but there are scenarios where users might need **specific critical prefixes to remain persistently in memory (or VRAM) and never be evicted**, even if they are not the most recently used. ### Use Case Motivation: In production environments, certain prefixes (e.g., system prompts, common instruction templates, or frequently reused context chunks) are accessed repeatedly across many inference requests. Evicting these prefixes can lead to unnecessary recomputation when they are needed again, which undermines the performance benefits of caching. Allowing users to "pin" such critical prefixes would ensure they remain in cache indefinitely, optimizing latency for high-priority workloads. ### Proposed Enhancement: Add a mechanism to mark specific prefixes as "pinned" (non-evictable). Pinned prefixes would: 1. Be prioritized for re...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m writing to propose a feature enhancement for the Prefix Caching mechanism. Currently, vllm uses an LRU (Least Recently Used) eviction policy for prefix caching: when the cache reaches its capacity limit, the least rec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Persistent/Pinned Prefixes in Prefix Caching feature request;stale ### 🚀 The feature, motivation and pitch I'm writing to propose a feature enhancement for the Prefix Caching mechanism. Currently, vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ical prefixes would ensure they remain in cache indefinitely, optimizing latency for high-priority workloads. ### Proposed Enhancement: Add a mechanism to mark specific prefixes as "pinned" (non-evictable). Pinned prefi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Used) eviction policy for prefix caching: when the cache reaches its capacity limit, the least recently accessed prefixes are evicted to make space for new ones. This works well for general use cases, but there are scen...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ial Considerations: - Ensuring pinned prefixes do not exceed the total cache capacity (with safeguards/errors if users attempt to pin more than possible). - Balancing pinned and dynamic (evictable) prefixes to avoid und...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
