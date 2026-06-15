# vllm-project/vllm#30707: [Bug]: RTX 5080 (SM120) + NVFP4 model fails pre-flight memory check despite model fitting in VRAM

| 字段 | 值 |
| --- | --- |
| Issue | [#30707](https://github.com/vllm-project/vllm/issues/30707) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;kernel;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: RTX 5080 (SM120) + NVFP4 model fails pre-flight memory check despite model fitting in VRAM

### Issue 正文摘录

## Summary vLLM 0.12.0 V1 engine fails to load a 14GB NVFP4-quantized model on RTX 5080 16GB due to overly aggressive pre-flight memory validation. The same model loads successfully with llama.cpp (GGUF Q4_K_M format), proving the model fits in VRAM. ## Environment - **GPU**: NVIDIA GeForce RTX 5080 (16GB VRAM, SM120/Blackwell) - **Driver**: 591.44 - **CUDA**: 13.0 (required for SM120 support) - **vLLM**: 0.12.0 - **OS**: Ubuntu 22.04 (WSL2) - **Model**: Qwen3-Coder-REAP-25B-NVFP4-v2 (14GB, compressed-tensors quantization) ## Issue Description ### What happens: 1. Model weights load successfully (14.0 GiB, ~90 seconds) 2. V1 engine performs memory validation check 3. Check fails because `gpu_memory_utilization * total_memory` exceeds free memory 4. Server crashes before attempting to allocate KV cache ### Error 1 - Initial startup check (gpu_memory_utilization=0.92): ``` ValueError: Free memory on device (14.55/15.92 GiB) on startup is less than desired GPU memory utilization (0.92, 14.65 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. ``` ### Error 2 - After model loads (gpu_memory_utilization=0.95): ``` INFO: Model loading took 14.0036 GiB mem...

## 现有链接修复摘要

#24968 [NVFP4] Enable MOE support for SM_120 (RTX 5090)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: RTX 5080 (SM120) + NVFP4 model fails pre-flight memory check despite model fitting in VRAM ## Summary vLLM 0.12.0 V1 engine fails to load a 14GB NVFP4-quantized model on RTX 5080 16GB due to overly aggressive pre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: supported gpu architecture 'compute_120a'`) - FlashInfer CUTLASS kernels compile successfully with CUDA 13.0 - The 14GB model + 2GB KV cache SHOULD fit in 16GB, but validation prevents attempting it performance attentio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: RTX 5080 (SM120) + NVFP4 model fails pre-flight memory check despite model fitting in VRAM ## Summary vLLM 0.12.0 V1 engine fails to load a 14GB NVFP4-quantized model on RTX 5080 16GB due to overly aggressive pre...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: RTX 5080 (SM120) + NVFP4 model fails pre-flight memory check despite model fitting in VRAM ## Summary vLLM 0.12.0 V1 engine fails to load a 14GB NVFP4-quantized model on RTX 5080 16GB due to overly aggressive pre...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ory` exceeds free memory 4. Server crashes before attempting to allocate KV cache ### Error 1 - Initial startup check (gpu_memory_utilization=0.92): ``` ValueError: Free memory on device (14.55/15.92 GiB) on startup is...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24968](https://github.com/vllm-project/vllm/pull/24968) | mentioned | 0.45 | [NVFP4] Enable MOE support for SM_120 (RTX 5090) | m on rtx5080/5090 - #21097 - w8a8 quantization not supporting sm120 - #24968 - nvfp4 moe support for sm_120 ## additional context - rtx 5080/5090 (blackwell/sm120) is bleeding-edg… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
