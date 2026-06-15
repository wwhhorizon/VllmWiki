# vllm-project/vllm#33864: Bug: CPU KV cache offloading fails for blocks formed during decode

| 字段 | 值 |
| --- | --- |
| Issue | [#33864](https://github.com/vllm-project/vllm/issues/33864) |
| 状态 | closed |
| 标签 | bug;kv-connector |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug: CPU KV cache offloading fails for blocks formed during decode

### Issue 正文摘录

## Summary When using CPU KV cache offloading (`--kv-offloading-size`), blocks that complete during the decode phase are never offloaded to CPU. Only blocks that complete during prefill are correctly offloaded. ## Root Cause In `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`, the `_get_reqs_to_store()` method calculates the number of blocks to store using: ```python new_tokens = scheduler_output.num_scheduled_tokens[req_id] total_tokens = req.num_computed_tokens + new_tokens num_blocks = total_tokens // self.offloaded_block_size ``` The problem is that `req.block_hashes` only contains hashes for **already-computed tokens**, not for tokens being scheduled in the current step. When the code later tries to access `req.block_hashes[block_idx]`, it fails silently for decode-formed blocks because those hashes don't exist yet. ## Why Prefill Works But Decode Fails - **Prefill**: All prompt tokens are computed in one step. By the next scheduler step, all block hashes exist in `req.block_hashes`, so the calculation works correctly. - **Decode**: Tokens are added incrementally. When `_get_reqs_to_store()` runs, it calculates blocks based on `num_computed_tokens + new_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Bug: CPU KV cache offloading fails for blocks formed during decode bug;kv-connector ## Summary When using CPU KV cache offloading (`--kv-offloading-size`), blocks that complete during the decode phase are never offloade...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cheStoreCommitted` events are not emitted for decode blocks, breaking tracing/monitoring 3. **Index corruption**: The internal `_next_stored_block_idx` tracker gets out of sync, causing incorrect behavior for subsequent...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Bug: CPU KV cache offloading fails for blocks formed during decode bug;kv-connector ## Summary When using CPU KV cache offloading (`--kv-offloading-size`), blocks that complete during the decode phase are never offloade...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Bug: CPU KV cache offloading fails for blocks formed during decode bug;kv-connector ## Summary When using CPU KV cache offloading (`--kv-offloading-size`), blocks that complete during the decode phase are never offloade...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
