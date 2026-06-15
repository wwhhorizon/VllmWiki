# vllm-project/vllm#38221: Flaky test: test_abort_during_final_step[False] fails intermittently

| 字段 | 值 |
| --- | --- |
| Issue | [#38221](https://github.com/vllm-project/vllm/issues/38221) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Flaky test: test_abort_during_final_step[False] fails intermittently

### Issue 正文摘录

## Summary `tests/v1/engine/test_abort_final_step.py::test_abort_during_final_step[False]` fails intermittently in CI, causing the `Engine (1 GPU)` job to fail. ## Failure Signature ``` AssertionError: Expected at least 1 captured finish status, got 0. File content: ['INIT:WORKER', 'INIT:SCHEDULER'] tests/v1/engine/test_abort_final_step.py:287 ``` The test expects the KV connector's `request_finished()` method to be called with `FINISHED_ABORTED` status, but it's never invoked despite successful initialization. ## Key Observations - `test_abort_during_final_step[False]` (async_scheduling=False) - **fails intermittently** - `test_abort_during_final_step[True]` (async_scheduling=True) - **passes consistently** This indicates a race condition specific to synchronous scheduling mode. ## Flakiness Pattern - [Buildkite Analytics](https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/e12f26d8-bf18-82e0-94bf-eee033ae0703?branch=main&period=7days) shows recent failures - Example failure: [Nightly build #58181](https://buildkite.com/vllm/ci/builds/58181) ## Likely Cause Race condition where the request is completed/freed before abort processing: 1. Request reaches `max_tokens...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: al_step.py::test_abort_during_final_step[False]` fails intermittently in CI, causing the `Engine (1 GPU)` job to fail. ## Failure Signature ``` AssertionError: Expected at least 1 captured finish status, got 0. File con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: st 1 captured finish status, got 0. File content: ['INIT:WORKER', 'INIT:SCHEDULER'] tests/v1/engine/test_abort_final_step.py:287 ``` The test expects the KV connector's `request_finished()` method to be called with `FIN...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Flaky test: test_abort_during_final_step[False] fails intermittently ## Summary `tests/v1/engine/test_abort_final_step.py::test_abort_during_final_step[False]` fails intermittently in CI, causing the `Engine (1 GPU)` jo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Flaky test: test_abort_during_final_step[False] fails intermittently ## Summary `tests/v1/engine/test_abort_final_step.py::test_abort_during_final_step[False]` fails intermittently in CI, causing the `Engine (1 GPU)` jo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
