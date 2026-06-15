# vllm-project/vllm#31371: [Feature]: Sort blocks by block_id in FreeKVCacheBlockQueue.append_n to enable contiguous allocation

| 字段 | 值 |
| --- | --- |
| Issue | [#31371](https://github.com/vllm-project/vllm/issues/31371) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Sort blocks by block_id in FreeKVCacheBlockQueue.append_n to enable contiguous allocation

### Issue 正文摘录

### The feature, motivation and pitch **Description:** We are working on a layer-wise KV cache transfer system and have observed that maintaining forward-contiguous block allocation significantly improves I/O efficiency. **The Problem:** When blocks are allocated in ascending order (e.g., `[1, 2, 3, 4, 5]`), we can merge multiple I/O submissions into a single contiguous transfer (`[1-5]`). However, if blocks are allocated in arbitrary or reverse order (e.g., `[5, 4, 3, 2, 1]`), each block requires a separate I/O submission. For long requests, this difference is substantial—potentially thousands of I/O submissions (number of blocks × number of layers) versus a handful of merged operations. **Proposed Solution:** Add a simple sort when returning blocks to the free list in `FreeKVCacheBlockQueue.append_n`: ```python def append_n(self, blocks: list[KVCacheBlock]) -> None: """Put a list of blocks back into the free list.""" if len(blocks) == 0: return blocks.sort(key=lambda x: x.block_id) # <-- Add this line last_block = self.fake_free_list_tail.prev_free_block ... ``` **File location:** `vllm/v1/core/kv_cache_utils.py` This ensures that when blocks are subsequently allocated, they ten...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Sort blocks by block_id in FreeKVCacheBlockQueue.append_n to enable contiguous allocation feature request;stale ### The feature, motivation and pitch **Description:** We are working on a layer-wise KV cache t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lity in KV cache operations. **Impact:** - Minimal overhead (sorting a small list of freed blocks) - Significant potential benefit for systems performing batched or layer-wise KV cache transfers ### Alternatives _No res...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Feature]: Sort blocks by block_id in FreeKVCacheBlockQueue.append_n to enable contiguous allocation feature request;stale ### The feature, motivation and pitch **Description:** We are working on a layer-wise KV cache t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ining forward-contiguous block allocation significantly improves I/O efficiency. **The Problem:** When blocks are allocated in ascending order (e.g., `[1, 2, 3, 4, 5]`), we can merge multiple I/O submissions into a sing...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: , motivation and pitch **Description:** We are working on a layer-wise KV cache transfer system and have observed that maintaining forward-contiguous block allocation significantly improves I/O efficiency. **The Problem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
