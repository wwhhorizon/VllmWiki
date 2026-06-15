# vllm-project/vllm#43711: [RFC]: Debug observation for prefix-cache lookup boundary before request-level stats

| 字段 | 值 |
| --- | --- |
| Issue | [#43711](https://github.com/vllm-project/vllm/issues/43711) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Debug observation for prefix-cache lookup boundary before request-level stats

### Issue 正文摘录

### Motivation. I’m trying to calibrate a narrow vLLM observability boundary, not propose a new serving API, scheduling policy, eviction policy, admission mechanism, offload mechanism, or external framework. Current read: vLLM exposes useful request/prefill-level prefix-cache signals, including cached-token counts. However, I do not see a native debug record that identifies a specific prefix-cache lookup with: - lookup boundary, - event order, - cache/hash identity, - local hit length, - and bounded matched-prefix evidence or an opaque correlation handle. Is that read wrong? Is there already a native vLLM event, trace field, invariant, or debug artifact that lets a user distinguish: > “this specific expected prefix span was observed at lookup under this cache/hash identity” from: > “this request had some cached tokens”? The motivating debugging cases are ordinary prefix-cache cases: - a nonzero cached-token count that may be shorter than the expected prefix; - a hit from a different cache/hash domain or configuration than the one being debugged; - repeated lookup paths caused by chunking, batching, retries, or scheduling behavior; - a user or external debugger needing to know whic...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Debug observation for prefix-cache lookup boundary before request-level stats RFC ### Motivation. I’m trying to calibrate a narrow vLLM observability boundary, not propose a new serving API, scheduling policy, ev...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a new serving API, scheduling policy, eviction policy, admission mechanism, offload mechanism, or external framework. Current read: vLLM exposes useful request/prefill-level prefix-cache signals, including cached-token...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ew serving API, scheduling policy, eviction policy, admission mechanism, offload mechanism, or external framework. Current read: vLLM exposes useful request/prefill-level prefix-cache signals, including cached-token cou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: counts. However, I do not see a native debug record that identifies a specific prefix-cache lookup with: - lookup boundary, - event order, - cache/hash identity, - local hit length, - and bounded matched-prefix evidence...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: immediately after: ```python coordinator.find_longest_cache_hit(request.block_hashes, max_cache_hit_length) ``` inside: ```text vllm.v1.core.kv_cache_manager.KVCacheManager.get_computed_blocks ``` and before prefix-cach...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
