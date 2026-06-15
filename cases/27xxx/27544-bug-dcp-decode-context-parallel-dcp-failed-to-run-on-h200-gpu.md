# vllm-project/vllm#27544: [Bug]: [DCP] Decode Context Parallel (DCP) failed to run on H200 GPU.

| 字段 | 值 |
| --- | --- |
| Issue | [#27544](https://github.com/vllm-project/vllm/issues/27544) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [DCP] Decode Context Parallel (DCP) failed to run on H200 GPU.

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-157-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H200 GPU 1: NVIDIA H200 GPU 2: NVIDIA H200 GPU 3: NVIDIA H200 GPU 4: NVIDIA H200 GPU 5: NVIDIA H200 GPU 6: NVIDIA H200 GPU 7: NVIDIA H200 ``` ### 🐛 Describe the bug Docker: vllm/vllm-openai:latest Model: Qwen/Qwen3-235B-A22B Test Command: vllm s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ==================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 00 GPU. bug;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: [DCP] Decode Context Parallel (DCP) failed to run on H200 GPU. bug;stale ### Your current environment Collecting environment information... ============================== System Info =============================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uires attention impls to return the softmax lse for decode, but the impl FlashAttentionImpl does not return the softmax lse for decode.', please check the stack trace above for the root cause ### Before submitting a new...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
