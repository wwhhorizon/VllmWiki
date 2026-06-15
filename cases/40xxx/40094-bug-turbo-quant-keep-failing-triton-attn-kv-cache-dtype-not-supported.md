# vllm-project/vllm#40094: [Bug]: Turbo Quant keep failing TRITON_ATTN 'kv_cache_dtype not supported'

| 字段 | 值 |
| --- | --- |
| Issue | [#40094](https://github.com/vllm-project/vllm/issues/40094) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Turbo Quant keep failing TRITON_ATTN 'kv_cache_dtype not supported'

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.14.0-33-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L4 Nvidia driver version : 580.126.09 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ===========...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ===============
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Turbo Quant keep failing TRITON_ATTN 'kv_cache_dtype not supported' bug ### Your current environment ```text Collecting environment information... ============================== System Info ======================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rted' bug ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Turbo Quant keep failing TRITON_ATTN 'kv_cache_dtype not supported' bug ### Your current environment ```text Collecting environment information... ============================== System Info ======================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
