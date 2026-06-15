# vllm-project/vllm#33029: [CI Failure]: MoE Integration Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#33029](https://github.com/vllm-project/vllm/issues/33029) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: MoE Integration Tests

### Issue 正文摘录

### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep] - RuntimeError: Server exited unexpectedly. -- FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-ModelOpt-fi-cutlass-dp-ep] - RuntimeError: Server exited unexpectedly. issue with AG/RS: (EngineCore_DP0 pid=9097) ERROR 01-24 23:53:57 [core.py:935] ValueError: Unsupported dtype torch.float8_e4m3fn: should be one of int8, uint8, int32, int64, float16, float32, float64, bfloat16. -- ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/48359#019bf3f4-daae-4bc9-afac-cbf276ad8d27 ### CC List. cc @robertgshaw2-redhat

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ls/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: MoE Integration Tests ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep` ### Basic information - [ ] Flaky test - [
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: MoE Integration Tests ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep` ### Basic information - [ ] Flaky test - [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-30B-A3B-NvFp4-CT-fi-cutlass-dp-ep` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
