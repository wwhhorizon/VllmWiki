# vllm-project/vllm#33532: [CI Failure]: DeepSeek V2 Lite FP8 0% Accuracy [NIGHTLY]

| 字段 | 值 |
| --- | --- |
| Issue | [#33532](https://github.com/vllm-project/vllm/issues/33532) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: DeepSeek V2 Lite FP8 0% Accuracy [NIGHTLY]

### Issue 正文摘录

### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test 0% accuracy in gsm8k seems to have started friday (i.e. clean result on Friday CI run) ### 📝 History of failing test failing over the weekend ### CC List. _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: DeepSeek V2 Lite FP8 0% Accuracy [NIGHTLY] ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Fla...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: DeepSeek V2 Lite FP8 0% Accuracy [NIGHTLY] ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Fla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: DeepSeek V2 Lite FP8 0% Accuracy [NIGHTLY] ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Fl
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: DeepSeek V2 Lite FP8 0% Accuracy [NIGHTLY] ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Fla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e FP8 0% Accuracy [NIGHTLY] ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Flaky test - [x] Can reproduce l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
