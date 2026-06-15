# vllm-project/vllm#31570: [CI Failure]: Pooling models (Classification model) + tp failure in Full CI run

| 字段 | 值 |
| --- | --- |
| Issue | [#31570](https://github.com/vllm-project/vllm/issues/31570) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Pooling models (Classification model) + tp failure in Full CI run

### Issue 正文摘录

### Name of failing test models/language/pooling_mteb_test/test_qwen3_reranker.py::test_rerank_models_mteb_tp[model_info0] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [CI Failure]: Pooling models (Classification model) + tp failure in Full CI run https://buildkite.com/vllm/ci/builds/45244/steps/canvas?sid=019b7335-eaf7-4adc-af2e-cceae83cb395 ``` Distributed Model Tests (2 GPUs) [2025-12-31T07:26:24Z] FAILED models/language/pooling_mteb_test/test_qwen3_reranker.py::test_rerank_models_mteb_tp[model_info0] - vllm.v1.engine.exceptions.EngineDeadError: ('EngineCore encountered an issue. See stack trace (above) for the root cause.', 'EngineCore encountered an issue. See stack trace (above) for the root cause.') -- [2025-12-31T07:26:24Z] ===== 1 failed, 3 passed, 268 deselected, 7 warnings in 158.88s (0:02:38) ====== ``` ### 📝 History of failing test LAST Success Created at 20251229 15:00 https://buildkite.com/vllm/ci/builds/45066/steps/canvas First Failure Created at 20251230 06:00 https://buildkite.com/vllm/ci/builds/45125/steps/canvas Most likely caused by #27614. [Co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Pooling models (Classification model) + tp failure in Full CI run ci-failure ### Name of failing test models/language/pooling_mteb_test/test_qwen3_reranker.py::test_rerank_models_mteb_tp[model_info0] ### B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Pooling models (Classification model) + tp failure in Full CI run ci-failure ### Name of failing test models/language/pooling_mteb_test/test_qwen3_reranker.py::test_rerank_models_mteb_tp[model_info0] ### B
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _mteb_tp[model_info0] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [CI Failure]: Pooling models (Clas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cation model) + tp failure in Full CI run ci-failure ### Name of failing test models/language/pooling_mteb_test/test_qwen3_reranker.py::test_rerank_models_mteb_tp[model_info0] ### Basic information - [ ] Flaky test - [...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
