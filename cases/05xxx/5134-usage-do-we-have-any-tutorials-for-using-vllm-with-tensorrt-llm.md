# vllm-project/vllm#5134: [Usage]: Do we have any tutorials for using vllm with tensorrt-LLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#5134](https://github.com/vllm-project/vllm/issues/5134) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Do we have any tutorials for using vllm with tensorrt-LLM?

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.15-1.el7.elrepo.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB GPU 2: Tesla V100-PCIE-32GB GPU 3: Tesla V100-PCIE-32GB Nvidia driver version: 525.89.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-23 Off-line CPU(s) list: 24-63 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: sing vllm with tensorrt-LLM? usage ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Cl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB GPU 2: Tesla V100-PCIE-32GB GPU 3: Tesla V100-PCIE-32GB Nvidia dr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
