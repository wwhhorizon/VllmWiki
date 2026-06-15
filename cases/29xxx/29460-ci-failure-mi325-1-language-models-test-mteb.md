# vllm-project/vllm#29460: [CI Failure]: mi325_1: Language Models Test (MTEB)

| 字段 | 值 |
| --- | --- |
| Issue | [#29460](https://github.com/vllm-project/vllm/issues/29460) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Language Models Test (MTEB)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **All 11 test files in `pooling_mteb_test/`** - Collection errors preventing test discovery **Failure:** Import/Collection error during pytest collection phase - all test modules fail to import **Likely cause:** Missing or broken import dependency in shared test utilities. All test files import from `tests.models.language.pooling.embed_utils` and `tests.models.utils` (not provided in documents). The collection-time failure (before any tests run) indicates either these modules don't exist, have import errors themselves, or depend on packages not available in the ROCm environment. The universal failure across all 11 test files points to a common missing dependency rather than test-specific issues. ### 📝 History of failing test AMD-CI build Buildkite references: - 1041 - 1077 - 1088 - 1109 - 1111 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: Language Models Test (MTEB) ci-failure ### Name of failing test `pytest -v -s models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi325_1: Language Models Test (MTEB) ci-failure ### Name of failing test `pytest -v -s models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ge/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **All 11 test files in `pooling_mt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ave import errors themselves, or depend on packages not available in the ROCm environment. The universal failure across all 11 test files points to a common missing dependency rather than test-specific issues. ### 📝 His...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Language Models Test (MTEB) ci-failure ### Name of failing test `pytest -v -s models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
