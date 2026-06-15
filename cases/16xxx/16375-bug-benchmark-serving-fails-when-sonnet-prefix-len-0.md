# vllm-project/vllm#16375: [Bug]: Benchmark_serving fails when --sonnet-prefix-len=0

| 字段 | 值 |
| --- | --- |
| Issue | [#16375](https://github.com/vllm-project/vllm/issues/16375) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Benchmark_serving fails when --sonnet-prefix-len=0

### Issue 正文摘录

### Your current environment PyTorch version: 2.8.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 Python version: 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-1015-gcp-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 44 On-line CPU(s) list: 0-43 Vendor ID: AuthenticAMD Model name: AMD EPYC 9B14 CPU family: 25 Model: 17 Thread(s) per core: 2 Core(s) per socket: 22 Socket(s): 1 Stepping: 1 BogoMIPS: 5199.99 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ils when --sonnet-prefix-len=0 bug ### Your current environment PyTorch version: 2.8.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: # Your current environment PyTorch version: 2.8.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation;...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Benchmark_serving fails when --sonnet-prefix-len=0 bug ### Your current environment PyTorch version: 2.8.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
