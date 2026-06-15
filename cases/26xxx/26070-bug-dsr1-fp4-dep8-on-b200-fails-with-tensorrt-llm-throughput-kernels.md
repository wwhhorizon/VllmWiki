# vllm-project/vllm#26070: [Bug]: DSR1 FP4 + DEP8 on B200 fails with TensorRT-LLM throughput kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#26070](https://github.com/vllm-project/vllm/issues/26070) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 FP4 + DEP8 on B200 fails with TensorRT-LLM throughput kernels

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-57-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 GPU 7: NVIDIA B200 Nvidia driver version : 580.65.01 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime...

## 现有链接修复摘要

#27439 [Bugfix] Use latency MOE backend as default for Flashinfer and other misc fixes

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: DSR1 FP4 + DEP8 on B200 fails with TensorRT-LLM throughput kernels bug;nvidia ### Your current environment Collecting environment information... ============================== System Info ========================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 64 Versions of relevant libraries ============================== [pip3] flashinfer-python==0.3.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ernels bug;nvidia ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: DSR1 FP4 + DEP8 on B200 fails with TensorRT-LLM throughput kernels bug;nvidia ### Your current environment Collecting environment information... ============================== System Info ========================...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27439](https://github.com/vllm-project/vllm/pull/27439) | closes_keyword | 0.95 | [Bugfix] Use latency MOE backend as default for Flashinfer and other misc fixes | Fixes: #26070 ## Test Plan Test Nemotron for accuracy and llama 3 70B FP4 for accuracy. ## Test Result <details> nvidia/NVIDIA-Nemotron-Nano-9B-v2: Original: ``` TP 2: Evaluating |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
