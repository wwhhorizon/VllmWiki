# vllm-project/vllm#36663: [Bug]: CUBLAS_STATUS_INVALID_VALUE in Docker due to LD_LIBRARY_PATH cuBLAS version conflict

| 字段 | 值 |
| --- | --- |
| Issue | [#36663](https://github.com/vllm-project/vllm/issues/36663) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUBLAS_STATUS_INVALID_VALUE in Docker due to LD_LIBRARY_PATH cuBLAS version conflict

### Issue 正文摘录

## Summary Serving models with quantization (e.g., `--quantization fp8`) in the official vLLM Docker image fails during profiling with `CUBLAS_STATUS_INVALID_VALUE`. The root cause is an `LD_LIBRARY_PATH` setting in the Dockerfile that causes a mismatched system cuBLAS to shadow PyTorch's bundled cuBLAS. ## Environment - **Docker image**: `vllm/vllm-openai:v0.17.0` - **Model**: `ByteDance-Seed/BAGEL-7B-MoT` (also reported with Qwen3.5-122B in #35608) - **Command**: `vllm serve ByteDance-Seed/BAGEL-7B-MoT --port 8091 --quantization fp8` ## Error ``` RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, std::is_same_v ? CUDA_R_32F : CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP) ``` The error occurs during `profile_run()` → `_dummy_sampler_run()` → `compute_logits()` → `lm_head` unquantized GEMM (`torch.nn.functional.linear`). The fp8-quantized linear layers (smaller dimensions) work fine; only the large `lm_head` matmul (hidden_size=3584 × vocab_size=152064) triggers the error. ## Root Cause The vLLM v0.17.0 Dockerfile sets: ```dockerfile ENV LD_LIBRAR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: CUBLAS_STATUS_INVALID_VALUE in Docker due to LD_LIBRARY_PATH cuBLAS version conflict ## Summary Serving models with quantization (e.g., `--quantization fp8`) in the official vLLM Docker image fails during profili...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LD_LIBRARY_PATH cuBLAS version conflict ## Summary Serving models with quantization (e.g., `--quantization fp8`) in the official vLLM Docker image fails during profiling with `CUBLAS_STATUS_INVALID_VALUE`. The root caus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cause is an `LD_LIBRARY_PATH` setting in the Dockerfile that causes a mismatched system cuBLAS to shadow PyTorch's bundled cuBLAS. ## Environment - **Docker image**: `vllm/vllm-openai:v0.17.0` - **Model**: `ByteDance-Se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ocker due to LD_LIBRARY_PATH cuBLAS version conflict ## Summary Serving models with quantization (e.g., `--quantization fp8`) in the official vLLM Docker image fails during profiling with `CUBLAS_STATUS_INVALID_VALUE`....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g., `--quantization fp8`) in the official vLLM Docker image fails during profiling with `CUBLAS_STATUS_INVALID_VALUE`. The root cause is an `LD_LIBRARY_PATH` setting in the Dockerfile that causes a mismatched system cuB...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
