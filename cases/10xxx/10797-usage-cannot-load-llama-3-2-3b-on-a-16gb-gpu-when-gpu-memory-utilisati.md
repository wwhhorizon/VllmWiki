# vllm-project/vllm#10797: [Usage]: cannot load llama 3.2 3b on a 16gb gpu when gpu_memory_utilisation=1

| 字段 | 值 |
| --- | --- |
| Issue | [#10797](https://github.com/vllm-project/vllm/issues/10797) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: cannot load llama 3.2 3b on a 16gb gpu when gpu_memory_utilisation=1

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.10 (x86_64) GCC version: (Ubuntu 14.2.0-4ubuntu2) 14.2.0 Clang version: 19.1.1 (1ubuntu1) CMake version: version 3.30.3 Libc version: glibc-2.40 Python version: 3.12.7 (main, Nov 6 2024, 18:29:01) [GCC 14.2.0] (64-bit runtime) Python platform: Linux-6.11.0-9-generic-x86_64-with-glibc2.40 Is CUDA available: True CUDA runtime version: 12.6.77 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4080 Nvidia driver version: 565.57.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: AuthenticAMD Model name: AMD Ryzen 9 7950X 16-Core Processor CPU family: 25 Model: 97 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 2 Frequency boost: enabled CPU(s) scaling MHz: 67% CPU max MHz: 5881.0000 CPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.10 (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.10 (x86_64) GCC version: (Ubuntu 14.2.0-4ubuntu2) 14.2.0 Clang vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: cannot load llama 3.2 3b on a 16gb gpu when gpu_memory_utilisation=1 usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUD...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: nnot load llama 3.2 3b on a 16gb gpu when gpu_memory_utilisation=1 usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: g model weights took 3.2636 GB INFO 11-30 13:57:06 worker.py:232] Memory profiling results: total_gpu_memory=15.56GiB initial_memory_usage=4.78GiB peak_torch_memory=4.43GiB memory_usage_post_profile=4.78GiB non_torch_me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
