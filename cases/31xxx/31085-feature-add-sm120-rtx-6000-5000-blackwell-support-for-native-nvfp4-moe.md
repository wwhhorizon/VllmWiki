# vllm-project/vllm#31085: [Feature]: Add SM120 (RTX 6000/5000 Blackwell) support for native NVFP4 MoE kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#31085](https://github.com/vllm-project/vllm/issues/31085) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;quantization;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add SM120 (RTX 6000/5000 Blackwell) support for native NVFP4 MoE kernels

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary SM120 (RTX 6000 Pro Blackwell, compute capability 12.0) is not recognized in the MXFP4 backend selection logic, causing fallback to Marlin instead of using native NVFP4 kernels. ## Environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX 6000 Pro (Blackwell, SM120a) - Compute Capability: (12, 0) - Model: gpt-oss-120b (MXFP4 quantization) ## Current Behavior Startup log shows: WARNING [marlin_utils_fp4.py:226] Your GPU does not have native support for FP4 computation but FP4 quantization is being used. Weight-only FP4 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-heavy workloads. And: INFO [mxfp4.py:161] Using Marlin backend ## Root Cause The MXFP4 backend selection in `vllm/model_executor/layers/quantization/mxfp4.py` only checks for SM100 family: ```python # Line 121-126 elif ( current_platform.is_device_capability_family(100) # Only matches SM10x and has_flashinfer() ... ``` SM120 ((12, 0)) doesn't match is_device_capability_family(100) since it's a different major version. Similarly, the Triton backend check excludes SM120: Line 96: `and (9, 0) csrc/quantization/fp4/nvfp4_scaled_mm_...

## 现有链接修复摘要

#33516 [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 0 Pro Blackwell, compute capability 12.0) is not recognized in the MXFP4 backend selection logic, causing fallback to Marlin instead of using native NVFP4 kernels. ## Environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Feature]: Add SM120 (RTX 6000/5000 Blackwell) support for native NVFP4 MoE kernels feature request;unstale ### 🚀 The feature, motivation and pitch ## Summary SM120 (RTX 6000 Pro Blackwell, compute capability 12.0) is n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: Add SM120 (RTX 6000/5000 Blackwell) support for native NVFP4 MoE kernels feature request;unstale ### 🚀 The feature, motivation and pitch ## Summary SM120 (RTX 6000 Pro Blackwell, compute capability 12.0) is n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: to Marlin instead of using native NVFP4 kernels. ## Environment - vLLM version: 0.13.0 - GPU: NVIDIA RTX 6000 Pro (Blackwell, SM120a) - Compute Capability: (12, 0) - Model: gpt-oss-120b (MXFP4 quantization) ## Current B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: NVIDIA RTX 6000 Pro (Blackwell, SM120a) - Compute Capability: (12, 0) - Model: gpt-oss-120b (MXFP4 quantization) ## Current Behavior Startup log shows: WARNING [marlin_utils_fp4.py:226] Your GPU does not have native sup...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33516](https://github.com/vllm-project/vllm/pull/33516) | closes_keyword | 0.95 | [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends | Fixes #31085 Fixes #30135 Fixes #29141 Related to #28589 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
