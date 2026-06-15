# vllm-project/vllm#34755: Qwen3-Coder-Next-FP8 with tool calling causes system hard-freeze on multi-GPU tensor parallel (v0.15.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#34755](https://github.com/vllm-project/vllm/issues/34755) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Qwen3-Coder-Next-FP8 with tool calling causes system hard-freeze on multi-GPU tensor parallel (v0.15.1)

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.17.0-14-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.0.140 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version : 590.48.01 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ==================...

## 现有链接修复摘要

#34495 [Bugfix] Fix IndexError in Qwen3CoderToolParser streaming

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: g causes system hard-freeze on multi-GPU tensor parallel (v0.15.1) usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Qwen3-Coder-Next-FP8 with tool calling causes system hard-freeze on multi-GPU tensor parallel (v0.15.1) usage;stale ### Your current environment ```text ============================== System Info =======================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Qwen3-Coder-Next-FP8 with tool calling causes system hard-freeze on multi-GPU tensor parallel (v0.15.1) usage;stale ### Your current environment ```text ============================== System Info ===============

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34495](https://github.com/vllm-project/vllm/pull/34495) | mentioned | 0.45 | [Bugfix] Fix IndexError in Qwen3CoderToolParser streaming | #34322](https://github.com/vllm-project/vllm/issues/34322) and pr [pr #34495](https://github.com/vllm-project/vllm/pull/34495) for qwen3codertoolparser issues. --tool-call-parser… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
