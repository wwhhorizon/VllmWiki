# vllm-project/vllm#5465: [Bug]: Runtime Error: GET was unable to find an engine to execute this computation for LLaVa-NEXT

| 字段 | 值 |
| --- | --- |
| Issue | [#5465](https://github.com/vllm-project/vllm/issues/5465) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Runtime Error: GET was unable to find an engine to execute this computation for LLaVa-NEXT

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.27 Python version: 3.10.12 (main, Jul 19 2023, 10:44:52) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-4.15.0-213-generic-x86_64-with-glibc2.27 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 12 On-line CPU(s) list: 0-11 Thread(s) per core: 1 Core(s) per socket: 12 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 61 Model name: Intel Core Processor (Broadwell) Stepping: 2 CPU MHz: 2095.076 BogoMIPS: 4190.15 Hypervisor vendor: KVM Virtualization type: full L1d cache: 32K L1i cache: 32K L2 cache: 4096K L3 cache: 16384K NUMA node0 CPU(s): 0-11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: utation for LLaVa-NEXT bug ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Cl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: rent environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] blas 1.0 mkl [conda] mkl 2019.4 243 [conda] mkl-service

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
