# vllm-project/vllm#43507: [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models

| 字段 | 值 |
| --- | --- |
| Issue | [#43507](https://github.com/vllm-project/vllm/issues/43507) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models

### Issue 正文摘录

# [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models ## Summary On consumer Blackwell hardware (NVIDIA RTX 50 series = SM_120, NVIDIA GB10 / DGX Spark = SM_121), vLLM's FP8 MoE backend selector picks `TRITON` instead of `VLLM_CUTLASS` for tensor/token-scaled FP8 models (e.g. `RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic`). This is correct fallback behavior — but the underlying reason is a real upstream gap, not just a configuration mistake. **CUTLASS 4.5 does not ship a `CollectiveBuilder` specialization for tensor/token-scaled FP8 grouped GEMM on SM_120/SM_121.** Investigation on real DGX Spark hardware (2026-05-23) confirms this. Filing this so other GB10/Spark owners stop wasting cycles rebuilding vLLM trying to enable CUTLASS MoE — the path doesn't exist yet at the CUTLASS layer. ## Affected hardware - NVIDIA GB10 (DGX Spark) → SM_121 - NVIDIA RTX 50 series consumer Blackwell → SM_120 - Any future SM_12x consumer Blackwell variant ## Symptom In server logs at startup: ``` INFO [fp8.py:405] Using TRITON Fp8 MoE backend out of potential backends: [AITER, FLASHINFER_TRTLLM, FLASHINFER_CUTLASS, DEEPGEMM, VLLM_CUTLA...

## 现有链接修复摘要

#32237 [Fix][MoE] Add SM120 support for FP8 MoE path | #43730 [Bugfix] Fix CUDA illegal memory access in Marlin MoE c_tmp on SM 12.0a (re-file of #36889) | #43814 [Bugfix][SM120] Enable CUTLASS grouped GEMM (MoE) for SM_120/SM_121 consumer Blackwell

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models # [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models # [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t just a configuration mistake. **CUTLASS 4.5 does not ship a `CollectiveBuilder` specialization for tensor/token-scaled FP8 grouped GEMM on SM_120/SM_121.** Investigation on real DGX Spark hardware (2026-05-23) confirm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: lable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models # [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models ##...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for tensor/token-scaled FP8 models # [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Blackwell / DGX Spark) for te...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32237](https://github.com/vllm-project/vllm/pull/32237) | mentioned | 0.45 | [Fix][MoE] Add SM120 support for FP8 MoE path | \| result \| \|---\|---\| \| `kernelptrarraytmawarpspecialized1smsm120` (pr #32237's choice) \| ❌ symbol does not exist in cutlass 4.5 (was a pre-release name) \| \| `kernelschedulesm120bl… |
| [#43730](https://github.com/vllm-project/vllm/pull/43730) | mentioned | 0.6 | [Bugfix] Fix CUDA illegal memory access in Marlin MoE c_tmp on SM 12.0a (re-file of #36889) | y on RTX PRO 6000 Blackwell Server Edition under the workload class [`#43507`](https://github.com/vllm-project/vllm/issues/43507) + [`jasl/vllm#12`](https://github.com/jasl/vllm/i… |
| [#43814](https://github.com/vllm-project/vllm/pull/43814) | closes_keyword | 0.95 | [Bugfix][SM120] Enable CUTLASS grouped GEMM (MoE) for SM_120/SM_121 consumer Blackwell | Fixes #43507. --- ## What changed ### Bug 1 — Python gate (`vllm/_custom_ops.py`) ```python # Before (wrong): if cuda_device_capability < 90 or cuda_device_capability >= 110: |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
