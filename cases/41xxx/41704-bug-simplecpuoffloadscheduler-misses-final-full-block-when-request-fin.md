# vllm-project/vllm#41704: [Bug]: SimpleCPUOffloadScheduler misses final full block when request finishes in the same scheduler step

| 字段 | 值 |
| --- | --- |
| Issue | [#41704](https://github.com/vllm-project/vllm/issues/41704) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: SimpleCPUOffloadScheduler misses final full block when request finishes in the same scheduler step

### Issue 正文摘录

## Describe the bug In eager mode, `SimpleCPUOffloadScheduler` can miss the final full KV block of a request when that block is computed in the same scheduler step where the request finishes. The store planner only considers blocks whose KV data has been confirmed computed before the current scheduler step. The code already documents this edge case in `vllm/v1/simple_kv_offload/manager.py`: ```python # Only considers blocks whose KV data has been **confirmed computed** by # the GPU. This means blocks from the current step are NOT stored until the # next step. If a request finishes in the same step as its last full block, # that block may be missed. (TODO: flush on finish.) ``` When the request finishes in that same step, `request_finished()` clears the eager store tracking state before a later scheduler step can observe and offload the newly completed block. ## Impact A later request that extends the same prompt can get a shorter CPU KV cache hit than expected. The final full block of the prior request is recomputed instead of being loaded from CPU offload. This affects the `SimpleCPUOffloadScheduler` / `SimpleCPUOffloadConnector` path, not the older weight offload path. ## Why th...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: t A later request that extends the same prompt can get a shorter CPU KV cache hit than expected. The final full block of the prior request is recomputed instead of being loaded from CPU offload. This affects the `Simple...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: , not the older weight offload path. ## Why this happens The scheduler builds connector metadata before it advances `request.num_computed_tokens` for the current step: 1. `Scheduler.schedule()` calls `connector.build_co...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: SimpleCPUOffloadScheduler misses final full block when request finishes in the same scheduler step ## Describe the bug In eager mode, `SimpleCPUOffloadScheduler` can miss the final full KV block of a request when...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: SimpleCPUOffloadScheduler misses final full block when request finishes in the same scheduler step ## Describe the bug In eager mode, `SimpleCPUOffloadScheduler` can miss the final full KV block of a request when...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: SimpleCPUOffloadScheduler misses final full block when request finishes in the same scheduler step ## Describe the bug In eager mode, `SimpleCPUOffloadScheduler` can miss the final full KV block of a request when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
