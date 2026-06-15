# vllm-project/vllm#7694: [Usage]: Periodic snapshots for spot instances

| 字段 | 值 |
| --- | --- |
| Issue | [#7694](https://github.com/vllm-project/vllm/issues/7694) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Periodic snapshots for spot instances

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: Could not collect Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-1134-azure-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD Model name: AMD EPYC 7V13 64-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 1 Core(s) per socket: 48 Socket(s): 1 Stepping: 1 BogoMIPS: 4890.88 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: s for spot instances usage ### Your current environment ```text PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: urrent environment ```text PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: Could not collect Clang version: Coul...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 550.54.15 cuDNN version: Could not colle...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tic==0.2.2 [pip3] torchvision==0.19.0 [pip3] transformers==4.43.3 [pip3] triton==3.0.0 [conda] blas 1.0 mkl [conda] cuda-cudart 12.1.105 0 nvidia [conda] cuda-cupti 12.1.105
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ur current environment ```text PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: Could not collect Clang version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
