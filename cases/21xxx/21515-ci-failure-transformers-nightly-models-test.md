# vllm-project/vllm#21515: [CI Failure]: Transformers Nightly Models Test

| 字段 | 值 |
| --- | --- |
| Issue | [#21515](https://github.com/vllm-project/vllm/issues/21515) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Transformers Nightly Models Test

### Issue 正文摘录

### Name of failing test tests/models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-moonshotai/Kimi-VL-A3B-Instruct] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The HF repo for Kimi-VL is incompatible with Transformers nightly because it uses `_validate_images_text_input_order` which has been removed from Transformers. ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/24808/steps/canvas?jid=01983a98-0269-4d9b-ac26-d7f26082d571 ### CC List. @Isotr0py @courage17340

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: Transformers Nightly Models Test ci-failure ### Name of failing test tests/models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-moonshotai/Kimi-VL-A3B-Instruct] ### Basic inf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Transformers Nightly Models Test ci-failure ### Name of failing test tests/models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-moonshotai/Kimi-VL-A3B-Instruct] ### Basic in
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Kimi-VL-A3B-Instruct] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The HF repo for Kimi-VL is incompa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Transformers Nightly Models Test ci-failure ### Name of failing test tests/models/multimodal/processing/test_common.py::test_processing_correctness[1.0-32-0.3-moonshotai/Kimi-VL-A3B-Instruct] ### Basic inf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
