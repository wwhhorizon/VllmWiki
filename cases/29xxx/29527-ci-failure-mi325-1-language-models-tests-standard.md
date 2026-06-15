# vllm-project/vllm#29527: [CI Failure]: mi325_1: Language Models Tests (Standard)

| 字段 | 值 |
| --- | --- |
| Issue | [#29527](https://github.com/vllm-project/vllm/issues/29527) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Language Models Tests (Standard)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests:** 11 test collection errors in `pooling_mteb_test/` directory **Files affected:** - test_baai.py - test_bge_reranker_v2_gemma.py - test_cross_encoder.py - test_gte.py - test_intfloat.py - test_jina.py - test_mxbai_rerank.py - test_nomic.py - test_qwen3_reranker.py - test_snowflake_arctic_embed.py - test_st_projector.py **Failure:** `ModuleNotFoundError: No module named 'mteb.types'` during import at `mteb_utils.py:11` **Configuration:** Tests marked with `core_model` excluding `slow_test` **Likely cause:** Missing or incompatible `mteb` package version. The installed version lacks the `mteb.types` module required by test utilities, causing all pooling MTEB tests to fail during collection phase before any test execution. ### 📝 History of failing test AMD-CI build Buildkite references: - 1041 - 1077 - 1088 - 1109 - 1111 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: mi325_1: Language Models Tests (Standard) ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [CI Failure]: mi325_1: Language Models Tests (Standard) ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests:** 11 test collect...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: t/` directory **Files affected:** - test_baai.py - test_bge_reranker_v2_gemma.py - test_cross_encoder.py - test_gte.py - test_intfloat.py - test_jina.py - test_mxbai_rerank.py - test_nomic.py - test_qwen3_reranker.py -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Language Models Tests (Standard) ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and (not slow_test)'` ### Basic information - [ ] Flaky test - [x] Can reproduce l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
