# vllm-project/vllm#39702: [Bug]: SimpleCPUOffloadScheduler crashes with AssertionError: Expected N hit tokens, got 0 (TOCTOU race in update_state_after_alloc)

| 字段 | 值 |
| --- | --- |
| Issue | [#39702](https://github.com/vllm-project/vllm/issues/39702) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: SimpleCPUOffloadScheduler crashes with AssertionError: Expected N hit tokens, got 0 (TOCTOU race in update_state_after_alloc)

### Issue 正文摘录

## Describe the bug `SimpleCPUOffloadScheduler.update_state_after_alloc()` crashes with an `AssertionError` during long-running sessions when CPU KV offloading is enabled. ``` AssertionError: Expected 19264 hit tokens, got 0 File "vllm/v1/simple_kv_offload/manager.py", line 267, in update_state_after_alloc assert hit_length == num_external_tokens, ( f"Expected {num_external_tokens} hit tokens, got {hit_length}" ) ``` The server crashes and all in-flight requests are lost. It reproduces reliably after extended use (typically after the CPU cache fills up and LRU eviction begins). ## Root cause This is a **TOCTOU (time-of-check/time-of-use) race** between `get_num_new_matched_tokens()` and `update_state_after_alloc()`: ``` 1. scheduler.py:619 get_num_new_matched_tokens() └─ find_longest_cache_hit() → finds N tokens in CPU LRU cache returns hit_length=N, BUT discards cpu_hit_blocks (_ = ...) *** no touch() called — blocks are NOT pinned *** 2. scheduler.py:746-754 kv_cache_manager.allocate_slots() └─ may call cpu_block_pool.get_new_blocks() └─ triggers CPU LRU eviction *** the N blocks found in step 1 are evicted here *** 3. scheduler.py:771 update_state_after_alloc(request, blocks, n...

## 现有链接修复摘要

#37160 [Feat][v1] Simple yet General CPU KV Cache Offloading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -dtype fp8_e4m3 \ --max-model-len 262144 ``` ## Environment - **vLLM version**: `0.19.1rc1.dev203+g0f3ce4c74.d20260411` - **GPU**: 2× RTX 4090 (TP=2) - **Model**: Gemma4-31B AWQ-4bit - **Python**: 3.12 - **OS**: Ubuntu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: able-hybrid-kv-cache-manager \ --tensor-parallel-size 2 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 262144 ``` ## Environment - **vLLM version**: `0.19.1rc1.dev203+g0f3ce4c74.d20260411` - **GPU**: 2× RTX 4090 (TP=2) -...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: SimpleCPUOffloadScheduler crashes with AssertionError: Expected N hit tokens, got 0 (TOCTOU race in update_state_after_alloc) ## Describe the bug `SimpleCPUOffloadScheduler.update_state_after_alloc()` crashes wit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er the persistent async-load pin takes over or the request finishes. ## Configuration ```bash VLLM_USE_SIMPLE_KV_OFFLOAD=1 vllm serve \ --kv-offloading-size 32 \ --no-disable-hybrid-kv-cache-manager \ --tensor-parallel-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he the result, and reuse it in `update_state_after_alloc()` instead of searching again.** ```python # In get_num_new_matched_tokens(): cpu_hit_blocks, hit_length = self.cpu_coordinator.find_longest_cache_hit(...) if hit...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37160](https://github.com/vllm-project/vllm/pull/37160) | mentioned | 0.45 | [Feat][v1] Simple yet General CPU KV Cache Offloading | **: 3.12 - **os**: ubuntu 22.04 (linux 6.8.0) - **introduced by**: pr #37160 (merged 2026-04-01) — `simplecpuoffloadconnector` is new, `manager.py` has had zero follow-up commits… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
