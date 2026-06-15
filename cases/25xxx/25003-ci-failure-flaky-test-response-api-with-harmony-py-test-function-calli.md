# vllm-project/vllm#25003: [CI Failure]: Flaky `test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]`

| 字段 | 值 |
| --- | --- |
| Issue | [#25003](https://github.com/vllm-project/vllm/issues/25003) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Flaky `test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]`

### Issue 正文摘录

### Name of failing test `entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The error: ``` [2025-09-16T22:18:58Z] E openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unknown recipient: functions.get_weather', 'type': 'BadRequestError', 'param': None, 'code': 400}} ``` Example failure: https://buildkite.com/vllm/ci/builds/30999#01995468-af55-4f82-b0cd-d7fd670abab9 ### 📝 History of failing test https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/e242093d-1033-8042-a229-87b736d010dd?branch=main&period=1day ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Flaky `test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]` ci-failure ### Name of failing test `entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/g
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : Flaky `test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]` ci-failure ### Name of failing test `entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The error: ``` [2025-09-16T22:18:5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng test The error: ``` [2025-09-16T22:18:58Z] E openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unknown recipient: functions.get_weather', 'type': 'BadRequestError', 'param': None, 'code': 400}} ``` Exa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Flaky `test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]` ci-failure ### Name of failing test `entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
