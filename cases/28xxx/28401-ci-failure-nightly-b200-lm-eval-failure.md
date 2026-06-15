# vllm-project/vllm#28401: [CI Failure]: Nightly B200 LM Eval Failure

| 字段 | 值 |
| --- | --- |
| Issue | [#28401](https://github.com/vllm-project/vllm/issues/28401) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Nightly B200 LM Eval Failure

### Issue 正文摘录

### Name of failing test FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness_param[Qwen1.5-MoE-W4A16-CT-tp1] - AssertionError: Accuracy too low: 0.000 < 0.450 - 0.080 ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Crash ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/38163#019a66fd-11a1-407d-8b8e-047044b28f45 ### CC List. _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: Nightly B200 LM Eval Failure ci-failure ### Name of failing test FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness_param[Qwen1.5-MoE-W4A16-CT-tp1] - AssertionError: Accuracy too low: 0.0...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: test_gsm8k_correctness_param[Qwen1.5-MoE-W4A16-CT-tp1] - AssertionError: Accuracy too low: 0.000 < 0.450 - 0.080 ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Nightly B200 LM Eval Failure ci-failure ### Name of failing test FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness_param[Qwen1.5-MoE-W4A16-CT-tp1] - AssertionError: Accuracy too low: 0.00
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: Nightly B200 LM Eval Failure ci-failure ### Name of failing test FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness_param[Qwen1.5-MoE-W4A16-CT-tp1] - AssertionError: Accuracy too low: 0.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness_param[Qwen1.5-MoE-W4A16-CT-tp1] - AssertionError: Accuracy too low: 0.000 < 0.450 - 0.080 ### Basic information - [ ] Flaky test - [x] Can reproduce loc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
