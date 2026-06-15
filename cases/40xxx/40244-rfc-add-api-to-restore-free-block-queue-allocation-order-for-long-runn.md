# vllm-project/vllm#40244: [RFC]: Add API to restore free_block_queue allocation order for long-running RLHF / rollout sessions

| 字段 | 值 |
| --- | --- |
| Issue | [#40244](https://github.com/vllm-project/vllm/issues/40244) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add API to restore free_block_queue allocation order for long-running RLHF / rollout sessions

### Issue 正文摘录

### Motivation. `reset_prefix_cache()` is explicitly documented as intended for use in RLHF flows (to invalidate prefix caching after weight updates) and for benchmarking. In those flows it is natural to call it between logical rounds / rollout iterations while no requests are active. However, the current implementation **only clears the prefix cache hash table; it does not restore the allocation order of `free_block_queue`**. Over many rounds the linked list becomes progressively scrambled, which in turn scatters newly allocated `block_table[req, :]` entries across the physical KV pool and degrades attention-kernel locality on subsequent prefills. The net effect on long-running sessions is a **monotonic prefill slowdown** even when no recompilation, no new cache entries, and no KV pressure changes are occurring between rounds. ### How the scrambling happens - `BlockPool.__init__` initializes `free_block_queue` as the strictly increasing sequence `[1, 2, ..., N-1]` (block 0 is the null block). - `popleft()` takes blocks off the head at allocation time; on request completion, a request's blocks are appended back to the tail **in reverse order of the request's own blocks** (as descr...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Add API to restore free_block_queue allocation order for long-running RLHF / rollout sessions RFC ### Motivation. `reset_prefix_cache()` is explicitly documented as intended for use in RLHF flows (to invalidate p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: F / rollout sessions RFC ### Motivation. `reset_prefix_cache()` is explicitly documented as intended for use in RLHF flows (to invalidate prefix caching after weight updates) and for benchmarking. In those flows it is n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [RFC]: Add API to restore free_block_queue allocation order for long-running RLHF / rollout sessions RFC ### Motivation. `reset_prefix_cache()` is explicitly documented as intended for use in RLHF flows (to invalidate p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: n RLHF flows (to invalidate prefix caching after weight updates) and for benchmarking. In those flows it is natural to call it between logical rounds / rollout iterations while no requests are active. However, the curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e is large. Decode is far less affected because each step only touches a small number of new KV pages. ### Why `reset_prefix_cache()` alone is not enough `BlockPool.reset_prefix_cache()` currently does the following and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
