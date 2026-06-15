# vllm-project/vllm#3499: [Usage]: Using a base model with a LoRA on top with AsyncLLMEngine for token streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#3499](https://github.com/vllm-project/vllm/issues/3499) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Using a base model with a LoRA on top with AsyncLLMEngine for token streaming

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.11.7 (main, Dec 15 2023, 18:12:31) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-21-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 Nvidia driver version: 525.147.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Vendor ID: AuthenticAMD Model name: AMD Ryzen Threadripper PRO 5975WX 32-Cores CPU family: 25 Model: 8 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 1 Stepping: 2 Frequency boost: enabled CPU max M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Using a base model with a LoRA on top with AsyncLLMEngine for token streaming usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e model with a LoRA on top with AsyncLLMEngine for token streaming usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
