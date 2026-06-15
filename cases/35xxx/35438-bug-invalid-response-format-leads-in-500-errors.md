# vllm-project/vllm#35438: [Bug]: Invalid response_format leads in 500 errors

| 字段 | 值 |
| --- | --- |
| Issue | [#35438](https://github.com/vllm-project/vllm/issues/35438) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Invalid response_format leads in 500 errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following request ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "openai/gpt-oss-120b", "messages": [ { "role": "user", "content": "hello" } ], "response_format": { "type": "json_schema", "schema": { "type": "object" }'} } ``` results in an HTTP 500 response: ```json {"error":{"message":"","type":"InternalServerError","param":null,"code":500}} ``` However, it should return HTTP 400 (Bad Request), because when using `"type": "json_schema"`, the schema must be wrapped inside the `json_schema` field, like this: ``` "response_format": { "type": "json_schema", "json_schema": { "name": "response", "schema": { "type": "object" } } } ``` In the vLLM logs: ``` (APIServer pid=1) WARNING 02-26 11:57:44 [protocol.py:53] The following fields were present in the request but ignored: {'schema'} (APIServer pid=1) Traceback (most recent call last): (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/chat_completion/api_router.py", line 58, in create_chat_completion (APIServer pid=1) generator = await handler.create_chat_completion(request, raw_r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Invalid response_format leads in 500 errors bug ### Your current environment ### 🐛 Describe the bug The following request ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/jso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ompletion/protocol.py#L446 Instead of using assert, the code should explicitly validate the input and raise a ValueError, since this is a client-side request validation issue, not a server error. ### Before submitting a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s in an HTTP 500 response: ```json {"error":{"message":"","type":"InternalServerError","param":null,"code":500}} ``` However, it should return HTTP 400 (Bad Request), because when using `"type": "json_schema"`, the sche...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: lib/python3.12/dist-packages/vllm/entrypoints/openai/chat_completion/api_router.py", line 58, in create_chat_completion (APIServer pid=1) generator = await handler.create_chat_completion(request, raw_request) (APIServer...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
