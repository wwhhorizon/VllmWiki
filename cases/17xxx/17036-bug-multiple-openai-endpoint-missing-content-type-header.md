# vllm-project/vllm#17036: [Bug]: Multiple openai endpoint Missing Content-Type Header

| 字段 | 值 |
| --- | --- |
| Issue | [#17036](https://github.com/vllm-project/vllm/issues/17036) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multiple openai endpoint Missing Content-Type Header

### Issue 正文摘录

### Your current environment Not reletaed ### 🐛 Describe the bug During property-based testing of the vLLM API, defined by an OpenAPI 3.1 schema, we observed a recurring issue with missing Content-Type headers across several endpoints. ```python 1. GET /health: Issue: Missing Content-Type header Details: The test failed because the server expects a Content-Type: application/json header, but it was not included in the request. 2. GET /ping: Issue: Missing Content-Type header Details: Similar to the previous failure, the Content-Type: application/json header was missing for the request to /ping. 3. POST /ping: Issue: Missing Content-Type header Details: The failure is due to the absence of the Content-Type: application/json header in the POST request to /ping. logs: test_new.py u,uuuu,,uu,,,,u,,,u. [100%] ================================================================================================================== FAILURES ================================================================================================================== _______________________________________________________________________________________ test_openapi_schema_with_fixture (verbose_name='GET /heal...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ionWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable. ref_error: type[Ex...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: json` E E [200] OK: E E E E Reproduce with: E E curl -X GET -H 'Content-Type: application/json' --insecure http://127.0.0.1:8080/health E E Falsifying example: test_openapi_schema_with_fixture( E case=, E
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": "application/json", } > case.call_and_validate(verify=False) E schemathesis.exceptions.CheckFailed: E E 1. Missing Content-Type header E E The following media types are documented in the schema: E - `application/json...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: a Content-Type: application/json header, but it was not included in the request. 2. GET /ping: Issue: Missing Content-Type header Details: Similar to the previous failure, the Content-Type: application/json header was m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
