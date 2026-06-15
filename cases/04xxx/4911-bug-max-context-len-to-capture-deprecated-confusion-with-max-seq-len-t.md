# vllm-project/vllm#4911: [Bug]: `max_context_len_to_capture` deprecated, confusion with `max_seq_len_to_capture`

| 字段 | 值 |
| --- | --- |
| Issue | [#4911](https://github.com/vllm-project/vllm/issues/4911) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `max_context_len_to_capture` deprecated, confusion with `max_seq_len_to_capture`

### Issue 正文摘录

### Your current environment PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.2 | packaged by Anaconda, Inc. | (main, Feb 27 2024, 17:35:02) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1063-azure-x86_64-with-glibc2.35 Is CUDA available: N/A CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD Model name: AMD EPYC 7V13 64-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 1 Core(s) per socket: 48 Socket(s): 1 Stepping: 1 BogoMIPS: 4890.88 Flags: fpu vme de pse tsc msr pae mce cx8 apic s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: with `max_seq_len_to_capture` bug ### Your current environment PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubunt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: g ### Your current environment PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : N/A CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 535.161.08 cuDNN version: Could not col...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; safe RET, no microcode Vulnerability Spec store...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
