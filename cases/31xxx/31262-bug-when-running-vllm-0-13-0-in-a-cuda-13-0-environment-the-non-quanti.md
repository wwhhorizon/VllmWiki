# vllm-project/vllm#31262: [Bug]: When running vLLM 0.13.0 in a CUDA 13.0 environment, the non-quantized version of the MoE model works without issues, but the FP8 quantized version fails to run.

| 字段 | 值 |
| --- | --- |
| Issue | [#31262](https://github.com/vllm-project/vllm/issues/31262) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When running vLLM 0.13.0 in a CUDA 13.0 environment, the non-quantized version of the MoE model works without issues, but the FP8 quantized version fails to run.

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:16:04) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-87-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B300 SXM6 AC GPU 1: NVIDIA B300 SXM6 AC GPU 2: NVIDIA B300 SXM6 AC GPU 3: NVIDIA B300 SXM6 AC GPU 4: NVIDIA B300 SXM6 AC GPU 5: NVIDIA B300 SXM6 AC GPU 6: NVIDIA B300 SXM6 AC GPU 7: NVIDIA B300 SXM6 AC Nvidia driver v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : When running vLLM 0.13.0 in a CUDA 13.0 environment, the non-quantized version of the MoE model works without issues, but the FP8 quantized version fails to run. bug ### Your current environment Collecting environment...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 0.13.0 in a CUDA 13.0 environment, the non-quantized version of the MoE model works without issues, but the FP8 quantized version fails to run. bug ### Your current environment Collecting environment information... ====...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.0.0.19 [pip3] nvidia-cuda-cupti==13.0.48 [pip3] nvidia-cuda-nvrtc==13.0.48 [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: When running vLLM 0.13.0 in a CUDA 13.0 environment, the non-quantized version of the MoE model works without issues, but the FP8 quantized version fails to run. bug ### Your current environment Collecting enviro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
