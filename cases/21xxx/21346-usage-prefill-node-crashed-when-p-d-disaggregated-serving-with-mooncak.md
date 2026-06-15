# vllm-project/vllm#21346: [Usage]: Prefill node crashed when P/D Disaggregated Serving with MooncakeStore for Qwen3MOE

| 字段 | 值 |
| --- | --- |
| Issue | [#21346](https://github.com/vllm-project/vllm/issues/21346) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Prefill node crashed when P/D Disaggregated Serving with MooncakeStore for Qwen3MOE

### Issue 正文摘录

### Your current environment ```text python3 collect_env.py INFO 07-22 11:48:03 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-97-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.77 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: py INFO 07-22 11:48:03 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: efill node crashed when P/D Disaggregated Serving with MooncakeStore for Qwen3MOE usage;stale ### Your current environment ```text python3 collect_env.py INFO 07-22 11:48:03 [__init__.py:239] Automatically detected plat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: Prefill node crashed when P/D Disaggregated Serving with MooncakeStore for Qwen3MOE usage;stale ### Your current environment ```text python3 collect_env.py INFO 07-22 11:48:03 [__init__.py:239] Automatically de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u126 [pip3] torchvision==0.21.0+cu126 [pip3] transformers==4.51.3 [pip3] triton==3.2.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
