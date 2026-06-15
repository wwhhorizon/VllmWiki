# vllm-project/vllm#41013: [CI Failure]: Batch chat endpoint returns 501 for file content

| 字段 | 值 |
| --- | --- |
| Issue | [#41013](https://github.com/vllm-project/vllm/issues/41013) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Batch chat endpoint returns 501 for file content

### Issue 正文摘录

### Name of failing test entrypoints-integration-api-server-openai-part ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Link to Failed CI https://buildkite.com/vllm/ci/builds/63071/canvas?jid=019dcde0-a093-427e-b6b0-fdc6fb8084b3&tab=output ## Error Message ## Root Cause `tests/entrypoints/openai/test_openai_schema.py` uses Schemathesis/Hypothesis to generate requests from the OpenAPI schema. For POST /v1/chat/completions/batch, it generated a request containing a message content part with `{"type": "file"}`. The server-side chat content parser does not support type="file" and raises: ``` NotImplementedError: Unknown part type: file ``` That propagates to the API response as: ``` {"error":{"message":"Unknown part type: file","type":"NotImplementedError","param":null,"code":501}} ``` So the root cause is a schema / test input vs implementation mismatch: - the schema-based test can generate file content for /v1/chat/completions/batch - but the current implementation does not support that content type - and the existing test-side filter only excludes this unsupported c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Batch chat endpoint returns 501 for file content ci-failure ### Name of failing test entrypoints-integration-api-server-openai-part ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: pi-server-openai-part ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Link to Failed CI https://build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 01}} ``` So the root cause is a schema / test input vs implementation mismatch: - the schema-based test can generate file content for /v1/chat/completions/batch - but the current implementation does not support that con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ailing test entrypoints-integration-api-server-openai-part ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s/openai/test_openai_schema.py` uses Schemathesis/Hypothesis to generate requests from the OpenAPI schema. For POST /v1/chat/completions/batch, it generated a request containing a message content part with `{"type": "fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
