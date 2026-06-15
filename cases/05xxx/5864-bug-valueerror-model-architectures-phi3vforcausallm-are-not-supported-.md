# vllm-project/vllm#5864: [Bug]: ValueError: Model architectures ['Phi3VForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#5864](https://github.com/vllm-project/vllm/issues/5864) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model architectures ['Phi3VForCausalLM'] are not supported for now.

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.15.0-1063-aws-x86_64-with-glibc2.31 Is CUDA available: N/A CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: Tesla T4 Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz Stepping: 7 CPU MHz: 2499.998 BogoMIPS: 4999.99 Hy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ValueError: Model architectures ['Phi3VForCausalLM'] are not supported for now. bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: Model architectures ['Phi3VForCausalLM'] are not supported for now. bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ost1 --model microsoft/Phi-3-vision-128k-instruct --trust-remote-code --dtype half ``` Error: [rank0]: ValueError: Model architectures ['Phi3VForCausalLM'] are not supported for now. Supported architectures: correctness...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Vulnerable Vulnerability Spec rstack overflo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
