# vllm-project/vllm#10179: [Installation]:  error: identifier "__builtin_dynamic_object_size" is undefined 

| 字段 | 值 |
| --- | --- |
| Issue | [#10179](https://github.com/vllm-project/vllm/issues/10179) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  error: identifier "__builtin_dynamic_object_size" is undefined 

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 11.4.0-9ubuntu1) 11.4.0 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.39 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-41-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 Nvidia driver version: 550.100 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 43 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: AuthenticAMD Model name: AMD EPYC 7K62 48-Core Processor CPU family: 23 Model: 49 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 1 Stepping: 0 Frequency boost: enabled CPU(s) scaling MHz: 64% CPU max MHz: 2600.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: error: identifier "__builtin_dynamic_object_size" is undefined installation;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0 Is debug build: False CUDA
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment information... PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 11.4.0-9ubuntu1) 11.4.0 Clang v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: llation;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: r: identifier "__builtin_dynamic_object_size" is undefined installation;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: torch==2.4.0 [pip3] torchaudio==2.4.0 [pip3] torchvision==0.19.0 [pip3] triton==3.0.0 [conda] blas 1.0 mkl [conda] cuda-cudart 12.1.105 0 nvidia [conda] cuda-cupti 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
