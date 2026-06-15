# vllm-project/vllm#22838: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#22838](https://github.com/vllm-project/vllm/issues/22838) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 2)

### Issue 正文摘录

### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[ovis1_6-test_case4] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test the test is hanging ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b393-4dc8-9a24-7dc533aed82c ### CC List. cc @DarkLight1337

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 2) ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[ovis1_6-test_case4] ### Basic information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 2) ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[ovis1_6-test_case4] ### Basic information
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s[ovis1_6-test_case4] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test the test is hanging ### 📝 History...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 2) ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[ovis1_6-test_case4] ### Basic information...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
