# vllm-project/vllm#26618: [CI Failure]: pooling model MTEB CI failure

| 字段 | 值 |
| --- | --- |
| Issue | [#26618](https://github.com/vllm-project/vllm/issues/26618) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: pooling model MTEB CI failure

### Issue 正文摘录

### Name of failing test `models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/34315/steps/canvas?sid=0199cc47-93cd-48de-9a15-04250b1a3b55 ``` [2025-10-10T04:42:04Z] FAILED models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py::test_rerank_models_mteb[model_info0] - RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} [2025-10-10T04:42:04Z] FAILED models/language/pooling_mteb_test/test_jina.py::test_embed_models_mteb[model_info0] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. [2025-10-10T04:42:04Z] FAILED models/language/pooling_mteb_test/test_st_projector.py::test_embed_models_mteb[model_info1] - AssertionError ``` ### 📝 History of failing test Reported in https://github.com/vllm-project/vllm/pull/26408#issuecomment-3388484957, which is likely a CG issue because of removing `enforce_eager=True` ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: pooling model MTEB CI failure ci-failure ### Name of failing test `models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: pooling model MTEB CI failure ci-failure ### Name of failing test `models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ge/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 04:42:04Z] FAILED models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py::test_rerank_models_mteb[model_info0] - RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} [2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: I Failure]: pooling model MTEB CI failure ci-failure ### Name of failing test `models/language/pooling_mteb_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
