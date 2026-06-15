# vllm-project/vllm#31394: [Bug]: accuracy issue with VLLM_USE_FLASHINFER_MOE_FP8=1 for Qwen3-Coder-480B-A35B-Instruct-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#31394](https://github.com/vllm-project/vllm/issues/31394) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: accuracy issue with VLLM_USE_FLASHINFER_MOE_FP8=1 for Qwen3-Coder-480B-A35B-Instruct-FP8

### Issue 正文摘录

### Your current environment Flashinfer fp8 moe does not seem to work correctly. Saw this issue on both B200 and GB300. The output of python collect_env.py ```text Your output of `python collect_env.py` here Collecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-14) Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Aug 14 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-11)] (64-bit runtime) Python platform : Linux-6.13.2-0_fbk8_0_g8695f611147d-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ============ OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-14) Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.34 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ashinfer fp8 moe does not seem to work correctly. Saw this issue on both B200 and GB300. The output of python collect_env.py ```text Your output of `python collect_env.py` here Collecting environment information... ====...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: accuracy issue with VLLM_USE_FLASHINFER_MOE_FP8=1 for Qwen3-Coder-480B-A35B-Instruct-FP8 bug ### Your current environment Flashinfer fp8 moe does not seem to work correctly. Saw this issue on both B200 and GB300....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: accuracy issue with VLLM_USE_FLASHINFER_MOE_FP8=1 for Qwen3-Coder-480B-A35B-Instruct-FP8 bug ### Your current environment Flashinfer fp8 moe does not seem to work correctly. Saw this issue on both B200 and GB300....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: accuracy issue with VLLM_USE_FLASHINFER_MOE_FP8=1 for Qwen3-Coder-480B-A35B-Instruct-FP8 bug ### Your current environment Flashinfer fp8 moe does not seem to work correctly. Saw this issue on both B200 and GB300....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
