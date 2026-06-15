# vllm-project/vllm#4438: [Bug]: Prefix caching does not work on Pascal GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#4438](https://github.com/vllm-project/vllm/issues/4438) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix caching does not work on Pascal GPUs

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Arch Linux (x86_64) GCC version: (GCC) 13.2.1 20230801 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.39 Python version: 3.11.8 (main, Feb 12 2024, 14:50:05) [GCC 13.2.1 20230801] (64-bit runtime) Python platform: Linux-6.7.8-arch1-1-x86_64-with-glibc2.39 Is CUDA available: N/A CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: Tesla P40 GPU 1: Tesla P40 Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 6 On-line CPU(s) list: 0-5 Vendor ID: AuthenticAMD Model name: AMD Ryzen 5 5600 6-Core Processor CPU family: 25 Model: 33 Thread(s) per core: 1 Core(s) per socket: 1 Socket(s): 6 Stepping: 2 BogoMIPS: 6989.99 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Arch Linux (x86_64) GCC version: (GCC) 13.2.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Arch Linux (x86_64) GCC version: (GCC) 13.2.1 20230801 Clang version: Could no...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: GPUs bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Arch Linux (x86_64) GCC ve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Vulnerable: Safe RET, no microcode Vulnerability Spec store...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: cent call first): File "/mnt/ml/vllm/venv/lib/python3.11/site-packages/triton/compiler/compiler.py", line 200 in llir_to_ptx File "/mnt/ml/vllm/venv/lib/python3.11/site-packages/triton/compiler/compiler.py", line 381 in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
