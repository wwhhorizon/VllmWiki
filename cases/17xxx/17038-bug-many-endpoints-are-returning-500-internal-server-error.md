# vllm-project/vllm#17038: [Bug]:  Many endpoints are returning 500 Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#17038](https://github.com/vllm-project/vllm/issues/17038) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Many endpoints are returning 500 Internal Server Error

### Issue 正文摘录

### Your current environment missed to capture ### 🐛 Describe the bug During property-based testing of the vLLM API, defined by an OpenAPI 3.1 schema, we observed a recurring issue Server Errors across several endpoints. ```python 1. POST /tokenize: Issue: Server error (500 Internal Server Error) and undocumented HTTP status code Details: The server responded with a 500 Internal Server Error, but the OpenAPI schema only documents 200 and 422 as possible responses. This suggests that the server might have an issue handling the request. 2. POST /detokenize: Issue: Server error (500 Internal Server Error) and undocumented HTTP status code Details: Similar to the previous failure, the server is returning a 500 Internal Server Error, while the OpenAPI schema only expects 200 or 422. 3. POST /v1/chat/completions: Issue 1: Server error (500 Internal Server Error) Details: The server returned a 500 error instead of the documented 200 or 422. 4. POST /v1/completions: Issue 1: Server error (500 Internal Server Error) Details: The server returned a 500 Internal Server Error instead of the expected 200 or 422. 5. POST /invocations: Issue: Server error (500 Internal Server Error) and undocumen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ionWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable. ref_error: type[Ex...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: json` E E [200] OK: E E E E Reproduce with: E E curl -X GET -H 'Content-Type: application/json' --insecure http://127.0.0.1:8080/health E E Falsifying example: test_openapi_schema_with_fixture( E case=, E
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": "application/json", } > case.call_and_validate(verify=False) E schemathesis.exceptions.CheckFailed: E E 1. Missing Content-Type header E E The following media types are documented in the schema: E - `application/json...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: esponses. This suggests that the server might have an issue handling the request. 2. POST /detokenize: Issue: Server error (500 Internal Server Error) and undocumented HTTP status code Details: Similar to the previous f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
