# vllm-project/vllm#42020: [CI Failure]:  mi300_1: Multi-Modal Models (Extended Generation 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#42020](https://github.com/vllm-project/vllm/issues/42020) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_1: Multi-Modal Models (Extended Generation 2)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=0) and not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/multimodal/generation/test_common.py::test_single_image_models[skywork_r1v-test_case57] FAILED models/multimodal/generation/test_common.py::test_single_image_models[skywork_r1v-test_case58] FAILED models/multimodal/generation/test_common.py::test_single_image_models[skywork_r1v-test_case59] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[skywork_r1v-test_case53] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[skywork_r1v-test_case54] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[skywork_r1v-test_case55] ``` ### 📝 History of failing test - Latest nightly date: 2026-05-07 - Latest build(s): [amd-ci #8279](https://buildkite.com/vllm/amd-ci/builds/8279) - Latest hardware status: `mi300_1`=fail

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi300_1: Multi-Modal Models (Extended Generation 2) ci-failure ### Name of failing test `pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=0) and not core_model'` ### Basic informati...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi300_1: Multi-Modal Models (Extended Generation 2) ci-failure ### Name of failing test `pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=0) and not core_model'` ### Basic informat
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/multimodal/genera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: mi300_1: Multi-Modal Models (Extended Generation 2) ci-failure ### Name of failing test `pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=0) and not core_model'` ### Basic informati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ulti-Modal Models (Extended Generation 2) ci-failure ### Name of failing test `pytest -v -s models/multimodal/generation/test_common.py -m 'split(group=0) and not core_model'` ### Basic information - [ ] Flaky test - [x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
