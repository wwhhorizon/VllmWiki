# vllm-project/vllm#5336: [Bug]: Getting an empty string ('') for every call on fine-tuned Code-Llama-7b-hf model

| 字段 | 值 |
| --- | --- |
| Issue | [#5336](https://github.com/vllm-project/vllm/issues/5336) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Getting an empty string ('') for every call on fine-tuned Code-Llama-7b-hf model

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.10.13 | packaged by conda-forge | (main, Oct 26 2023, 18:07:37) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.0-26-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version: 525.105.17 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 48 On-line CPU(s) list: 0-47 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Getting an empty string ('') for every call on fine-tuned Code-Llama-7b-hf model bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: F...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mpty string ('') for every call on fine-tuned Code-Llama-7b-hf model bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] numpy 1.25.2 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
