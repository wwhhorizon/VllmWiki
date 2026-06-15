# vllm-project/vllm#7070: [Bug]: RuntimeError: CHECK_EQ(paged_kv_indptr.size(0), batch_size + 1) failed. 1 vs 257. When load gemma-2-9b-it using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#7070](https://github.com/vllm-project/vllm/issues/7070) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CHECK_EQ(paged_kv_indptr.size(0), batch_size + 1) failed. 1 vs 257. When load gemma-2-9b-it using vllm

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-117-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 72 On-line CPU(s) list: 0-71 Thread(s) per core: 2 Core(s) per socket: 18 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: _EQ(paged_kv_indptr.size(0), batch_size + 1) failed. 1 vs 257. When load gemma-2-9b-it using vllm bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug buil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: lear flush_l1d arch_capabilities Versions of relevant libraries: [pip3] flashinfer==0.1.3+cu121torch2.3 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu11==2.20.5 [pip3] nvidia-nccl-cu12==2.20.5...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
