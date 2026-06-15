# vllm-project/vllm#5424: [Bug]: CUDA out of memory when setting prompt_logprobs with larger batch_size

| 字段 | 值 |
| --- | --- |
| Issue | [#5424](https://github.com/vllm-project/vllm/issues/5424) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA out of memory when setting prompt_logprobs with larger batch_size

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-182-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe Nvidia driver version: 535.171.04 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 256 On-line CPU(s) list: 0-255 Thread(s) per core: 2 Core(s) per socket: 64 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7713 64-Core Processor Stepping: 1 Frequency boost: enabled CPU MHz: 1499....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: CUDA out of memory when setting prompt_logprobs with larger batch_size bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: DA out of memory when setting prompt_logprobs with larger batch_size bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
