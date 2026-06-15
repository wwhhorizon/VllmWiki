# vllm-project/vllm#26558: CUDA illegal memory access in fused_marlin_moe with GLM-4.6-GPTQ MoE model (V1 engine, TP=4)

| 字段 | 值 |
| --- | --- |
| Issue | [#26558](https://github.com/vllm-project/vllm/issues/26558) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA illegal memory access in fused_marlin_moe with GLM-4.6-GPTQ MoE model (V1 engine, TP=4)

### Issue 正文摘录

### Describe the bug CUDA illegal memory access error during model initialization with GLM-4.6-GPTQ-Int4-Int8Mix MoE model when using the V1 engine with tensor parallelism. ### Environment - vLLM version: 0.11.0rc2.dev371+gaafb99a4d.d20251010 - Platform: CUDA 13 (tried 12.8 12.9) - GPU: 4x GPU RTX 6000 pro - Python: 3.12 - PyTorch CUDA version: with nccl==2.27.3 ### Configuration ```bash vllm serve models/GLM-4.6-GPTQ-Int4-Int8Mix \ --trust-remote-code \ --served-model-name GLM-4.6 \ --tensor-parallel-size 4 \ --swap-space 16.0 \ --enable-prefix-caching \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --enable-auto-tool-choice ``` ### Error Traceback The error occurs during the profiling run in `determine_available_memory()`: ```python torch.AcceleratorError: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` **Stack trace:** ``` File "/home/ioplex/vllm/vllm/model_executor/layers/fused_moe/fused_marlin_moe.py", line 243, in fused_...

## 现有链接修复摘要

#26953 Fix GPTQ Marlin MoE mixed precision support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en using the V1 engine with tensor parallelism. ### Environment - vLLM version: 0.11.0rc2.dev371+gaafb99a4d.d20251010 - Platform: CUDA 13 (tried 12.8 12.9) - GPU: 4x GPU RTX 6000 pro - Python: 3.12 - PyTorch CUDA versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: CUDA illegal memory access in fused_marlin_moe with GLM-4.6-GPTQ MoE model (V1 engine, TP=4) stale ### Describe the bug CUDA illegal memory access error during model initialization with GLM-4.6-GPTQ-Int4-Int8Mix MoE mod
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llegal memory access error during model initialization with GLM-4.6-GPTQ-Int4-Int8Mix MoE model when using the V1 engine with tensor parallelism. ### Environment - vLLM version: 0.11.0rc2.dev371+gaafb99a4d.d20251010 - P...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: CUDA illegal memory access in fused_marlin_moe with GLM-4.6-GPTQ MoE model (V1 engine, TP=4) stale ### Describe the bug CUDA illegal memory access error during model initialization with GLM-4.6-GPTQ-Int4-Int8Mix MoE mod...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ;sampling_logits cuda;kernel;moe;quantization;sampling build_error;crash;mismatch dtype;env_dependency;shape #26953 Fix GPTQ Marlin MoE mixed precision support Describe the bug

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26953](https://github.com/vllm-project/vllm/pull/26953) | mentioned | 0.6 | Fix GPTQ Marlin MoE mixed precision support | Q Marlin MoE. <!-- markdownlint-disable --> ## Purpose Resole issue #26558 CUDA illegal memory access in fused_marlin_moe with GLM-4.6-GPTQ MoE model (V1 engine, TP=4) ## Test Plan |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
