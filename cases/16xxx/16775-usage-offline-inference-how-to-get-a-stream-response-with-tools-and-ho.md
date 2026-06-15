# vllm-project/vllm#16775: [Usage]: [offline inference] How to get a stream response with tools and how to implement the "parallel_tool_calls" parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#16775](https://github.com/vllm-project/vllm/issues/16775) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Usage]: [offline inference] How to get a stream response with tools and how to implement the "parallel_tool_calls" parameter

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: Could not collect Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.14.0-503.26.1.el9_5.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe Nvidia driver version: 570.124.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 104 On-line CPU(s) list: 0-103 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6230R CPU @ 2.10GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 26 Socket(s): 2 Stepping: 7 CPU max MHz: 4000...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: Could not collect Clang version: Cou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe Nvidia driver version: 570.124.06 cuDNN version: Could not coll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ith tools and how to implement the "parallel_tool_calls" parameter usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0.dev0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.2 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
