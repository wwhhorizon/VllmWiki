# vllm-project/vllm#10794: [Bug]: Improve Error Messaging for Unsupported Tasks in vLLM (e.g., embedding with Llama Models)

| 字段 | 值 |
| --- | --- |
| Issue | [#10794](https://github.com/vllm-project/vllm/issues/10794) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Improve Error Messaging for Unsupported Tasks in vLLM (e.g., embedding with Llama Models)

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux trixie/sid (x86_64) GCC version: (GCC) 12.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.40 Python version: 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.12-amd64-x86_64-with-glibc2.40 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: AuthenticAMD Model name: AMD EPYC 7443P 24-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 1 Core(s) per socket: 24 Socket(s): 1 Stepping: 1 Frequency boost: enabled CPU(s) scaling MHz: 51% CPU max MHz: 4035.6440 CPU min MHz:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rove Error Messaging for Unsupported Tasks in vLLM (e.g., embedding with Llama Models) bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu124
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ng for Unsupported Tasks in vLLM (e.g., embedding with Llama Models) bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu124
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n==0.20.1 [pip3] transformers==4.46.3 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
