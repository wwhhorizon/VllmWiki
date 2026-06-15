# vllm-project/vllm#42571: [Bug]: KV Block double free when using eager SimpleCPUOffloading + Sliding window attention

| 字段 | 值 |
| --- | --- |
| Issue | [#42571](https://github.com/vllm-project/vllm/issues/42571) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV Block double free when using eager SimpleCPUOffloading + Sliding window attention

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description of the bug We encountered a double-free issue (same physical block added to free list twice) when eager SimpleCPUOffload is enabled and using a model with sliding window attention (gpt-oss-120b in our case). Specifically, the same physical block can be reused for sliding window attention during the same request, as it may be freed and used to hold new KV cache when it is no longer in the window. Each time the physical block enters the sliding window, its block ID is appended to CPU block list (`StoreRequestState.block_ids`). Thus, the same block may be listed in the CPU offloading list multiple times for the same LLM request. This interacts with the block freeing logic (`BlockPool.free_blocks()`) in a problematic way when eager offload finishes. If the same physical `KVCacheBlock` appears more than once in a single LLM request, the current implementation decrements the block's `ref_cnt` for each occurrence, then appends every occurrence whose final `ref_cnt == 0` to `free_block_queue`. That means a batched release such as `free_blocks([block, block])` can make `free_block_queue.num_free_blocks` increase by two for...

## 现有链接修复摘要

#42615 [Bugfix] Dedup gpu_block_ids in SimpleCPUOffload eager store path | #42903 [Bugfix][kv_offload] Dedup gpu_block_ids in eager-mode SCO (store + load paths)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing a model with sliding window attention (gpt-oss-120b in our case). Specifically, the same physical block can be reused for sliding window attention during the same request, as it may be freed and used to hold new KV...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: hysical block can be reused for sliding window attention during the same request, as it may be freed and used to hold new KV cache when it is no longer in the window. Each time the physical block enters the sliding wind...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: KV Block double free when using eager SimpleCPUOffloading + Sliding window attention bug ### Your current environment ### 🐛 Describe the bug ## Description of the bug We encountered a double-free issue (same phys...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: KV Block double free when using eager SimpleCPUOffloading + Sliding window attention bug ### Your current environment ### 🐛 Describe the bug ## Description of the bug We encountered a double-free issue (same phys...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42615](https://github.com/vllm-project/vllm/pull/42615) | closes_keyword | 0.95 | [Bugfix] Dedup gpu_block_ids in SimpleCPUOffload eager store path | Fixes #42571 ### Problem When eager `SimpleCPUOffloading` is combined with sliding-window attention, the same physical `KVCacheBlock` can be reused within a single request as the |
| [#42903](https://github.com/vllm-project/vllm/pull/42903) | closes_keyword | 0.95 | [Bugfix][kv_offload] Dedup gpu_block_ids in eager-mode SCO (store + load paths) | Fixes #42085. Same defect class as #42571. ## What's broken `SimpleCPUOffloadScheduler` emits duplicate `gpu_block_ids` in two places: ### Store path (`_prepare_eager_store_spec |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
