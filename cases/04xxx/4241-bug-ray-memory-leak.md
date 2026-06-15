# vllm-project/vllm#4241: [Bug]: Ray memory leak

| 字段 | 值 |
| --- | --- |
| Issue | [#4241](https://github.com/vllm-project/vllm/issues/4241) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ray memory leak

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.11.3 (main, Apr 19 2024, 17:22:27) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.4.0-177-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 40 bits physical, 48 bits virtual CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 1 Core(s) per socket: 1 Socket(s): 64 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC-Milan Processor Stepping: 1 CPU MHz: 2994.374 BogoMIPS: 5988.74 Virtualization: AMD-V Hypervisor ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: memory leak bug;ray;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 Nvidia driver version: 535.161.08 cuDNN version: Could not collect...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: m running on a multi-GPU setup. After each model run I need to clear the GPU memory to leave room for the next model, which means (among other things) that I need to shut down the Ray cluster (via `ray.shutdown()`). Tha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Ray memory leak bug;ray;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
