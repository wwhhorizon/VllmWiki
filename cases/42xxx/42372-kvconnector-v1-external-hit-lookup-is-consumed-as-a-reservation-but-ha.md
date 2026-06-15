# vllm-project/vllm#42372: KVConnector V1 external hit lookup is consumed as a reservation, but has no plan/abort lifecycle

| 字段 | 值 |
| --- | --- |
| Issue | [#42372](https://github.com/vllm-project/vllm/issues/42372) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KVConnector V1 external hit lookup is consumed as a reservation, but has no plan/abort lifecycle

### Issue 正文摘录

### Summary In the current V1 `KVConnector` scheduler flow, `get_num_new_matched_tokens()` looks like a query-style API, but a positive result is later consumed as a commitment by `update_state_after_alloc()`. That creates an ambiguous contract for external KV backends that need eviction protection, remote leases, prefetch state, pinning, or any other reservation-like behavior. ### Current flow The scheduler calls: ```python ext_tokens, load_kv_async = connector.get_num_new_matched_tokens( request, num_new_local_computed_tokens, ) ``` If `ext_tokens` is positive, the scheduler uses that value to allocate cache blocks: ```python new_blocks = kv_cache_manager.allocate_slots( request, num_new_tokens, num_external_computed_tokens=ext_tokens, delay_cache_blocks=load_kv_async, ... ) ``` Then it calls: ```python connector.update_state_after_alloc( request, kv_cache_manager.get_blocks(request_id), ext_tokens, ) ``` `update_state_after_alloc()` has no return value and no normal way to say: the earlier lookup returned 100 external tokens, but only 50 are still valid now. So once `get_num_new_matched_tokens()` returns a positive token count, that value is effectively a reservation-level comm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t of connector-side machinery caused by the API shape, not by backend-specific business logic. ### Example Suppose an external backend observes 100 matching tokens: ```python get_num_new_matched_tokens(...) -> (100, Tru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ext_tokens` is positive, the scheduler uses that value to allocate cache blocks: ```python new_blocks = kv_cache_manager.allocate_slots( request, num_new_tokens, num_external_computed_tokens=ext_tokens, delay_cache_bloc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: has no plan/abort lifecycle ### Summary In the current V1 `KVConnector` scheduler flow, `get_num_new_matched_tokens()` looks like a query-style API, but a positive result is later consumed as a commitment by `update_sta...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tate_after_alloc()`. That creates an ambiguous contract for external KV backends that need eviction protection, remote leases, prefetch state, pinning, or any other reservation-like behavior. ### Current flow The schedu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: If `ext_tokens` is positive, the scheduler uses that value to allocate cache blocks: ```python new_blocks = kv_cache_manager.allocate_slots( request, num_new_tokens, num_external_computed_tokens=ext_tokens, delay_cache_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
