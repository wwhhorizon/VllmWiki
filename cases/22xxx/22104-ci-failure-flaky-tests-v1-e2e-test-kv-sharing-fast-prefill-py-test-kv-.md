# vllm-project/vllm#22104: [CI Failure]: Flaky tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False]

| 字段 | 值 |
| --- | --- |
| Issue | [#22104](https://github.com/vllm-project/vllm/issues/22104) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Flaky tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False]

### Issue 正文摘录

### Name of failing test `tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test clearly seems flaky from buildkite and goes away when I restart my failed jobs https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/da952c2e-285d-8272-bb8e-25486933fd79?period=7days ### 📝 History of failing test The test was added in https://github.com/vllm-project/vllm/pull/21590 ### CC List. cc @sarckk @heheda12345

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Flaky tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False] ci-failure ### Name of failing test `tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False]`
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _fast_prefill[False]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test clearly seems flaky from...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ts/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False] ci-failure ### Name of failing test `tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False]` ### Basic information...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: haring_fast_prefill.py test_kv_sharing_fast_prefill[False]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: Flaky tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False] ci-failure ### Name of failing test `tests/v1/e2e/test_kv_sharing_fast_prefill.py test_kv_sharing_fast_prefill[False]`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
