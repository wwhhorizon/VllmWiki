# vllm-project/vllm#41854: [CI Failure]:  mi300_1: Multi-Modal Models (Extended Generation 3)

| 字段 | 值 |
| --- | --- |
| Issue | [#41854](https://github.com/vllm-project/vllm/issues/41854) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_1: Multi-Modal Models (Extended Generation 3)

### Issue 正文摘录

### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/multimodal/generation/test_common.py::test_single_image_models[aria-test_case127] FAILED models/multimodal/generation/test_common.py::test_single_image_models[glm4v-test_case134] FAILED models/multimodal/generation/test_common.py::test_single_image_models[glm4v-test_case135] FAILED models/multimodal/generation/test_common.py::test_single_image_models[glm4v-test_case136] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[aria-test_case98] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[glm_ocr-test_case102] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[glm_ocr-test_case103] FAILED models/multimodal/generation/test_common.py::test_multi_image_models[glm_ocr-test_case104] ``` ### 📝 History of failing test - Latest nightly date: 2026-05-06 - Latest build(s): [amd-ci #8223](https://buildkite.com/vllm/amd-ci/builds/8223) - Latest hardware status: `mi300_1`=fail

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi300_1: Multi-Modal Models (Extended Generation 3) ci-failure ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Descr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi300_1: Multi-Modal Models (Extended Generation 3) ci-failure ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Desc
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: neration 3) ci-failure ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/multimodal/gene...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: mi300_1: Multi-Modal Models (Extended Generation 3) ci-failure ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Descr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ls (Extended Generation 3) ci-failure ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
