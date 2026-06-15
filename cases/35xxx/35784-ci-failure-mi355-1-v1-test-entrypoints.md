# vllm-project/vllm#35784: [CI Failure]:  mi355_1: V1 Test entrypoints

| 字段 | 值 |
| --- | --- |
| Issue | [#35784](https://github.com/vllm-project/vllm/issues/35784) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: V1 Test entrypoints

### Issue 正文摘录

### Name of failing test `pytest -s -v v1/entrypoints/openai/serving_responses/test_basic.py::test_instructions` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a regression in this TG. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5661/steps/canvas?sid=019cad58-e64c-4eb5-a1c1-02602caf22da&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: V1 Test entrypoints ci-failure ### Name of failing test `pytest -s -v v1/entrypoints/openai/serving_responses/test_basic.py::test_instructions` ### Basic information - [ ] Flaky test - [x] Can r
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi355_1: V1 Test entrypoints ci-failure ### Name of failing test `pytest -s -v v1/entrypoints/openai/serving_responses/test_basic.py::test_instructions` ### Basic information - [ ] Flaky test - [x] Can rep...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: y::test_instructions` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a regression in this TG....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /openai/serving_responses/test_basic.py::test_instructions` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
