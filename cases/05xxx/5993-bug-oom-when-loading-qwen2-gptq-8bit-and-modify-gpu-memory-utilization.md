# vllm-project/vllm#5993: [Bug]: OOM when loading Qwen2 GPTQ 8bit and modify gpu_memory_utilization didn't help

| 字段 | 值 |
| --- | --- |
| Issue | [#5993](https://github.com/vllm-project/vllm/issues/5993) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM when loading Qwen2 GPTQ 8bit and modify gpu_memory_utilization didn't help

### Issue 正文摘录

### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.35 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-6.5.0-41-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 2080 Ti GPU 1: NVIDIA GeForce RTX 2080 Ti GPU 2: NVIDIA GeForce RTX 2080 Ti GPU 3: NVIDIA GeForce RTX 2080 Ti GPU 4: NVIDIA GeForce RTX 2080 Ti Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 56 On-line CPU(s) list: 0-55 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz CPU family: 6 Model: 79 Th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ilization didn't help bug;stale ### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rrent environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: OOM when loading Qwen2 GPTQ 8bit and modify gpu_memory_utilization didn't help bug;stale ### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: oading Qwen2 GPTQ 8bit and modify gpu_memory_utilization didn't help bug;stale ### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.42.3 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
