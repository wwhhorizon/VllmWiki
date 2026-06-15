# vllm-project/vllm#10974: [Usage]: How to run local model in docker with cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#10974](https://github.com/vllm-project/vllm/issues/10974) |
| 状态 | closed |
| 标签 | usage;stale |
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

> [Usage]: How to run local model in docker with cpu

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.31.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 6 2024, 20:22:13) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.14.0-427.13.1.el9_4.x86_64-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 45 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8358P CPU @ 2.60GHz CPU family: 6 Model: 106 Thread(s) per core: 1 Core(s) per socket: 4 Socket(s): 2 Stepping: 6 BogoMIPS: 5187.81 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Usage]: How to run local model in docker with cpu usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to run local model in docker with cpu usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to run local model in docker with cpu usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
