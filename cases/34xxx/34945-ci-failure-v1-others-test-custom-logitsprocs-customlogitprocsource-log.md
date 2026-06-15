# vllm-project/vllm#34945: [CI Failure]: V1 Others : test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT]

| 字段 | 值 |
| --- | --- |
| Issue | [#34945](https://github.com/vllm-project/vllm/issues/34945) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: V1 Others : test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT]

### Issue 正文摘录

### Name of failing test v1/logits_processors/test_custom_offline.py::test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Please take a look at - https://buildkite.com/vllm/ci/builds/52218#019c74b4-5f62-4d3f-8a88-49760ce307ce ``` v1/logits_processors/test_custom_offline.py::test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT] - AssertionError: Request 0 generated [344, 4, 347, 4, 8, 38, 524, 10, 1294, 23, 5, 589, 9, 886, 6, 10817, 4, 38, 524, 10], should all be 128 ``` ### 📝 History of failing test Started failing https://buildkite.com/vllm/ci/builds/52052#019c6f8d-c53d-45f5-b83a-986fc72fee30 ( nightly feb 17th) ### CC List. cc @njhill can you help take a look or point at someone please. Thanks 🙌

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: V1 Others : test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT] stale;ci-failure ### Name of failing test v1/logits_processors/test_custom_offline.py::test_custom_logitsprocs[CustomL
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: st_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT] stale;ci-failure ### Name of failing test v1/logits_processors/test_custom_offline.py::test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOU...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: C_SOURCE_ENTRYPOINT] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Please take a look at - https://bui...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: V1 Others : test_custom_logitsprocs[CustomLogitprocSource.LOGITPROC_SOURCE_ENTRYPOINT] stale;ci-failure ### Name of failing test v1/logits_processors/test_custom_offline.py::test_custom_logitsprocs[CustomL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
