# vllm-project/vllm#35128: [CI Failure]:  mi355_1: Language Models Tests (Standard)

| 字段 | 值 |
| --- | --- |
| Issue | [#35128](https://github.com/vllm-project/vllm/issues/35128) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Language Models Tests (Standard)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are some failing tests in this TG: ```log FAILED models/language/generation/test_common.py::test_models[True-True-5-32-TitanML/tiny-mixtral] FAILED models/language/generation/test_common.py::test_models[True-False-5-32-TitanML/tiny-mixtral] FAILED models/language/generation/test_common.py::test_models[False-True-5-32-TitanML/tiny-mixtral] FAILED models/language/generation/test_common.py::test_models[False-False-5-32-TitanML/tiny-mixtral] ``` ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5234/steps/canvas?sid=019c894c-5dc1-4807-989f-da8eca7627cc&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Language Models Tests (Standard) ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi355_1: Language Models Tests (Standard) ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are some failing tests in th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: al] FAILED models/language/generation/test_common.py::test_models[True-False-5-32-TitanML/tiny-mixtral] FAILED models/language/generation/test_common.py::test_models[False-True-5-32-TitanML/tiny-mixtral] FAILED models/l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_1: Language Models Tests (Standard) ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
