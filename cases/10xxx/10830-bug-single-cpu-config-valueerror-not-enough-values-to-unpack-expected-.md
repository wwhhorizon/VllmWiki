# vllm-project/vllm#10830: [Bug]: [single CPU][config] ValueError: not enough values to unpack (expected 2, got 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#10830](https://github.com/vllm-project/vllm/issues/10830) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [single CPU][config] ValueError: not enough values to unpack (expected 2, got 1)

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.1 Libc version: glibc-2.35 Python version: 3.10.15 | packaged by conda-forge | (main, Oct 16 2024, 01:24:24) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 384 On-line CPU(s) list: 0-383 Vendor ID: GenuineIntel Model name: GENUINE INTEL(R) XEON(R) CPU family: 6 Model: 173 Thread(s) per core: 2 Core(s) per socket: 96 Socket(s): 2 Stepping: 0 CPU max MHz: 2700.0000 CPU min MHz: 800.0000 BogoMIPS: 4000.00 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: to unpack (expected 2, got 1) bug ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: [single CPU][config] ValueError: not enough values to unpack (expected 2, got 1) bug ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Unknown: No mitigations Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.3 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
