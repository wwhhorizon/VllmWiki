# vllm-project/vllm#42987: [SM120] _dummy_sampler_run hangs indefinitely on RTX 5090 due to top_k=vocab_size-1 triggering an SM120-broken top-k masking kernel (one-line fix)

| 字段 | 值 |
| --- | --- |
| Issue | [#42987](https://github.com/vllm-project/vllm/issues/42987) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;gemm;kernel;operator;sampling;triton |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [SM120] _dummy_sampler_run hangs indefinitely on RTX 5090 due to top_k=vocab_size-1 triggering an SM120-broken top-k masking kernel (one-line fix)

### Issue 正文摘录

### Summary On physical RTX 5090 hardware (SM120 / compute_120f), `vllm serve` hangs indefinitely during engine startup. The hang is in `_dummy_sampler_run` (called from `profile_run` → `_initialize_kv_caches`) when it invokes the sampler with `top_k = logits.size(1) - 1` (i.e. `vocab_size - 1`, which is **151935** for `Qwen/Qwen2.5-3B-Instruct`). Real production sampling uses small `top_k` values (e.g. 40, 50) and does not hang. Substituting a small `top_k` in the dummy run resolves the startup hang with no functional regression — the dummy sampler exists only for KV-cache memory profiling, where realistic top_k values give an identical memory footprint. ### One-line proposed fix `vllm/v1/worker/gpu_model_runner.py`, in `_dummy_sampler_run`: ```diff - top_k=dummy_tensors(logits.size(1) - 1), + top_k=dummy_tensors(50), ``` (or any small constant in the typical-production range, e.g. 20–100.) I'd be glad to send a PR. Wanted to surface the diagnosis first in case there's a different preferred remediation (e.g. detect SM120 and short-circuit, or fix the underlying kernel). ### Diagnostic evidence (py-spy, captured 2026-05-17 on a real RTX 5090) ``` Thread MainThread (active): "VLLM:...

## 现有链接修复摘要

#43013 [Bugfix] Use realistic top_k in _dummy_sampler_run to avoid SM120 startup hang

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e there's a different preferred remediation (e.g. detect SM120 and short-circuit, or fix the underlying kernel). ### Diagnostic evidence (py-spy, captured 2026-05-17 on a real RTX 5090) ``` Thread MainThread (active): "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: during engine startup. The hang is in `_dummy_sampler_run` (called from `profile_run` → `_initialize_kv_caches`) when it invokes the sampler with `top_k = logits.size(1) - 1` (i.e. `vocab_size - 1`, which is **151935**...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ``` Thread MainThread (active): "VLLM::EngineCore" apply_top_k_top_p_triton (vllm/v1/sample/ops/topk_topp_triton.py:1000) apply_top_k_top_p (vllm/v1/sample/ops/topk_topp_sampler.py:252) forward_native (vllm/v1/sample/op...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [SM120] _dummy_sampler_run hangs indefinitely on RTX 5090 due to top_k=vocab_size-1 triggering an SM120-broken top-k masking kernel (one-line fix) ### Summary On physical RTX 5090 hardware (SM120 / compute_120f), `vllm s
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: thread is stuck inside `cuLaunchKernel → clock_gettime` — a `CUDA_LAUNCH_BLOCKING=1` sync poll waiting for a GPU kernel that **never returns**. The process sits at 100% CPU, GPU at 0% util, allocated memory ~7128 MiB, o...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43013](https://github.com/vllm-project/vllm/pull/43013) | closes_keyword | 0.95 | [Bugfix] Use realistic top_k in _dummy_sampler_run to avoid SM120 startup hang | Fixes #42987. On RTX 5090 (SM120), vllm serve hangs indefinitely during engine startup. As diagnosed in the issue with py-spy, the hang is in _dummy_sampler_run (profile_run → _in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
