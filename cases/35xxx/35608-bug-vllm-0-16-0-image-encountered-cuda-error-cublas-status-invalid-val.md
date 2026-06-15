# vllm-project/vllm#35608: [Bug]: vllm 0.16.0+image encountered CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx

| 字段 | 值 |
| --- | --- |
| Issue | [#35608](https://github.com/vllm-project/vllm/issues/35608) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;moe;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.16.0+image encountered CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx

### Issue 正文摘录

### Your current environment Encountered RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx( handle, opa, opb, m, n, k, alpha_ptr, a, CUDA_R_16F, lda, b, CUDA_R_16F, ldb, beta_ptr, c, std::is_same_v ? CUDA_R_32F : CUDA_R_16F, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` when deploying Qwen3.5-122B Didn't find much documentation or solution regarding this issue, but solved it in an unexpected way. Solution ``` unset LD_LIBRARY_PATH ``` ### 🐛 Describe the bug It seems like the vllm image is having conflict with the CUDA library and can be resolved by unsetting LD_LIBRARY_PATH. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: R_16F, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` when deploying Qwen3.5-122B Didn't find much documentation or solution regarding this issue, but solved it in an unexpected way. Solution ``` unset LD_LIBRARY_PA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: buted_parallel;frontend_api;gemm_linear;model_support;moe;multimodal_vlm;quantization;scheduler_memory attention;cuda;kernel;moe;quantization;triton crash dtype;env_dependency;memory_layout Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vllm 0.16.0+image encountered CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx bug ### Your current environment Encountered RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: encountered CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx bug ### Your current environment Encountered RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx( handle, opa,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: vlm;quantization;scheduler_memory attention;cuda;kernel;moe;quantization;triton crash dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
