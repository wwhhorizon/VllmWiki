# vllm-project/vllm#24975: [CI Failure]: entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]

| 字段 | 值 |
| --- | --- |
| Issue | [#24975](https://github.com/vllm-project/vllm/issues/24975) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b]

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/30927#019952f1-b0eb-4079-b2a9-f8bf9dcc5e87 FAILED entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b] - openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unknown recipient: functions.get_weather', 'type': 'BadRequestError', 'param': None, 'code': 400}} ### 📝 History of failing test I think it is flaky since the test is added. ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b] ci-failure ### Name of failing test entrypoints/openai/test_response_api_with_harmony.py::test_function_callin
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b] ci-failure ### Name of failing test entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b] #...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: g[openai/gpt-oss-20b] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_with_harmony.py::test_function_calling[openai/gpt-oss-20b] - openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unknown recipient: functions.get_weather', 'type': 'BadRequestError', 'param': None, 'code'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: entrypoints/openai/test_response_api_with_harmony.py::test_function_calling[openai/gpt-oss-20b] ci-failure ### Name of failing test entrypoints/openai/test_response_api_with_harmony.py::test_function_calli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
