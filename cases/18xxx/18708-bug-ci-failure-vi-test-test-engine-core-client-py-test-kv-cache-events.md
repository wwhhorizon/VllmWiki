# vllm-project/vllm#18708: [Bug][CI Failure] - VI Test - test_engine_core_client.py::test_kv_cache_events[True-tcp]

| 字段 | 值 |
| --- | --- |
| Issue | [#18708](https://github.com/vllm-project/vllm/issues/18708) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][CI Failure] - VI Test - test_engine_core_client.py::test_kv_cache_events[True-tcp]

### Issue 正文摘录

### Your current environment Flakey test for at least the past month: https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/4abfbf0d-3a86-8a68-9ff3-0e0ab0fbb38b?period=28days&tags=scm.branch%3Amain%2Cresult%3Afailed ### 🐛 Describe the bug Failing tests: ``` FAILED v1/engine/test_engine_core_client.py::test_kv_cache_events[True-tcp] - AssertionError: No message received assert None is not None ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug][CI Failure] - VI Test - test_engine_core_client.py::test_kv_cache_events[True-tcp] bug;ci-failure ### Your current environment Flakey test for at least the past month: https://buildkite.com/organizations/vllm/anal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][CI Failure] - VI Test - test_engine_core_client.py::test_kv_cache_events[True-tcp] bug;ci-failure ### Your current environment Flakey test for at least the past month: https://buildkite.com/organizations/vllm/anal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
