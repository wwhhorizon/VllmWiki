# vllm-project/vllm#36651: cumem allocator: double-free and stale error codes during sleep/wake cycles

| 字段 | 值 |
| --- | --- |
| Issue | [#36651](https://github.com/vllm-project/vllm/issues/36651) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | import_error;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> cumem allocator: double-free and stale error codes during sleep/wake cycles

### Issue 正文摘录

## Your current environment vLLM v0.17.0 (also reproducible on main) with cumem allocator enabled, using sleep/wake cycles for colocated GRPO training. ## How would you like to use vllm Colocated training where vLLM's GPU memory is released via `sleep()` during training steps and reclaimed via `wake_up()` for inference. ## Before submitting a new issue... - [x] I have searched for [similar issues](https://github.com/vllm-project/vllm/issues). ## Description Several bugs in the cumem allocator cause CUDA driver errors during sleep/wake cycles: ### 1. Double cuMemRelease on already-unmapped allocations `sleep()` iterates all allocations and calls `unmap_and_release` unconditionally. If some allocations are already unmapped (e.g. from a previous partial sleep or external release), this causes a double `cuMemRelease`. Similarly, `wake_up()` calls `create_and_map` on already-mapped allocations. There is no per-allocation tracking of mapped state. ### 2. CUDA ops on freed memory during sleep When the allocator is sleeping, PyTorch's garbage collector can trigger `my_free` on tensors whose backing memory was already released by `sleep()`. The C++ `my_free` then calls `unmap_and_release`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: sleep/wake cycles ## Your current environment vLLM v0.17.0 (also reproducible on main) with cumem allocator enabled, using sleep/wake cycles for colocated GRPO training. ## How would you like to use vllm Colocated train...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: p()` for inference. ## Before submitting a new issue... - [x] I have searched for [similar issues](https://github.com/vllm-project/vllm/issues). ## Description Several bugs in the cumem allocator cause CUDA driver error...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ed from the Python callback. This can cause incorrect unmapping. ### 5. Flash Attention 4 rotary embedding import failure `find_spec("flash_attn")` succeeds with FA4 installed, but `from flash_attn.ops.triton.rotary imp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: during sleep/wake cycles ## Your current environment vLLM v0.17.0 (also reproducible on main) with cumem allocator enabled, using sleep/wake cycles for colocated GRPO training. ## How would you like to use vllm Colocate...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: recv_size` returned from the Python callback. This can cause incorrect unmapping. ### 5. Flash Attention 4 rotary embedding import failure `find_spec("flash_attn")` succeeds with FA4 installed, but `from flash_attn.ops....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
