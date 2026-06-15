# vllm-project/vllm#33416: [Bug] NVFP4 MoE kernels fail on RTX Blackwell (SM12.0) - device capability family check missing SM120

| 字段 | 值 |
| --- | --- |
| Issue | [#33416](https://github.com/vllm-project/vllm/issues/33416) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] NVFP4 MoE kernels fail on RTX Blackwell (SM12.0) - device capability family check missing SM120

### Issue 正文摘录

## Bug Description vLLM v0.15.0 fails to run NVFP4 quantized MoE models on RTX Blackwell GPUs (compute capability 12.0, e.g., RTX PRO 6000 Blackwell Workstation Edition). The NVFP4 MoE backend selection code only checks for SM9.0 (Hopper) and SM10.x family (data center Blackwell B100/B200), but not SM12.0 (RTX Blackwell). ## Error Message ``` ValueError: NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device. ``` ## Root Cause The device capability checks in the NVFP4 MoE backend selection code use `is_device_capability_family(100)` which only matches SM10.x: ```python # Current code - only checks family 100 (SM10.x) current_platform.is_device_capability_family(100) ``` RTX Blackwell GPUs have compute capability 12.0 (SM120), which returns: - `is_device_capability_family(100)` → **False** (120 // 10 = 12 ≠ 100 // 10 = 10) - `has_device_capability(100)` → **True** (120 >= 100) RTX Blackwell (SM12.0) shares the same native FP4/FP8 tensor core capabilities as data center Blackwell (SM10.0), so these kernels should work on both families. ## Affected Files - `vllm/model_executor/layers/fused_moe/flashinfer_cutla...

## 现有链接修复摘要

#33417 fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels | #36453 fix: Add SM120 capability family check for FlashInfer NVFP4 MoE backends

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug] NVFP4 MoE kernels fail on RTX Blackwell (SM12.0) - device capability family check missing SM120 ## Bug Description vLLM v0.15.0 fails to run NVFP4 quantized MoE models on RTX Blackwell GPUs (compute capability 12....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug] NVFP4 MoE kernels fail on RTX Blackwell (SM12.0) - device capability family check missing SM120 ## Bug Description vLLM v0.15.0 fails to run NVFP4 quantized MoE models on RTX Blackwell GPUs (compute capability 12....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: y 12.0, e.g., RTX PRO 6000 Blackwell Workstation Edition). The NVFP4 MoE backend selection code only checks for SM9.0 (Hopper) and SM10.x family (data center Blackwell B100/B200), but not SM12.0 (RTX Blackwell). ## Erro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: U**: NVIDIA RTX PRO 6000 Blackwell Workstation Edition (SM12.0) - **vLLM Version**: v0.15.0 - **Model**: MiniMax-M2.1-NVFP4 - **CUDA**: 13.0.2 - **Driver**: 580.126.09 ## Steps to Reproduce 1. Run vLLM v0.15.0 on an RTX...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: SM120 ## Bug Description vLLM v0.15.0 fails to run NVFP4 quantized MoE models on RTX Blackwell GPUs (compute capability 12.0, e.g., RTX PRO 6000 Blackwell Workstation Edition). The NVFP4 MoE backend selection code only...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33417](https://github.com/vllm-project/vllm/pull/33417) | closes_keyword | 0.95 | fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels | Fixes #33416 --- ## For Maintainers This is a regression bugfix affecting NVFP4 MoE models on RTX Blackwell GPUs (SM12.0). Please consider cherry-picking this to `releases/v0.15 |
| [#36453](https://github.com/vllm-project/vllm/pull/36453) | closes_keyword | 0.95 | fix: Add SM120 capability family check for FlashInfer NVFP4 MoE backends | Closes #33416, #33333 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
