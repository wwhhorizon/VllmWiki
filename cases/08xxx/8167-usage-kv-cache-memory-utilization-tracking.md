# vllm-project/vllm#8167: [Usage]: KV cache memory utilization tracking 

| 字段 | 值 |
| --- | --- |
| Issue | [#8167](https://github.com/vllm-project/vllm/issues/8167) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: KV cache memory utilization tracking 

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux trixie/sid (x86_64) GCC version: (Debian 13.3.0-6) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.40 Python version: 3.12.5 (main, Aug 22 2024, 13:11:09) [GCC 14.2.0] (64-bit runtime) Python platform: Linux-6.8.12-amd64-x86_64-with-glibc2.40 Is CUDA available: N/A CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4060 Ti Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz CPU family: 6 Model: 63 Thread(s) per core: 2 Core(s) per socket: 8 Socket(s): 2 Stepping: 2 CPU(s) scaling MHz: 45% CPU max MHz: 3200.0000 CPU min MHz: 1200.0000 BogoMIPS: 47...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux trixie/sid (x86_64) GCC versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux trixie/sid (x86_64) GCC version: (Debian 13.3.0-6) 13.3.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: king usage;stale ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Debian GNU/Linux trixie/si...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: KV cache memory utilization tracking usage;stale ### Your current environment Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build Py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: o 2.3.0 py311_cu121 pytorch [conda] torchtriton 2.3.0 py311 pytorch [conda] torchvision 0.18.0 py311_cu121 pytorch ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
