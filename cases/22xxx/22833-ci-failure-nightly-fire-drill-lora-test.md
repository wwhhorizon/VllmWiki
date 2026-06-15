# vllm-project/vllm#22833: [CI Failure][NIGHTLY FIRE DRILL]: LoRA Test

| 字段 | 值 |
| --- | --- |
| Issue | [#22833](https://github.com/vllm-project/vllm/issues/22833) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: LoRA Test

### Issue 正文摘录

### Name of failing test lora/test_minicpmv_tp.py::test_minicpmv_lora ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test startup failure ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b381-446a-ab8b-8e859f2ab9d1 ### CC List. @jeejeelee can you take a look?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: LoRA Test ci-failure ### Name of failing test lora/test_minicpmv_tp.py::test_minicpmv_lora ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external l
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: y::test_minicpmv_lora ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test startup failure ### 📝 History of f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: failing test lora/test_minicpmv_tp.py::test_minicpmv_lora ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: LoRA Test ci-failure ### Name of failing test lora/test_minicpmv_tp.py::test_minicpmv_lora ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external li...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
