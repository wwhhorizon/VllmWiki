# vllm-project/vllm#25679: [CI Failure]: Cascade attention E2E test fails with FlashInfer backend

| 字段 | 值 |
| --- | --- |
| Issue | [#25679](https://github.com/vllm-project/vllm/issues/25679) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Cascade attention E2E test fails with FlashInfer backend

### Issue 正文摘录

### Name of failing test `v1/e2e/test_cascade_attention.py::test_cascade_attention[FLASHINFER]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test As discussed in #25489, removing the `_VLLM_V1` suffixes revealed that this test is actually failing on main - there's a correctness issue with cascade attention on the FlashInfer backend ([CI run](https://buildkite.com/organizations/vllm/pipelines/ci/builds/32459/jobs/01998103-b1bc-498f-8dac-e8980ca0e108/log)). Previously, the test was trying to run with `FLASHINFER_VLLM_V1`, a backend which didn't exist, so it'd fall back to FlashAttention and pass ([recent nightly](https://buildkite.com/organizations/vllm/pipelines/ci/builds/32390/jobs/01997f08-3b4d-4fdd-bfb8-a55f97193b93/log#155-286)). ### 📝 History of failing test Failure revealed in #25489, so the test was disabled. ### CC List. _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [CI Failure]: Cascade attention E2E test fails with FlashInfer backend stale;ci-failure ### Name of failing test `v1/e2e/test_cascade_attention.py::test_cascade_attention[FLASHINFER]` ### Basic information - [ ] Flaky t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Cascade attention E2E test fails with FlashInfer backend stale;ci-failure ### Name of failing test `v1/e2e/test_cascade_attention.py::test_cascade_attention[FLASHINFER]` ### Basic information - [ ] Flaky
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ttention[FLASHINFER]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test As discussed in #25489, removing t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t_cascade_attention.py::test_cascade_attention[FLASHINFER]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: Cascade attention E2E test fails with FlashInfer backend stale;ci-failure ### Name of failing test `v1/e2e/test_cascade_attention.py::test_cascade_attention[FLASHINFER]` ### Basic information - [ ] Flaky t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
