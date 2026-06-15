# vllm-project/vllm#5517: [Bug]: Excessive Memory Consumption of Cudagraph on A10G/L4 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#5517](https://github.com/vllm-project/vllm/issues/5517) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Excessive Memory Consumption of Cudagraph on A10G/L4 GPUs

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.11.7 (main, Dec 15 2023, 18:12:31) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-1020-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G GPU 1: NVIDIA A10G GPU 2: NVIDIA A10G GPU 3: NVIDIA A10G GPU 4: NVIDIA A10G GPU 5: NVIDIA A10G GPU 6: NVIDIA A10G GPU 7: NVIDIA A10G Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: AuthenticAMD Model name: AMD EPYC 7R32 CPU family: 23 Model: 49 Thread(s) per core: 2 Core(s) p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Excessive Memory Consumption of Cudagraph on A10G/L4 GPUs bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: GPUs bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec rstack overflow: Vul...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] _anaconda_depends 2024.02 py311_mkl_1 [conda] blas 1.0 mkl [conda] mkl

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
