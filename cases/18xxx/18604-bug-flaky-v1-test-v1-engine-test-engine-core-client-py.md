# vllm-project/vllm#18604: [Bug][Flaky]: V1 Test - v1/engine/test_engine_core_client.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18604](https://github.com/vllm-project/vllm/issues/18604) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Flaky]: V1 Test - v1/engine/test_engine_core_client.py

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug The test `v1/engine/test_engine_core_client.py::test_kv_cache_events[True-tcp]` is flaky. https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/4abfbf0d-3a86-8a68-9ff3-0e0ab0fbb38b?period=7days&tags=scm.branch%3Amain cc @robertgshaw2-redhat @njhill ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug][Flaky]: V1 Test - v1/engine/test_engine_core_client.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug The test `v1/engine/test_engine_core_client.py::test_kv_cache_events[True-tcp]` is flak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ll ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][Flaky]: V1 Test - v1/engine/test_engine_core_client.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug The test `v1/engine/test_engine_core_client.py::test_kv_cache_events[True-tcp]` is flak...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
