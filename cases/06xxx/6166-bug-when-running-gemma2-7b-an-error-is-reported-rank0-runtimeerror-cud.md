# vllm-project/vllm#6166: [Bug]: When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` Set up according to the prompts:  os.environ['VLLM_ATTENTION_BACKEND'] = 'FLASHINFER'         print("Environment variable set for VLLM_ATTENTION_BACKEND:", os.getenv('VLLM_ATTENTION_BACKEND'))

| 字段 | 值 |
| --- | --- |
| Issue | [#6166](https://github.com/vllm-project/vllm/issues/6166) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` Set up according to the prompts:  os.environ['VLLM_ATTENTION_BACKEND'] = 'FLASHINFER'         print("Environment variable set for VLLM_ATTENTION_BACKEND:", os.getenv('VLLM_ATTENTION_BACKEND'))

### Issue 正文摘录

### Your current environment When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` Set up according to the prompts: os.environ['VLLM_ATTENTION_BACKEND'] = 'FLASHINFER' print("Environment variable set for VLLM_ATTENTION_BACKEND:", os.getenv('VLLM_ATTENTION_BACKEND')) ### 🐛 Describe the bug When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` Set up according to the prompts: os.environ['VLLM_ATTENTION_BACKEND'] = 'FLASHINFER' print("Environment variable set for VLLM_ATTENTION_BACKEND:", os.getenv('VLLM_ATTENTION_BACKEND'))

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: TENSOR_OP)` Set up according to the prompts: os.environ['VLLM_ATTENTION_BACKEND'] = 'FLASHINFER' print("Environment variable set for VLLM_ATTENTION_BACKEND:", os.getenv('VLLM_ATTENTION_BACKEND')) bug;stale ### Your curr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ug]: When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ld...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t for VLLM_ATTENTION_BACKEND:", os.getenv('VLLM_ATTENTION_BACKEND')) bug;stale ### Your current environment When running gemma2 7b, an error is reported [rank0]: RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
