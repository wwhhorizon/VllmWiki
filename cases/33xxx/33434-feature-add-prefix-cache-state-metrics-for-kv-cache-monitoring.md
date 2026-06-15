# vllm-project/vllm#33434: [Feature]: Add prefix cache state metrics for KV cache monitoring

| 字段 | 值 |
| --- | --- |
| Issue | [#33434](https://github.com/vllm-project/vllm/issues/33434) |
| 状态 | open |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add prefix cache state metrics for KV cache monitoring

### Issue 正文摘录

## 🚀 The feature, motivation and pitch ### Motivation When monitoring vLLM in production with Grafana dashboards, the current `vllm:kv_cache_usage_perc` metric shows total KV cache usage but doesn't distinguish between: - **Active blocks**: Blocks currently being used by running requests - **Prefix cached blocks**: Blocks stored in the prefix cache for potential reuse This makes it difficult to: 1. Understand actual memory pressure from active requests 2. Monitor prefix cache effectiveness 3. Plan capacity based on available token capacity ### Proposed Feature Add new Prometheus metrics to expose prefix cache state: | Metric | Type | Description | |--------|------|-------------| | `vllm:num_kv_cache_total_blocks` | Gauge | Total KV cache blocks available | | `vllm:num_prefix_cached_blocks` | Gauge | Blocks currently in prefix cache | | `vllm:num_prefix_cached_tokens` | Gauge | Tokens currently in prefix cache | | `vllm:prefix_cache_usage_perc` | Gauge | Prefix cache usage as fraction of total (0-1) | ### Use Cases These metrics enable users to calculate derived metrics in Grafana: ```promql # Active KV cache usage (blocks serving requests, excluding idle prefix cache) vllm:kv_cach...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Feature]: Add prefix cache state metrics for KV cache monitoring stale ## 🚀 The feature, motivation and pitch ### Motivation When monitoring vLLM in production with Grafana dashboards, the current `vllm:kv_cache_usage_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add prefix cache state metrics for KV cache monitoring stale ## 🚀 The feature, motivation and pitch ### Motivation When monitoring vLLM in production with Grafana dashboards, the current `vllm:kv_cache_usage_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: or: - Capacity planning in production deployments - Understanding prefix cache hit rates in context of memory usage - Auto-scaling decisions based on actual available capacity
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e from active requests 2. Monitor prefix cache effectiveness 3. Plan capacity based on available token capacity ### Proposed Feature Add new Prometheus metrics to expose prefix cache state: | Metric | Type | Description...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: c shows total KV cache usage but doesn't distinguish between: - **Active blocks**: Blocks currently being used by running requests - **Prefix cached blocks**: Blocks stored in the prefix cache for potential reuse This m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
