# vllm-project/vllm#22661: [CI Failure]: Entrypoints test

| 字段 | 值 |
| --- | --- |
| Issue | [#22661](https://github.com/vllm-project/vllm/issues/22661) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints test

### Issue 正文摘录

### Name of failing test entrypoints/openai/test_openai_schema.py::test_openapi_stateless[POST /v1/chat/completions] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2025-08-11T13:20:45Z] (verbose_name='POST /v1/chat/completions') SUBFAIL entrypoints/openai/test_openai_schema.py::test_openapi_stateless[POST /v1/chat/completions] - schemathesis.exceptions.CheckFailed: [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] 1. Server error [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] 2. Undocumented Content-Type [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] Received: text/plain; charset=utf-8 [2025-08-11T13:20:45Z] Documented: application/json [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] [500] Internal Server Error: [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] `Internal Server Error` [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] Reproduce with: [2025-08-11T13:20:45Z] [2025-08-11T13:20:45Z] curl -X POST -H 'Content-Type: application/json' -d '{"messages": [{"role": "assistant", "tool_calls": [{"custom": {"input": "", "name": ""}, "id": "", "type": "custom"}]}]}' --insecure...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /v1/chat/completions] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2025-08-11T13:20:45Z] (verbos...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Entrypoints test ci-failure ### Name of failing test entrypoints/openai/test_openai_schema.py::test_openapi_stateless[POST /v1/chat/completions] ### Basic information - [ ] Flaky test - [x] Can reproduce
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: chema.py::test_openapi_stateless[POST /v1/chat/completions] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints test ci-failure ### Name of failing test entrypoints/openai/test_openai_schema.py::test_openapi_stateless[POST /v1/chat/completions] ### Basic information - [ ] Flaky test - [x] Can reproduce l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
