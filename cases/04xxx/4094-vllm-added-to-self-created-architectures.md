# vllm-project/vllm#4094: vLLM added to self-created architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#4094](https://github.com/vllm-project/vllm/issues/4094) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM added to self-created architectures

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Clang version: Could not collect CMake version: version 3.27.2 Libc version: glibc-2.26 Python version: 3.9.16 | packaged by conda-forge | (main, Feb 1 2023, 21:39:03) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-5.10.179-166.674.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 525.85.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7R32 Stepping: 0 CPU MHz: 2955.534 BogoMIPS: 5599.99 Hypervisor vendor: KVM Virtualization type: full L1d ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: vLLM added to self-created architectures usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: age;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Amazon Linux 2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0220513 [pip3] torchtext==0.14.1 [pip3] torchvision==0.16.1+cu118 [pip3] triton==2.1.0 [conda] blas 1.0 mkl conda-forge [conda] captum 0.5.0 0 pytorch [conda] cudatoolkit 11.7.0
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
