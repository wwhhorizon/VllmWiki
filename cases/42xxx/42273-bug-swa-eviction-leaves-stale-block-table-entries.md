# vllm-project/vllm#42273: [Bug]: SWA eviction leaves stale block table entries

| 字段 | 值 |
| --- | --- |
| Issue | [#42273](https://github.com/vllm-project/vllm/issues/42273) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: SWA eviction leaves stale block table entries

### Issue 正文摘录

### Your current environment Additional context: - Affected area: V1 KV cache manager / worker block table / sliding-window attention - Example model: Phi-3-mini-4k-instruct (sliding_window=2047) - Example workload: chunked prefill with a prompt long enough to cross a SWA eviction boundary ### 🐛 Describe the bug ## Summary Sliding window attention (SWA) eviction can leave stale physical block ids in the worker/GPU block table for an already-running request. The CPU-side KV cache manager replaces fully skipped out-of-window logical blocks with `null_block` and calls `free_blocks` on the old physical blocks, making them eligible for reuse once their refcount reaches zero. However, for already-running/cached requests, the worker update path appends newly allocated block ids and does not appear to rewrite earlier logical slots to `null_block`. Current kernels appear to produce correct outputs because those logical positions are outside the sliding window and are pruned/masked. But I could not find a documented contract saying that stale/out-of-window block table entries may exist and that any attention backend consuming these block tables for SWA must exclude them before they can affe...

## 现有链接修复摘要

#30887 [Bugfix] [Kernel] Triton attention kernels: mask out V blocks that fall outside sliding window

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: SWA eviction leaves stale block table entries bug ### Your current environment Additional context: - Affected area: V1 KV cache manager / worker block table / sliding-window attention - Example model: Phi-3-mini-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: SWA eviction leaves stale block table entries bug ### Your current environment Additional context: - Affected area: V1 KV cache manager / worker block table / sliding-window attention - Example model: Phi-3-mini-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e entries for evicted logical positions, and attention backends are explicitly expected to make those positions unreachable via masking/pruning. If that is the intended design, could you point me to the relevant documen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ache manager / worker block table / sliding-window attention - Example model: Phi-3-mini-4k-instruct (sliding_window=2047) - Example workload: chunked prefill with a prompt long enough to cross a SWA eviction boundary #...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: stale/out-of-window block table entries may exist and that any attention backend consuming these block tables for SWA must exclude them before they can affect output. This is a possible robustness concern: if an attenti...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30887](https://github.com/vllm-project/vllm/pull/30887) | mentioned | 0.45 | [Bugfix] [Kernel] Triton attention kernels: mask out V blocks that fall outside sliding window | ting masking/pruning exactly right. there is a related precedent. pr #30887 fixed a triton attention bug where v values outside the sliding window were not fully masked, allowing… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
