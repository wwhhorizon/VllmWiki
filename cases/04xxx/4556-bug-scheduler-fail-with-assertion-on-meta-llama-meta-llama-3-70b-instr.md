# vllm-project/vllm#4556: [Bug]: Scheduler fail with assertion on "meta-llama/Meta-Llama-3-70B-Instruct" when calling concurrently

| 字段 | 值 |
| --- | --- |
| Issue | [#4556](https://github.com/vllm-project/vllm/issues/4556) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Scheduler fail with assertion on "meta-llama/Meta-Llama-3-70B-Instruct" when calling concurrently

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.10.13 (main, May 2 2024, 11:35:09) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.10.0-28-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 GPU 4: NVIDIA L4 GPU 5: NVIDIA L4 GPU 6: NVIDIA L4 GPU 7: NVIDIA L4 Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model na...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: n calling concurrently bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Scheduler fail with assertion on "meta-llama/Meta-Llama-3-70B-Instruct" when calling concurrently bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Scheduler fail with assertion on "meta-llama/Meta-Llama-3-70B-Instruct" when calling concurrently bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.19.3 [pip3] torch==2.2.1 [pip3] triton==2.2.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
