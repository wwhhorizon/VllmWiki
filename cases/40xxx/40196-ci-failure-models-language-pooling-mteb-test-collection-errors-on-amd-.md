# vllm-project/vllm#40196: [CI failure] models/language/pooling_mteb_test: collection errors on AMD-CI

| 字段 | 值 |
| --- | --- |
| Issue | [#40196](https://github.com/vllm-project/vllm/issues/40196) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI failure] models/language/pooling_mteb_test: collection errors on AMD-CI

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **All 11 test files in `pooling_mteb_test/`** - Collection errors blocking test discovery **Failure:** ImportError during pytest collection phase - all pooling MTEB test modules fail to import **Configuration:** - Test filter: `core_model and (not slow_test)` - Command: `pytest -v -s models/language -m 'core_model and (not slow_test)'` - 168 tests deselected (found but filtered out) - 11 collection errors in pooling_mteb_test **Likely cause:** Missing import dependencies preventing collection of pooling MTEB tests. The tests import from `tests.models.language.pooling.embed_utils` (document 40) and `tests.models.utils` (not in provided documents). The pytest command scans the entire `models/language` directory and successfully collects 168 tests from other subdirectories (generation, pooling, generation_ppl_test) but fails when attempting to import pooling_mteb_test modules. The missing dependency is likely in the test utility modu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI failure] models/language/pooling_mteb_test: collection errors on AMD-CI rocm;ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI failure] models/language/pooling_mteb_test: collection errors on AMD-CI rocm;ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI failure] models/language/pooling_mteb_test: collection errors on AMD-CI rocm;ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **All 11 test files in `pooling_mt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: failure] models/language/pooling_mteb_test: collection errors on AMD-CI rocm;ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
