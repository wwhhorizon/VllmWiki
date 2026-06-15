# vllm-project/vllm#9371: [Bug]: process killed when I set tp>1 for running benchmark_throughput.py

| 字段 | 值 |
| --- | --- |
| Issue | [#9371](https://github.com/vllm-project/vllm/issues/9371) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: process killed when I set tp>1 for running benchmark_throughput.py

### Issue 正文摘录

### Your current environment CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.2.0 24292 26466ce804ac523b398608f17388eb6d605a3f09) CMake version: version 3.26.4 Libc version: glibc-2.31 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-173-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI250X/MI250 (gfx90a:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.2.41133 MIOpen runtime version: 3.2.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 32 On-line CPU(s) list: 0-31 Thread(s) per core: 1 Core(s) per socket: 16 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 73F3 16-Core Processo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: hmark_throughput.py bug;stale ### Your current environment CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: running benchmark_throughput.py bug;stale ### Your current environment CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : process killed when I set tp>1 for running benchmark_throughput.py bug;stale ### Your current environment CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 20.04.6 LTS (x86_64)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI250X/MI250 (gfx90a:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not coll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: process killed when I set tp>1 for running benchmark_throughput.py bug;stale ### Your current environment CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 20.04.6 LTS (x8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
