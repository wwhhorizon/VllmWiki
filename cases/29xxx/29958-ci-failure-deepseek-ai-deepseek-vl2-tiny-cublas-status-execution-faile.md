# vllm-project/vllm#29958: [CI Failure]: deepseek-ai/deepseek-vl2-tiny `CUBLAS_STATUS_EXECUTION_FAILED`

| 字段 | 值 |
| --- | --- |
| Issue | [#29958](https://github.com/vllm-project/vllm/issues/29958) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;moe |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: deepseek-ai/deepseek-vl2-tiny `CUBLAS_STATUS_EXECUTION_FAILED`

### Issue 正文摘录

### Name of failing test GPU_MEMORY_UTILIZATION=0.8 PREFILLER_TP_SIZE=2 DECODER_TP_SIZE=2 MODEL_NAMES=deepseek-ai/deepseek-vl2-tiny bash tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Run `GPU_MEMORY_UTILIZATION=0.8 PREFILLER_TP_SIZE=1 DECODER_TP_SIZE=2 MODEL_NAMES=deepseek-ai/deepseek-vl2-tiny bash tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh` (requires 3 gpus) should fail with ``` [0;36m(EngineCore_DP0 pid=244834)[0;0m ERROR 12-03 11:12:04 [core.py:845] RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, std::is_same_v ? CUDA_R_32F : CUDA_R_16BF, ldc, compute_type, CUBLAS_GEMM_DEFAULT_TENSOR_OP)` ``` I don't think this error is necessarily related to NIXL or PD, so we should be able to repro on a colocated dp/ep setup ### 📝 History of failing test / ### CC List. @yewentao256

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Failure]: deepseek-ai/deepseek-vl2-tiny `CUBLAS_STATUS_EXECUTION_FAILED` stale;ci-failure ### Name of failing test GPU_MEMORY_UTILIZATION=0.8 PREFILLER_TP_SIZE=2 DECODER_TP_SIZE=2 MODEL_NAMES=deepseek-ai/deepseek-vl2-ti...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: eek-ai/deepseek-vl2-tiny bash tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: deepseek-ai/deepseek-vl2-tiny `CUBLAS_STATUS_EXECUTION_FAILED` stale;ci-failure ### Name of failing test GPU_MEMORY_UTILIZATION=0.8 PREFILLER_TP_SIZE=2 DECODER_TP_SIZE=2 MODEL_NAMES=deepseek-ai/deepseek-vl2
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g test GPU_MEMORY_UTILIZATION=0.8 PREFILLER_TP_SIZE=2 DECODER_TP_SIZE=2 MODEL_NAMES=deepseek-ai/deepseek-vl2-tiny bash tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh ### Basic information - [ ] Flaky test -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: imeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling `cublasGemmEx( handle, opa, opb, m, n, k, &falpha, a, CUDA_R_16BF, lda, b, CUDA_R_16BF, ldb, &fbeta, c, std::is_same_v ? CUDA_R_32F : CUDA_R_16BF, ldc, c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
