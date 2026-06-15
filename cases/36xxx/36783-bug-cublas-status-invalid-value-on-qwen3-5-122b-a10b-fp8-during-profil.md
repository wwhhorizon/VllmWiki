# vllm-project/vllm#36783: [Bug]: CUBLAS_STATUS_INVALID_VALUE on Qwen3.5-122B-A10B-FP8 during profile run

| 字段 | 值 |
| --- | --- |
| Issue | [#36783](https://github.com/vllm-project/vllm/issues/36783) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUBLAS_STATUS_INVALID_VALUE on Qwen3.5-122B-A10B-FP8 during profile run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm==0.17.1 Loading Qwen3.5-122B-A10B-FP8 on a single B200 fails with a `CUBLAS_STATUS_INVALID_VALUE` error during the profiling/dummy run phase (`_dummy_run` → `determine_available_memory`). The model weights load successfully (115.37 GiB, ~65s), but the engine crashes immediately after during KV cache initialization. The error occurs inside inductor-generated code at a `cublasGemmEx` call in the first decoder layer's linear attention projection: ``` RuntimeError: CUDA error: CUBLAS_STATUS_INVALID_VALUE when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, std::is_same_v ? CUDA_R_32F : CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` ``` The stack trace points to `qwen3_5.py` → `qwen3_next.py` → inductor-compiled forward → `extern_kernels.mm` with a reinterpret_tensor of shape `(3072, 128)`. Memory is not the issue — the B200 has 192GB and the model only uses ~115GB. ### How to reproduce ```python from vllm import LLM llm = LLM( model="Qwen/Qwen3.5-122B-A10B-FP8", tensor_parallel_size=1, gpu_memory_utilization=0.95, max_model_len=2048, enable_prefix_c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ``` The stack trace points to `qwen3_5.py` → `qwen3_next.py` → inductor-compiled forward → `extern_kernels.mm` with a reinterpret_tensor of shape `(3072, 128)`. Memory is not the issue — the B200 has 192GB and the model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: CUBLAS_STATUS_INVALID_VALUE on Qwen3.5-122B-A10B-FP8 during profile run bug ### Your current environment ### 🐛 Describe the bug vllm==0.17.1 Loading Qwen3.5-122B-A10B-FP8 on a single B200 fails with a `CUBLAS_STA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: escribe the bug vllm==0.17.1 Loading Qwen3.5-122B-A10B-FP8 on a single B200 fails with a `CUBLAS_STATUS_INVALID_VALUE` error during the profiling/dummy run phase (`_dummy_run` → `determine_available_memory`). The model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: CUBLAS_STATUS_INVALID_VALUE on Qwen3.5-122B-A10B-FP8 during profile run bug ### Your current environment ### 🐛 Describe the bug vllm==0.17.1 Loading Qwen3.5-122B-A10B-FP8 on a single B200 fails with a `CUBLAS_STA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: CUBLAS_STATUS_INVALID_VALUE on Qwen3.5-122B-A10B-FP8 during profile run bug ### Your current environment ### 🐛 Describe the bug vllm==0.17.1 Loading Qwen3.5-122B-A10B-FP8 on a single B200 fails with a `CUBLAS_STA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
