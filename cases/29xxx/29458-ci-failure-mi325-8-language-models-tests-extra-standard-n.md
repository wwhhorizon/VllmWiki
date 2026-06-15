# vllm-project/vllm#29458: [CI Failure]: mi325_8: Language Models Tests (Extra Standard) %N

| 字段 | 值 |
| --- | --- |
| Issue | [#29458](https://github.com/vllm-project/vllm/issues/29458) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_8: Language Models Tests (Extra Standard) %N

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language -m 'core_model and slow_test' --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --shard-id=$BUILDKITE_PARALLEL_JOB` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple MTEB (Massive Text Embedding Benchmark) pooling tests fail during collection phase in `models/language/pooling_mteb_test/`. **Failure:** `ModuleNotFoundError: No module named 'mteb.types'` during test collection, affecting 11 test files (test_baai.py, test_bge_reranker_v2_gemma.py, test_cross_encoder.py, test_gte.py, test_intfloat.py, test_jina.py, test_mxbai_rerank.py, test_nomic.py, test_qwen3_reranker.py, test_snowflake_arctic_embed.py, test_st_projector.py). **Root cause:** The `mteb` package is either missing or installed at an incompatible version that lacks the `mteb.types` module. The `mteb_utils.py` helper file imports `from mteb.types import Array` which triggers this error. **Test scope:** MTEB correctness tests for embedding and reranking models (BAAI, GTE, Snowflake Arctic, Jina, Nomic, Qwen3, etc.) **Likely cause:** Missing `mteb` depend...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: mi325_8: Language Models Tests (Extra Standard) %N ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and slow_test' --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --shard-id=$BUIL
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: mi325_8: Language Models Tests (Extra Standard) %N ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and slow_test' --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --shard-id=$BUI...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_8: Language Models Tests (Extra Standard) %N ci-failure ### Name of failing test `pytest -v -s models/language -m 'core_model and slow_test' --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --shard-id=$BUI...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ILDKITE_PARALLEL_JOB` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple MTEB (Massive Text Embedd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: * Missing `mteb` dependency in the CI environment's requirements for AMD/ROCm builds. ### 📝 History of failing test AMD-CI build Buildkite references: - 1041 - 1077 - 1088 - 1109 - 1111 ### CC List. _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
