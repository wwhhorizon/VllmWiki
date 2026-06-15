# vllm-project/vllm#29526: [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#29526](https://github.com/vllm-project/vllm/issues/29526) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 | build_error;import_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling)

### Issue 正文摘录

### Name of failing test `export VLLM_WORKER_MULTIPROC_METHOD=spawn && pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Collection Errors** in pooling entrypoint tests (2 errors) **Failing Tests:** - `entrypoints/pooling/embed/test_correctness_mteb.py` - Collection error - `entrypoints/pooling/score/test_correctness_mteb.py` - Collection error **Failure:** ModuleNotFoundError at import time - `from mteb.types import Array` fails because `mteb.types` module doesn't exist in the installed mteb version. **Configuration:** - Tests use MTEB (Massive Text Embedding Benchmark) library for correctness validation - Import chain: test file → `tests.models.language.pooling_mteb_test.mteb_utils` → `mteb.types` **Likely cause:** Version incompatibility - the `mteb` library installed in the test environment has a different module structure than expected. The `mteb.types` module may have been moved, renamed, or removed in the installed version. The deprecation warnings visible in logs (207 warnings about `MultilingualTask`, 378 about `metadata_dict...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling) ci-failure ### Name of failing test `export VLLM_WORKER_MULTIPROC_METHOD=spawn && pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test -
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: MULTIPROC_METHOD=spawn && pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling) ci-failure ### Name of failing test `export VLLM_WORKER_MULTIPROC_METHOD=spawn && pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Collection Errors** in pooling en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rsion is installed. **Additional context:** 9 tests skipped (expected - ROCm encoder self-attention tests), 637 deprecation warnings from mteb library indicating API changes between versions. ### 📝 History of failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
