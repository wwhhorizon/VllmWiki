# vllm-project/vllm#16021: [Bug]: Unable to run Phi4 with tensor-parallel-size 4 torch.compile compatiblity

| 字段 | 值 |
| --- | --- |
| Issue | [#16021](https://github.com/vllm-project/vllm/issues/16021) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run Phi4 with tensor-parallel-size 4 torch.compile compatiblity

### Issue 正文摘录

### Your current environment INFO 04-03 15:28:10 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-1024-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G GPU 1: NVIDIA A10G GPU 2: NVIDIA A10G GPU 3: NVIDIA A10G Nvidia driver version: 555.42.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD Model name: AMD EPYC 7R32 CPU family: 23 Model: 49 Thread(s) per core: 2 Core(s) per socket...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Unable to run Phi4 with tensor-parallel-size 4 torch.compile compatiblity bug;stale ### Your current environment INFO 04-03 15:28:10 [__init__.py:256] Automatically detected platform cuda. Collecting environment...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e to run Phi4 with tensor-parallel-size 4 torch.compile compatiblity bug;stale ### Your current environment INFO 04-03 15:28:10 [__init__.py:256] Automatically detected platform cuda. Collecting environment information....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: t INFO 04-03 15:28:10 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.50.0.dev0 [pip3] triton==3.2.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.1 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
