# vllm-project/vllm#33123: [Bug][ROCm]: Prefix caching produces different output on first request (cache miss) vs subsequent requests (cache hit)

| 字段 | 值 |
| --- | --- |
| Issue | [#33123](https://github.com/vllm-project/vllm/issues/33123) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: Prefix caching produces different output on first request (cache miss) vs subsequent requests (cache hit)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On AMD MI355X GPUs (gfx950), vLLM with prefix caching enabled produces **different output on the first request vs subsequent identical requests**. The first request (cache miss -> full prefill) returns a different result than subsequent requests (cache hit -> partial prefill with cached KV). This does **not** occur on AMD MI325X. ### Environment - **GPU**: AMD Instinct MI355X (gfx950) - **vLLM Version**: Current upstream (0.14.0rc2.dev293+g4561f1398.d20260125.rocm700) - **Model**: Qwen/Qwen3-0.6B ### Bug Description When prefix caching is enabled on MI355X, the **first request computes attention from scratch** (no cached KV to reuse), while **subsequent identical requests reuse the cached KV prefix**. These two computation paths produce numerically different results on MI355X, causing the first request's output to differ from all subsequent requests. | Request | Cache Status | Computation Path | Output | |---------|--------------|------------------|--------| | Run 1 | ❌ Cache miss | Full prefill | `'The European Union consists of 27 member states'` | | Run 2 | ✅ Cache hit | Partial prefill + cached KV | `'The European Union (EU)...

## 现有链接修复摘要

#33759 fix(rocm): Use correct kv_cache_layout for sliding window with shuffle KV cache | #33761 fix(rocm): use correct kv_cache_layout in extend_for_sliding_window | #34878 [ROCm][Test] Fix beam search determinism failures from batch-size-dependent FP divergence and removed wrong marker | #35553 [ROCm][CI] Fix tool use test stability - disable skinny GEMM, prefix caching, eliminate batch variance | #40179 [Core] Add --deterministic-prefix-caching for reproducible prefill on ROCm

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 10: [Bug][ROCm]: Prefix caching produces different output on first request (cache miss) vs subsequent requests (cache hit) bug;rocm;stale ### Your current environment ### 🐛 Describe the bug On AMD MI355X GPUs (gfx950), vLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug][ROCm]: Prefix caching produces different output on first request (cache miss) vs subsequent requests (cache hit) bug;rocm;stale ### Your current environment ### 🐛 Describe the bug On AMD MI355X GPUs (gfx950), vLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 325X. ### Environment - **GPU**: AMD Instinct MI355X (gfx950) - **vLLM Version**: Current upstream (0.14.0rc2.dev293+g4561f1398.d20260125.rocm700) - **Model**: Qwen/Qwen3-0.6B ### Bug Description When prefix caching is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug][ROCm]: Prefix caching produces different output on first request (cache miss) vs subsequent requests (cache hit) bug;rocm;stale ### Your current environment ### 🐛 Describe the bug On AMD MI355X GPUs (gfx950), vLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: issue. Also, this does not happen on CUDA, even under the same attention backend. Furthermore, this happens on ROCm under both `TRITON_ATTN` and `ROCM_AITER_FA`, therefore it is not an attention backend-specific issue....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33759](https://github.com/vllm-project/vllm/pull/33759) | closes_keyword | 0.95 | fix(rocm): Use correct kv_cache_layout for sliding window with shuffle KV cache | Fixes #33123 The `extend_for_sliding_window` method in the ROCm AITER Flash Attention backend was using a hardcoded `kv_cache_layout="NHD"` while the actual storage path uses SHUF |
| [#33761](https://github.com/vllm-project/vllm/pull/33761) | closes_keyword | 0.95 | fix(rocm): use correct kv_cache_layout in extend_for_sliding_window | Fixes #33123 - Non-deterministic prefix caching output on ROCm with AITER backend. ## Root Cause When shuffle KV cache is enabled via `rocm_aiter_ops.is_shuffle_kv_cache_enabled( |
| [#34878](https://github.com/vllm-project/vllm/pull/34878) | closes_keyword | 0.95 | [ROCm][Test] Fix beam search determinism failures from batch-size-dependent FP divergence and removed wrong marker | fix with: `pytest -s -v tests/samplers/` on MI355 ## Related - #33123 --- Prefix caching produces different output on ROCm due to the same batch-size-dependent FP divergence in a |
| [#35553](https://github.com/vllm-project/vllm/pull/35553) | mentioned | 0.6 | [ROCm][CI] Fix tool use test stability - disable skinny GEMM, prefix caching, eliminate batch variance | o reduce flakiness on ROCm. ## Related - #33493 - #35049 - #35152 - #33123 # Motivation - https://buildkite.com/vllm/amd-ci/builds/5613/steps/canvas?sid=019ca05d-72bb-43d5-b712-05… |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | closes_keyword | 0.95 | [Core] Add --deterministic-prefix-caching for reproducible prefill on ROCm | Fixes #33123. Adds --deterministic-prefix-caching flag that ensures cache-miss and cache-hit prefills produce identical outputs on ROCm (and any backend affected by bf16 GEMM non-d |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
