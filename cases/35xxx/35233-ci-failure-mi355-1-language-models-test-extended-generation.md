# vllm-project/vllm#35233: [CI Failure]:  mi355_1: Language Models Test (Extended Generation)

| 字段 | 值 |
| --- | --- |
| Issue | [#35233](https://github.com/vllm-project/vllm/issues/35233) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Language Models Test (Extended Generation)

### Issue 正文摘录

### Name of failing test `pytest -s -v models/language/generation/test_common.py::test_models[False-False-5-32-EleutherAI/pythia-70m]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this TG, but it is believed to be cause by some numerical differences introduced by skinny GEMMs. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5300/steps/canvas?sid=019c8e72-d8b4-4ffb-9855-f84a59966fb4&tab=output

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: eutherAI/pythia-70m]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `pytest -s -v models/language/generation/test_common.py::test_models[False-False-5-32-EleutherAI/pythia-70m]` ### Ba
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi355_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `pytest -s -v models/language/generation/test_common.py::test_models[False-False-5-32-EleutherAI/pythia-70m]` ### Bas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi355_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `pytest -s -v models/language/generation/test_common.py::test_models[False-False-5-32-EleutherAI/pythia-70m]` ### Bas...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: `pytest -s -v models/language/generation/test_common.py::test_models[False-False-5-32-EleutherAI/pythia-70m]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
