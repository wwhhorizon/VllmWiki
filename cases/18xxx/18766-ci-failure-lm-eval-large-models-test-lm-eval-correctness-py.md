# vllm-project/vllm#18766: [CI Failure]: LM Eval Large Models - test_lm_eval_correctness.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18766](https://github.com/vllm-project/vllm/issues/18766) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: LM Eval Large Models - test_lm_eval_correctness.py

### Issue 正文摘录

### Name of failing test `test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename4]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` gsm8k | exact_match,strict-match: ground_truth=0.671 | measured=0.355 gsm8k | exact_match,flexible-extract: ground_truth=0.664 | measured=0.356 ``` Full log: https://buildkite.com/vllm/ci/builds/20837/summary/annotations?sid=01970fe6-97da-4bd8-b139-30d20cf3912f ### 📝 History of failing test Not sure ### CC List. cc @robertgshaw2-redhat @mgoin

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: LM Eval Large Models - test_lm_eval_correctness.py ci-failure ### Name of failing test `test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename4]` ### Basic information - [ ] Flaky test...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: LM Eval Large Models - test_lm_eval_correctness.py ci-failure ### Name of failing test `test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename4]` ### Basic information - [ ] Flaky tes
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: LM Eval Large Models - test_lm_eval_correctness.py ci-failure ### Name of failing test `test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename4]` ### Basic information - [ ] Flaky test...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: am[config_filename4]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` gsm8k | exact_match,strict-mat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` gsm8k | exact_match,strict-match: ground_truth=0.671 | measured=0.355 gsm8k | exact_match,flexible-extract: ground_truth=0.664 | measured=0.356 ``` F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
