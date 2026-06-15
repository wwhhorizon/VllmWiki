# vllm-project/vllm#29669: [Bug]: Can't build VLLM wheel using VLLM docker image.

| 字段 | 值 |
| --- | --- |
| Issue | [#29669](https://github.com/vllm-project/vllm/issues/29669) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't build VLLM wheel using VLLM docker image.

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.4.210-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : Nvidia driver version : 570.172.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== Versions of relevant libraries ============================== [pip3] efficientnet_pytorch==0.7.1 [pip3] flashinf...

## 现有链接修复摘要

#29672 [CI/build] Add libraries needed for building VLLM wheel to the test docker image.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: Can't build VLLM wheel using VLLM docker image. bug ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ============================== [pip3] efficientnet_pytorch==0.7.1 [pip3] flashinfer-python==0.5.2 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er image. bug ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: evelopment attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory attention;cuda;kernel;moe;quantization;triton build_error;crash env_d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29672](https://github.com/vllm-project/vllm/pull/29672) | closes_keyword | 0.95 | [CI/build] Add libraries needed for building VLLM wheel to the test docker image. | fixes issue #29669. In pull request #29270 we switched from devel to basic nvidia image as a base for the default and test VLLM docker image. This basic nvidia image doesn't conta |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
