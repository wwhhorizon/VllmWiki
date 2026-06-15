# vllm-project/vllm#43906: [Bug] MXFP8 MoE always falls back to MARLIN on SM_121 (DGX Spark / GB10): TrtLlmFp8ExpertsBase gates on family(100), excluding SM_12x consumer Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#43906](https://github.com/vllm-project/vllm/issues/43906) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization |
| 症状 | build_error;import_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] MXFP8 MoE always falls back to MARLIN on SM_121 (DGX Spark / GB10): TrtLlmFp8ExpertsBase gates on family(100), excluding SM_12x consumer Blackwell

### Issue 正文摘录

## Summary On NVIDIA GB10 / DGX Spark (SM_121) serving a `modelopt_mxfp8` checkpoint, the MXFP8 MoE backend selector skips `FLASHINFER_TRTLLM` and falls back to `MARLIN` W8A16. MoE expert weights are dequantized to BF16 before compute, losing the block-32 MX FP8 precision and significant throughput from the native Blackwell `tcgen05.mma` MX path. This is distinct from #43507 which covers `VLLM_CUTLASS` MoE for tensor/token-scaled FP8-Dynamic models. This issue is specifically about the `FLASHINFER_TRTLLM` backend path for **MXFP8 (OCP block-32 MX)** models. ## Affected hardware - NVIDIA GB10 / DGX Spark → SM_121 - NVIDIA RTX 5000-series consumer Blackwell → SM_120 - Any SM_12x consumer/prosumer Blackwell variant ## Affected model - `modelopt_mxfp8` checkpoints (OCP MX FP8 E4M3, block-32 weight + activation scales) - Confirmed on: `gemma-4-26B-A4B` MoE architecture ## Symptom At startup, the engine selects MARLIN instead of FLASHINFER_TRTLLM: ``` INFO [mxfp8.py:88] Using 'MARLIN' MxFp8 MoE backend. ``` ## Root cause — precise diagnosis ### 1. Device family check in `TrtLlmFp8ExpertsBase._supports_current_device()` ```python # vllm/model_executor/layers/fused_moe/modular_kernel.py (...

## 现有链接修复摘要

#40082 Integrate flashinfer b12x MoE and FP4 GEMM kernels for SM120/121

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug] MXFP8 MoE always falls back to MARLIN on SM_121 (DGX Spark / GB10): TrtLlmFp8ExpertsBase gates on family(100), excluding SM_12x consumer Blackwell ## Summary On NVIDIA GB10 / DGX Spark (SM_121) serving a `modelopt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug] MXFP8 MoE always falls back to MARLIN on SM_121 (DGX Spark / GB10): TrtLlmFp8ExpertsBase gates on family(100), excluding SM_12x consumer Blackwell ## Summary On NVIDIA GB10 / DGX Spark (SM_121) serving a `modelopt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ts are dequantized to BF16 before compute, losing the block-32 MX FP8 precision and significant throughput from the native Blackwell `tcgen05.mma` MX path. This is distinct from #43507 which covers `VLLM_CUTLASS` MoE fo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: DGX Spark (SM_121) serving a `modelopt_mxfp8` checkpoint, the MXFP8 MoE backend selector skips `FLASHINFER_TRTLLM` and falls back to `MARLIN` W8A16. MoE expert weights are dequantized to BF16 before compute, losing the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mer Blackwell ## Summary On NVIDIA GB10 / DGX Spark (SM_121) serving a `modelopt_mxfp8` checkpoint, the MXFP8 MoE backend selector skips `FLASHINFER_TRTLLM` and falls back to `MARLIN` W8A16. MoE expert weights are dequa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40082](https://github.com/vllm-project/vllm/pull/40082) | mentioned | 0.45 | Integrate flashinfer b12x MoE and FP4 GEMM kernels for SM120/121 | 8 (different backend/quant format, same hardware exclusion pattern) - #40082 — sm_121 flashinfer + cutlass-dsl support for non-moe linear layers (the fix that *did* work for linea… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
