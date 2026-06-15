# vllm-project/vllm#42381: [Bug]: Scheduler deadlocks after VLLMValidationError when prompt exceeds max_model_len by 1 token

| 字段 | 值 |
| --- | --- |
| Issue | [#42381](https://github.com/vllm-project/vllm/issues/42381) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Scheduler deadlocks after VLLMValidationError when prompt exceeds max_model_len by 1 token

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, May 4 2026, 09:06:35) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-111-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 NVL GPU 1: NVIDIA H100 NVL Nvidia driver version : 595.71.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True =============================...

## 现有链接修复摘要

#42442 [Bugfix] Abort request on ValueError/VLLMValidationError in generate() and encode()

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Scheduler deadlocks after VLLMValidationError when prompt exceeds max_model_len by 1 token bug ### Your current environment Collecting environment information... ============================== System Info ======
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc amd_ibpb_ret arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ]: Scheduler deadlocks after VLLMValidationError when prompt exceeds max_model_len by 1 token bug ### Your current environment Collecting environment information... ============================== System Info ===========...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42442](https://github.com/vllm-project/vllm/pull/42442) | closes_keyword | 0.95 | [Bugfix] Abort request on ValueError/VLLMValidationError in generate() and encode() | Fixes #42381. The `except ValueError` handlers in `AsyncLLM.generate()` and `AsyncLLM.encode()` were the only exception handlers in those methods that did not call `abort()` when |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
