# vllm-project/vllm#34706: [CI Failure]: LM Eval Small Models (B200) - Qwen3-Next

| 字段 | 值 |
| --- | --- |
| Issue | [#34706](https://github.com/vllm-project/vllm/issues/34706) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: LM Eval Small Models (B200) - Qwen3-Next

### Issue 正文摘录

### Name of failing test ``` evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-FP8-EP2] ``` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Degraded accuracy scores: ``` FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] - AssertionError: GSM8K metric too low: 0.0000 = (0.75 - 0.08) FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-FP8-EP2] - AssertionError: GSM8K metric too low: 0.0114 = (0.85 - 0.08) ``` ### 📝 History of failing test failing for one day (only on most recent nightly ### CC List. @tdoublep

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-FP8-EP2] ``` ### Basic information - [ ] Flaky test - [x] Can...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: LM Eval Small Models (B200) - Qwen3-Next ci-failure ### Name of failing test ``` evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] evals/gsm8k/test_gsm8k_correctne...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: LM Eval Small Models (B200) - Qwen3-Next ci-failure ### Name of failing test ``` evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] evals/gsm8k/test_gsm8k_correctne...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: en3-Next-FP8-EP2] ``` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Degraded accuracy scores: ``` FAIL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: LM Eval Small Models (B200) - Qwen3-Next ci-failure ### Name of failing test ``` evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] evals/gsm8k/test_gsm8k_correctne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
