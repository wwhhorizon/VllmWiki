# vllm-project/vllm#8460: [Installation]: vLLM Not Working on x86 CPUs from v0.6.1 Onwards

| 字段 | 值 |
| --- | --- |
| Issue | [#8460](https://github.com/vllm-project/vllm/issues/8460) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vLLM Not Working on x86 CPUs from v0.6.1 Onwards

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: 17.0.2 (https://github.com/llvm/llvm-project b2417f51dbbd7435eb3aaf203de24de6754da50e) CMake version: version 3.30.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1023-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8375C CPU @ 2.90GHz CPU family: 6 Model: 106 Thread(s) per core: 2 Core(s) per socket: 8 Socket(s): 1 Stepping: 6 BogoMIPS: 5799.92 Flags: fpu vme de pse tsc msr pae mce cx8...

## 现有链接修复摘要

#8467 [Doc] Add oneDNN installation to CPU backend documentation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: vLLM Not Working on x86 CPUs from v0.6.1 Onwards installation ### Your current environment ```text PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTo
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt environment ```text PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulner...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _error;nan_inf env_dependency #8467 [Doc] Add oneDNN installation to CPU backend documentation Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8467](https://github.com/vllm-project/vllm/pull/8467) | closes_keyword | 0.95 | [Doc] Add oneDNN installation to CPU backend documentation | FIX #8460 (*link existing issues this PR will resolve*) - This PR adds missing oneDNN installation to cpu backend installation instruction. **BEFORE SUBMITTING, PLEASE READ THE |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
