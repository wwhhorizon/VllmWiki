# vllm-project/vllm#20492: [RFC]: KV-Cache Interoperability API Standardization

| 字段 | 值 |
| --- | --- |
| Issue | [#20492](https://github.com/vllm-project/vllm/issues/20492) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: KV-Cache Interoperability API Standardization

### Issue 正文摘录

### Motivation This RFC proposes a KV-Cache Interoperability API, covering standardized notification events (via KVEvents) and reproducible prefix-block hashing. These standards aim to support cross-system cache awareness, observability, and future tooling for indexing, routing, and diagnostics. vLLM already ships with internal [KVEvents](https://github.com/vllm-project/vllm/issues/16669) contributed by the NVIDIA Dynamo team - that’s a strong foundation. But as external systems aim for cache-aware inference, we need to treat these internal mechanisms as public contracts to support broader adoption and interop. ### Goals 1. **KVEvents Internal API as a Public Contract** The KVEvents schema is already well-defined in vLLM and used internally by the `KVCacheManager` for GPU cache events. It’s also being extended to CPU offloading via the `KVConnector` (see [#19854](https://github.com/vllm-project/vllm/issues/19854)). This RFC proposes formalizing KVEvents as the public contract for any component emitting or consuming KV-Cache lifecycle events - including external indexers, routers, and engines. 2. **Ensure Reproducible Block Hashing Across Languages** Prefix cache block keys must be...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [RFC]: KV-Cache Interoperability API Standardization RFC;stale ### Motivation This RFC proposes a KV-Cache Interoperability API, covering standardized notification events (via KVEvents) and reproducible prefix-block has...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nd future tooling for indexing, routing, and diagnostics. vLLM already ships with internal [KVEvents](https://github.com/vllm-project/vllm/issues/16669) contributed by the NVIDIA Dynamo team - that’s a strong foundation...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: standardized notification events (via KVEvents) and reproducible prefix-block hashing. These standards aim to support cross-system cache awareness, observability, and future tooling for indexing, routing, and diagnostic...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: API, covering standardized notification events (via KVEvents) and reproducible prefix-block hashing. These standards aim to support cross-system cache awareness, observability, and future tooling for indexing, routing,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s -> vLLM-hashes. While this avoids introducing reproducible hashing and configuration syncs, it requires complex indexing and lookups, along with the networking overhead of passing the 32bit token-ids in every event. 3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
