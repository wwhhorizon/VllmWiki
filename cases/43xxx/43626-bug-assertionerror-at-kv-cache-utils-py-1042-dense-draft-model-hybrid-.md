# vllm-project/vllm#43626: [Bug]: AssertionError at kv_cache_utils.py:1042 — dense draft model + hybrid-attention main (DeltaNet+SWA) fails in unify_kv_cache_spec_page_size

| 字段 | 值 |
| --- | --- |
| Issue | [#43626](https://github.com/vllm-project/vllm/issues/43626) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;moe;operator |
| 症状 | crash;nondeterministic;slowdown |
| 根因提示 | dtype;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError at kv_cache_utils.py:1042 — dense draft model + hybrid-attention main (DeltaNet+SWA) fails in unify_kv_cache_spec_page_size

### Issue 正文摘录

## Summary Pairing a **dense draft model** (`LocoOperator/LocoOperator-4B`) with a **hybrid-attention main model** (`Qwen/Qwen3-Coder-Next-80B-A3B`, DeltaNet + sliding-window attention) fails at engine init with a bare `AssertionError` in `unify_kv_cache_spec_page_size` — the dense draft's `page_size_bytes` doesn't equal the hybrid main's `max_page_size`. ## Stack trace (live, deterministic across 3 boot attempts) ``` File "/usr/local/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5951, in profile_cudagraph_memory self._init_minimal_kv_cache_for_profiling() File "/usr/local/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5870, in _init_minimal_kv_cache_for_profiling kv_cache_groups = get_kv_cache_groups(self.vllm_config, kv_cache_spec) File "/usr/local/lib/python3.12/site-packages/vllm/v1/core/kv_cache_utils.py", line 1654, in get_kv_cache_groups kv_cache_spec = unify_kv_cache_spec_page_size(kv_cache_spec) File "/usr/local/lib/python3.12/site-packages/vllm/v1/core/kv_cache_utils.py", line 1042, in unify_kv_cache_spec_page_size assert new_spec.page_size_bytes == max_page_size AssertionError ``` ## Reproduction - **Main**: `Qwen/Qwen3-C...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ionError ``` ## Reproduction - **Main**: `Qwen/Qwen3-Coder-Next-80B-A3B-NVFP4` (DeltaNet + SWA hybrid attention, MoE 3B-active / 80B total) - **Draft**: `LocoOperator/LocoOperator-4B` (4B dense) - **Args** added to an o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: site-packages/vllm/v1/worker/gpu_model_runner.py", line 5951, in profile_cudagraph_memory self._init_minimal_kv_cache_for_profiling() File "/usr/local/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: doesn't equal the hybrid main's `max_page_size`. ## Stack trace (live, deterministic across 3 boot attempts) ``` File "/usr/local/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5951, in profile_c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: doesn't equal the hybrid main's `max_page_size`. ## Stack trace (live, deterministic across 3 boot attempts) ``` File "/usr/local/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5951, in profile_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AssertionError at kv_cache_utils.py:1042 — dense draft model + hybrid-attention main (DeltaNet+SWA) fails in unify_kv_cache_spec_page_size ## Summary Pairing a **dense draft model** (`LocoOperator/LocoOperator-4B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
