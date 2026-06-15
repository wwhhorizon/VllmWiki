# vllm-project/vllm#5420: [Bug]: Automatic Prefix caching not working while hitting same request multiple times

| 字段 | 值 |
| --- | --- |
| Issue | [#5420](https://github.com/vllm-project/vllm/issues/5420) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Automatic Prefix caching not working while hitting same request multiple times

### Issue 正文摘录

### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.9.16 (main, Oct 26 2023, 03:04:46) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1048-aws-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 535.104.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7R32 Stepping: 0 CPU MHz: 2800.000 BogoMIPS: 5600.00 Hypervisor vendor: KVM Virtualization type: full L1d cache: 64 KiB L1i cache: 64 KiB L2 cache...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ng same request multiple times bug ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 535.104.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Automatic Prefix caching not working while hitting same request multiple times bug ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to bui...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: vllm/assets/44570240/e7e03d73-f13f-426d-8444-a242af9f7ee4) I observe the KV cache is automatically offloaded after the request is done correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
