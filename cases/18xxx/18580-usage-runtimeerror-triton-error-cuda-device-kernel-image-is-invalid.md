# vllm-project/vllm#18580: [Usage]:RuntimeError: Triton Error [CUDA]: device kernel image is invalid

| 字段 | 值 |
| --- | --- |
| Issue | [#18580](https://github.com/vllm-project/vllm/issues/18580) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:RuntimeError: Triton Error [CUDA]: device kernel image is invalid

### Issue 正文摘录

### Your current environment ```text (vllm) llm@aitt:/data_a/llm$ python collect_env.py INFO 05-23 10:07:58 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.4 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu118 Is debug build : False CUDA used to build PyTorch : 11.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.0-214-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 N...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 20.04.4 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]:RuntimeError: Triton Error [CUDA]: device kernel image is invalid usage ### Your current environment ```text (vllm) llm@aitt:/data_a/llm$ python collect_env.py INFO 05-23 10:07:58 [__init__.py:239] Automatically...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Usage]:RuntimeError: Triton Error [CUDA]: device kernel image is invalid usage ### Your current environment ```text (vllm) llm@aitt:/data_a/llm$ python collect_env.py INFO 05-23 10:07:58 [__init__.py:239] Automatically...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.4 LTS (x86_64) GCC version : (Ubuntu 9.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
