# vllm-project/vllm#13121: [Usage]: The deepseek-ai/DeepSeek-R1 model is not running properly on H100x8*2 devices. Requesting assistance.

| 字段 | 值 |
| --- | --- |
| Issue | [#13121](https://github.com/vllm-project/vllm/issues/13121) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The deepseek-ai/DeepSeek-R1 model is not running properly on H100x8*2 devices. Requesting assistance.

### Issue 正文摘录

### Your current environment ```text INFO 02-11 15:33:40 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Jan 17 2025, 14:35:34) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Orde...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: epseek-ai/DeepSeek-R1 model is not running properly on H100x8*2 devices. Requesting assistance. usage ### Your current environment ```text INFO 02-11 15:33:40 __init__.py:190] Automatically detected platform cuda. Colle...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: The deepseek-ai/DeepSeek-R1 model is not running properly on H100x8*2 devices. Requesting assistance. usage ### Your current environment ```text INFO 02-11 15:33:40 __init__.py:190] Automatically detected platf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: The deepseek-ai/DeepSeek-R1 model is not running properly on H100x8*2 devices. Requesting assistance. usage ### Your current environment ```text INFO 02-11 15:33:40 __init__.py:190] Automatically detected platf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
