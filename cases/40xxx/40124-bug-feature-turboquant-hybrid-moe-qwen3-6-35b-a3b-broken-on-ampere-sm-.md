# vllm-project/vllm#40124: [Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes

| 字段 | 值 |
| --- | --- |
| Issue | [#40124](https://github.com/vllm-project/vllm/issues/40124) |
| 状态 | open |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;quantization;sampling;triton |
| 症状 | crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes

### Issue 正文摘录

## Summary TurboQuant KV cache (`k8v4`) combined with **hybrid MoE models** (Qwen3.6-35B-A3B-FP8 — 30 MoE + 10 dense layers, E=256, top_k=8, `block_shape=[128,128]`) **does not work on Ampere GPUs** (SM 80-86). Multiple code paths assume Hopper+ (SM ≥ 89) and hybrid model geometry is not handled correctly. We have identified and fixed 13 issues, packaged as a runtime monkey-patch applied at container startup. All patches are available as open source: **Repository: https://github.com/Sandermage/genesis-vllm-patches** ## Environment - **vLLM**: `0.19.1rc1` nightly (`vllm/vllm-openai:nightly` as of 2026-04-16) - **GPUs**: 2× NVIDIA RTX A5000 24 GB (SM86, Ampere), `tensor_parallel_size=2` - **Model**: `Qwen/Qwen3-35B-A3B-FP8` — hybrid MoE, `block_shape=[128,128]` - **Config**: `kv_cache_dtype=turboquant_k8v4`, `max_model_len=163840`, `gpu_memory_utilization=0.905` - **Driver**: NVIDIA 570.211.01, CUDA 12.8 ## Issues Found (13 patches) ### Critical — Model fails to run on Ampere without these | # | Issue | Related PR | |---|-------|-----------| | 1 | `TritonBlockFP8ScaledMM` uses `fp8e4nv` which requires SM ≥ 89 → silent compute errors on Ampere | — | | 2 | Kernel selector picks Triton...

## 现有链接修复摘要

#29354 Add unpermute-aware fused MoE path and small-batch fallback | #39016 [MoE] Triton MoE Perf regression - restore low latency path | #39391 fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs | #39748 [Perf] Re-enable dual-stream input projection for Qwen3/Qwen3.5 GDN | #39931 [Feature] TurboQuant: support hybrid models and uniform quantization | #39988 [Bugfix] Fix turboquant FP8 cast failure for BF16 models on Ampere GPUs | #40384 [Bugfix] Exclude O(1) Mamba groups from hybrid KV cache token capacity

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes ## Summary TurboQuant KV cache (`k8v4`) combined with **hybrid MoE models** (Qwen3.6-35B-A3B-FP8 — 30 MoE + 10...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: thout these | # | Issue | Related PR | |---|-------|-----------| | 1 | `TritonBlockFP8ScaledMM` uses `fp8e4nv` which requires SM ≥ 89 → silent compute errors on Ampere | — | | 2 | Kernel selector picks Triton for block...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes ## Summary TurboQuant KV cache (`k8v4`) combined with **hybrid MoE models** (Qwen3.6-35B-A3B-FP8 — 30 MoE + 10...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes ## Summary TurboQuant KV cache (`k8v4`) combined with **hybrid MoE models** (Qwen3.6-35B-A3B-FP8 — 30 MoE + 10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes ## Summary TurboQuant KV cache (`k8v4`) combined with **hybrid MoE models** (Qwen3.6-35B-A3B-FP8 — 30 MoE + 10...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29354](https://github.com/vllm-project/vllm/pull/29354) | mentioned | 0.45 | Add unpermute-aware fused MoE path and small-batch fallback | \| **+8% decode** \| \| 10 \| `naive_block_assignment` for moe \| #39016 / #29354 \| **+3-5% decode** \| \| 11 \| tuned triton moe kernel configs for a5000 \| original \| **-8% to -16.5% ker… |
| [#39016](https://github.com/vllm-project/vllm/pull/39016) | mentioned | 0.45 | [MoE] Triton MoE Perf regression - restore low latency path | several of these fixes overlap with open prs (#39931, #39988, #39748, #39016, #39391, #35687). the ampere-specific fp8 issues (patches 1, 2, 5) and the tuned triton configs (patch… |
| [#39391](https://github.com/vllm-project/vllm/pull/39391) | mentioned | 0.45 | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs | of these fixes overlap with open prs (#39931, #39988, #39748, #39016, #39391, #35687). the ampere-specific fp8 issues (patches 1, 2, 5) and the tuned triton configs (patch 11) are… |
| [#39748](https://github.com/vllm-project/vllm/pull/39748) | mentioned | 0.45 | [Perf] Re-enable dual-stream input projection for Qwen3/Qwen3.5 GDN | action several of these fixes overlap with open prs (#39931, #39988, #39748, #39016, #39391, #35687). the ampere-specific fp8 issues (patches 1, 2, 5) and the tuned triton configs… |
| [#39931](https://github.com/vllm-project/vllm/pull/39931) | mentioned | 0.45 | [Feature] TurboQuant: support hybrid models and uniform quantization | 4 ## suggested action several of these fixes overlap with open prs (#39931, #39988, #39748, #39016, #39391, #35687). the ampere-specific fp8 issues (patches 1, 2, 5) and the tuned… |
| [#39988](https://github.com/vllm-project/vllm/pull/39988) | mentioned | 0.45 | [Bugfix] Fix turboquant FP8 cast failure for BF16 models on Ampere GPUs | ggested action several of these fixes overlap with open prs (#39931, #39988, #39748, #39016, #39391, #35687). the ampere-specific fp8 issues (patches 1, 2, 5) and the tuned triton… |
| [#40384](https://github.com/vllm-project/vllm/pull/40384) | mentioned | 0.6 | [Bugfix] Exclude O(1) Mamba groups from hybrid KV cache token capacity | entification and filter design credit to @Sandermage — ref his [issue #40124 tracking table](https://github.com/vllm-project/vllm/issues/40124) (patch 9) and the `ai-jz/vllm#1` ap… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
