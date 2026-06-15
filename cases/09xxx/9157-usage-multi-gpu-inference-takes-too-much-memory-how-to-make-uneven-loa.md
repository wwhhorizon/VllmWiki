# vllm-project/vllm#9157: [Usage]: Multi-gpu inference takes too much memory + how to make uneven load

| 字段 | 值 |
| --- | --- |
| Issue | [#9157](https://github.com/vllm-project/vllm/issues/9157) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Multi-gpu inference takes too much memory + how to make uneven load

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.3 LTS (x86_64) GCC version: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.12.6 | packaged by Anaconda, Inc. | (main, Oct 3 2024, 07:30:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-84-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4060 Ti GPU 1: NVIDIA GeForce RTX 4060 Ti Nvidia driver version: 560.28.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 48 On-line CPU(s) list: 0-47 Thread(s) per core: 2 Core(s) per socket: 12 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 79 Model name: Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz Stepping: 1 CPU MHz: 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ke uneven load usage;stale ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.3 LTS (x86_64) GCC version: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4060 Ti GPU 1: NVIDIA GeForce RTX 4060 Ti Nvidia driver version: 560.28.03 cuDNN version: Could...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ulti-gpu inference takes too much memory + how to make uneven load usage;stale ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.45.1 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
