# vllm-project/vllm#3839: [Bug]: Error happen in async_llm_engine when use multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3839](https://github.com/vllm-project/vllm/issues/3839) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error happen in async_llm_engine when use multiple GPUs

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.11.8 (main, Feb 26 2024, 21:39:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 GPU 4: NVIDIA RTX A6000 GPU 5: NVIDIA RTX A6000 GPU 6: NVIDIA RTX A6000 GPU 7: NVIDIA RTX A6000 Nvidia driver version: 535.161.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 43 bits physical, 48 bits virtual CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: se multiple GPUs bug;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 GPU 4: NVIDIA RTX A6000...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Error happen in async_llm_engine when use multiple GPUs bug;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
