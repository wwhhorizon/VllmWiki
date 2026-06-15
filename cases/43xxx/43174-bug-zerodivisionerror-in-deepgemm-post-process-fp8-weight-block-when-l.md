# vllm-project/vllm#43174: [Bug]: ZeroDivisionError in deepgemm_post_process_fp8_weight_block when loading FP8 model with TP=16 on dual-node H20

| 字段 | 值 |
| --- | --- |
| Issue | [#43174](https://github.com/vllm-project/vllm/issues/43174) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ZeroDivisionError in deepgemm_post_process_fp8_weight_block when loading FP8 model with TP=16 on dual-node H20

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-117-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 Nvidia driver version : 570.172.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True =...

## 现有链接修复摘要

#43182 Fix ZeroDivisionError when TP does not divide n_groups for DeepSeek-V4 FP8 | #43899 fix: avoid ZeroDivisionError in FP8 scaled MM kernels with high TP (closes #43174)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: ZeroDivisionError in deepgemm_post_process_fp8_weight_block when loading FP8 model with TP=16 on dual-node H20 bug ### Your current environment Collecting environment information... ==============================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.11.post2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: DivisionError in deepgemm_post_process_fp8_weight_block when loading FP8 model with TP=16 on dual-node H20 bug ### Your current environment Collecting environment information... ============================== System Inf...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43182](https://github.com/vllm-project/vllm/pull/43182) | closes_keyword | 0.95 | Fix ZeroDivisionError when TP does not divide n_groups for DeepSeek-V4 FP8 | Fixes:** #43174 ## Problem When using DeepSeek-V4 FP8 model with certain TP sizes (e.g., TP=3/5/6/7/16), the deepgemm BMM path crashes with `ZeroDivisionError` because `bmm_batch |
| [#43899](https://github.com/vllm-project/vllm/pull/43899) | closes_keyword | 0.95 | fix: avoid ZeroDivisionError in FP8 scaled MM kernels with high TP (closes #43174) | Closes #43174 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
