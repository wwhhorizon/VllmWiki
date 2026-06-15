# vllm-project/vllm#42085: [Bug]: SimpleCPUOffloadConnector + Hybrid KV Cache Manager: GPU block pool exhaustion (popleft_n assert) on second long-context request

| 字段 | 值 |
| --- | --- |
| Issue | [#42085](https://github.com/vllm-project/vllm/issues/42085) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;fp8 |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SimpleCPUOffloadConnector + Hybrid KV Cache Manager: GPU block pool exhaustion (popleft_n assert) on second long-context request

### Issue 正文摘录

# [Bug]: SimpleCPUOffloadConnector + Hybrid KV Cache Manager: GPU block pool exhaustion (`popleft_n` assert) on second long-context request ## Describe the bug After a single long-context request completes successfully, the next request crashes the engine in the GPU block allocator. `single_type_kv_cache_manager.allocate_new_blocks()` calls `block_pool.get_new_blocks(N)` which calls `free_block_queue.popleft_n(N)`. The free queue runs dry mid-pop and the assertion fires: ``` File "vllm/v1/core/sched/scheduler.py", line 744, in schedule new_blocks = self.kv_cache_manager.allocate_slots(...) File "vllm/v1/core/kv_cache_manager.py", line 400, in allocate_slots new_blocks = self.coordinator.allocate_new_blocks(...) File "vllm/v1/core/kv_cache_coordinator.py", line 187, in allocate_new_blocks File "vllm/v1/core/single_type_kv_cache_manager.py", line 270, in allocate_new_blocks new_blocks = self.block_pool.get_new_blocks(num_new_blocks) File "vllm/v1/core/block_pool.py", line 336, in get_new_blocks ret = self.free_block_queue.popleft_n(num_blocks) File "vllm/v1/core/kv_cache_utils.py", line 269, in popleft_n assert curr_block is not None AssertionError ``` The `EngineCore` then exits, a...

## 现有链接修复摘要

#42903 [Bugfix][kv_offload] Dedup gpu_block_ids in eager-mode SCO (store + load paths)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: on reset (engine dead). The crash fires in `Scheduler.schedule()` while building S1's first chunked-prefill step, before any model execution. So whatever GPU blocks the allocator expected to be available at that moment,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ention + sliding-window + chunked-local. The full-attention group is the smallest (this run reports `Available KV cache memory: 7.13 GiB → 145,274 tokens`). When S0 finishes, `SimpleCPUOffloadConnector` enqueues an asyn...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: SimpleCPUOffloadConnector + Hybrid KV Cache Manager: GPU block pool exhaustion (popleft_n assert) on second long-context request # [Bug]: SimpleCPUOffloadConnector + Hybrid KV Cache Manager: GPU block pool exhaus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ger: GPU block pool exhaustion (popleft_n assert) on second long-context request # [Bug]: SimpleCPUOffloadConnector + Hybrid KV Cache Manager: GPU block pool exhaustion (`popleft_n` assert) on second long-context reques...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: from `docker/Dockerfile.full` ### Server command ```yaml - --kv-cache-dtype=fp8 - --block-size=256 - --max-model-len=128000 - --gpu-memory-utilization=0.97 - --tensor-parallel-size=2 - --kv-transfer-config={"kv_connecto...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42903](https://github.com/vllm-project/vllm/pull/42903) | closes_keyword | 0.95 | [Bugfix][kv_offload] Dedup gpu_block_ids in eager-mode SCO (store + load paths) | Fixes #42085. Same defect class as #42571. ## What's broken `SimpleCPUOffloadScheduler` emits duplicate `gpu_block_ids` in two places: ### Store path (`_prepare_eager_store_spec |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
