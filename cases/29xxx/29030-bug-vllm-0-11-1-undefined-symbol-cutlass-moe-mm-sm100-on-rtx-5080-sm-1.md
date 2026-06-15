# vllm-project/vllm#29030: [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0

| 字段 | 值 |
| --- | --- |
| Issue | [#29030](https://github.com/vllm-project/vllm/issues/29030) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0

### Issue 正文摘录

# [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 ## Environment - **vLLM Version**: 0.11.1 - **GPU**: NVIDIA GeForce RTX 5080 (Compute Capability 12.0, 15.5GB VRAM) - **CUDA Version**: 13.0 - **PyTorch Version**: 2.9.0+cu130 - **OS**: Linux (Debian) - **Installation Method**: Built from source with `TORCH_CUDA_ARCH_LIST="8.0 8.6 8.9 9.0 12.0"` ## Bug Description When building vLLM 0.11.1 from source on RTX 5080 (SM 12.0) with CUDA 13.0, the build completes successfully but fails at import time with: ```python ImportError: /path/to/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb ``` Demangled: `cutlass_moe_mm_sm100(at::Tensor&, at::Tensor const&, ...)` ## Root Cause Analysis The bug is in **CMakeLists.txt lines 621-638** (FP4 kernel configuration): ```cmake if(${CMAKE_CUDA_COMPILER_VERSION} VERSION_GREATER_EQUAL 13.0) cuda_archs_loose_intersection(FP4_ARCHS "10.0f;11.0f;12.0f" "${CUDA_ARCHS}") else() cuda_archs_loose_intersection(FP4_ARCHS "10.0a;10.1a;12.0a;12.1a" "${CUDA_ARCHS}") endif() if(${CMAKE_CUDA_COMPILER_VERSION} VERSION_GREATER_EQUAL 12.8 AND FP4_ARCHS) ... list(APPEN...

## 现有链接修复摘要

#24968 [NVFP4] Enable MOE support for SM_120 (RTX 5090)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 stale # [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 ## Environment - **...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 stale # [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 ## Environment - **...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ## Root Cause Analysis The bug is in **CMakeLists.txt lines 621-638** (FP4 kernel configuration): ```cmake if(${CMAKE_CUDA_COMPILER_VERSION} VERSION_GREATER_EQUAL 13.0) cuda_archs_loose_intersection(FP4_ARCHS "10.0f;11....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 stale # [Bug]: vLLM 0.11.1 undefined symbol `cutlass_moe_mm_sm100` on RTX 5080 (SM 12.0) with CUDA 13.0 ## Environment - **...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: archs_loose_intersection(FP4_ARCHS "10.0f;11.0f;12.0f" "${CUDA_ARCHS}") else() cuda_archs_loose_intersection(FP4_ARCHS "10.0a;10.1a;12.0a;12.1a" "${CUDA_ARCHS}") endif() if(${CMAKE_CUDA_COMPILER_VERSION} VERSION_GREATER...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24968](https://github.com/vllm-project/vllm/pull/24968) | mentioned | 0.45 | [NVFP4] Enable MOE support for SM_120 (RTX 5090) | . ## related issues - #28589: sm 12.1 undefined symbol workaround - #24968: pr attempting to add sm_120 moe support (unmerged, has conflicts) - #24921: rtx 5090 nvfp4 moe kernel i… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
