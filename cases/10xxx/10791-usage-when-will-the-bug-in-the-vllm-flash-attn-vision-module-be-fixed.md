# vllm-project/vllm#10791: [Usage]: When will the bug in the vllm-flash-attn vision module be fixed?

| 字段 | 值 |
| --- | --- |
| Issue | [#10791](https://github.com/vllm-project/vllm/issues/10791) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When will the bug in the vllm-flash-attn vision module be fixed?

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.7 | packaged by conda-forge | (main, Oct 4 2024, 16:05:46) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.8.0-49-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: GenuineIntel Model name: 13th Gen Intel(R) Core(TM) i7-13700 CPU family: 6 Model: 183 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 1 CPU max MHz: 5200.0000 CPU min MHz: 800.0000 BogoMIPS: 4224.00 Flags: fpu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: dule be fixed? usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.2 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 vLLM Build Flags: CUDA A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : When will the bug in the vllm-flash-attn vision module be fixed? usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
