# vllm-project/vllm#19854: [RFC]: KV cache offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#19854](https://github.com/vllm-project/vllm/issues/19854) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 57; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: KV cache offloading

### Issue 正文摘录

### Motivation. Currently, in vLLM v1 there is no in-house solution for offloading KV cache data from the GPU memory to other medium (in particular, CPU memory). There is a proposed RFC (#16144) and respective PRs (#13377 and #17653) that try to address that. The approach they take is somewhat similar to the way offloading was implemented in V0: 1. On the scheduler side, extend the core GPU allocator (KVCacheManager) to support CPU offloading 2. On the worker side, add a synchronous call to handle the actual CPU GPU transfer in the `execute_model` function. In this RFC I propose an alternative approach which supports the following requirements: * **Async saving** of new KV data from GPU to cache. GPU memory will not be freed until save is completed (similar to NixlConnector) * **Async loading** of KV data from the cache to GPU. Requests waiting for cache load won't be scheduled until load is completed (similar to NixlConnector) * Support **pluggable backends** for cache (CPU backend for start) * Allow pulling of **cache events** (cache insert, evict, access), in the same way as the GPU cache. This will allow a unified KVCacheEvent stream. * Enable **LRU eviction** of offloaded dat...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: KV cache offloading RFC;keep-open ### Motivation. Currently, in vLLM v1 there is no in-house solution for offloading KV cache data from the GPU memory to other medium (in particular, CPU memory). There is a propo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: somewhat similar to the way offloading was implemented in V0: 1. On the scheduler side, extend the core GPU allocator (KVCacheManager) to support CPU offloading 2. On the worker side, add a synchronous call to handle th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: evictions of offloaded data. Its output will be encoded over `KVConnectorMetadata` and sent to workers. On the worker side, we will also have an OffloadingConnector which parses load/store requests sent by the `Offloadi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: until load is completed (similar to NixlConnector) * Support **pluggable backends** for cache (CPU backend for start) * Allow pulling of **cache events** (cache insert, evict, access), in the same way as the GPU cache....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
