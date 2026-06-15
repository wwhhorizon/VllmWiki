# vllm-project/vllm#4516: [Bug]: vllm/vllm-openai:v0.4.1 becomes unresponsive on specific requests

| 字段 | 值 |
| --- | --- |
| Issue | [#4516](https://github.com/vllm-project/vllm/issues/4516) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai:v0.4.1 becomes unresponsive on specific requests

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.7-arch1-2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 550.76 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: GenuineIntel Model name: 12th Gen Intel(R) Core(TM) i9-12900K CPU family: 6 Model: 151 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 2 CPU max MHz: 5200.0000 CPU min MHz: 800.0000 BogoMIPS: 6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vllm/vllm-openai:v0.4.1 becomes unresponsive on specific requests bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm/vllm-openai:v0.4.1 becomes unresponsive on specific requests bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.19.3 [pip3] torch==2.2.1 [pip3] triton==2.2.0 [pip3] vllm-nccl-cu12==2.18.1.0.3.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
