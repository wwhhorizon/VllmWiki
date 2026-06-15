# vllm-project/vllm#44238: [Bug] MooncakeConnector: KV cache data corruption under concurrent PD transfers (batch_transfer_sync_write race)

| 字段 | 值 |
| --- | --- |
| Issue | [#44238](https://github.com/vllm-project/vllm/issues/44238) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] MooncakeConnector: KV cache data corruption under concurrent PD transfers (batch_transfer_sync_write race)

### Issue 正文摘录

## Summary When running vLLM in Prefill-Decode disaggregated mode with `MooncakeConnector`, KV cache data corruption is observed at the decode side under moderate concurrency. The source buffer remains consistent (pre/post hash match), but the destination buffer content diverges from the source after `batch_transfer_sync_write` completes. ## Environment - **Model**: Qwen3-Omni-30B-A3B-Instruct - **Mode**: vLLM PD disaggregated (1 prefill process + 1 decode process) - **Transfer**: MooncakeConnector + proxy - **Workload**: Audio-in-video streaming requests (large descriptors) - **Protocol**: RDMA ## Reproduction ``` WARMUP_ROUNDS=2 STRESS_ROUNDS=8 BATCH_SIZE=5 # Total ~50 requests stream=True, max_tokens=96 ``` The issue is **reproducible on every run** of the stress script, though the specific request/descriptor that exhibits mismatch varies. ## Observed Behavior ### Transfer Details (single failing request) A single request has 8 descriptors checked: - 4 large descriptors: `length=2,424,832` bytes each - 4 small descriptors: `length=16,384` bytes each - Total per request: ~9.3 MiB ### Verification Method - **Sender side**: Computes `src_hash_pre` before transfer, `src_hash_post`...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: nsfers (batch_transfer_sync_write race) ## Summary When running vLLM in Prefill-Decode disaggregated mode with `MooncakeConnector`, KV cache data corruption is observed at the decode side under moderate concurrency. The...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ZE=5 # Total ~50 requests stream=True, max_tokens=96 ``` The issue is **reproducible on every run** of the stress script, though the specific request/descriptor that exhibits mismatch varies. ## Observed Behavior ### Tr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Total ~50 requests stream=True, max_tokens=96 ``` The issue is **reproducible on every run** of the stress script, though the specific request/descriptor that exhibits mismatch varies. ## Observed Behavior ### Transfer...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug] MooncakeConnector: KV cache data corruption under concurrent PD transfers (batch_transfer_sync_write race) ## Summary When running vLLM in Prefill-Decode disaggregated mode with `MooncakeConnector`, KV cache data...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: is Looking at `mooncake_connector.py`, the transfer path is: 1. `_read_blocks()` receives pull request from decode side via ZMQ 2. `_build_transfer_params()` assembles `src_ptrs`, `dst_ptrs`, `lengths` from block IDs 3....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
