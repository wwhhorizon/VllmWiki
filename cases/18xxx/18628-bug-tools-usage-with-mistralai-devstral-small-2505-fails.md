# vllm-project/vllm#18628: [Bug]: Tools usage with `mistralai/Devstral-Small-2505` fails

| 字段 | 值 |
| --- | --- |
| Issue | [#18628](https://github.com/vllm-project/vllm/issues/18628) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tools usage with `mistralai/Devstral-Small-2505` fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When calling vLLM /v1/chat/completions with tools, using the local MCP integration, the HTTP 400 is returned. The error is returned after the example JSON payload is sent to the vLLM. Here is a `curl` call example: ```bash curl http://localhost:8000/v1/chat/completions -H "content-type: application/json" -d '{ "model": "mistralai/Devstral-Small-2505", "stream": false, "tools": [ { "type": "function", "function": { "name": "getWeather_mcp_spring-mcp-server", "description": "Get weather information by city name", "parameters": { "type": "object", "properties": { "cityName": { "type": "string" } }, "required": [ "cityName" ], "$schema": "http://json-schema.org/draft-07/schema#" } } } ], "messages": [ { "role": "user", "content": [ { "type": "text", "text": "How is the weather in Roma?" } ] }, { "role": "assistant", "reasoning_content": null, "content": null, "tool_calls": [ { "id": "5Wsrymo6g", "type": "function", "function": { "name": "getWeather_mcp_spring-mcp-server", "arguments": "{\"cityName\": \"Roma\"}" } } ] }, { "role": "tool", "content": [ { "type": "text", "text": "Sunny" } ], "name": "getWeather_mcp_spring-mcp-server", "...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: "cityName" ], "$schema": "http://json-schema.org/draft-07/schema#" } } } ], "messages": [ { "role": "user", "content": [ { "type": "text", "text": "How is the weather in Roma?" } ] },
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: p_spring-mcp-server", "description": "Get weather information by city name", "parameters": { "type": "object", "properties": { "cityName": { "type": "string" } }, "required": [ "cityName"
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Tools usage with `mistralai/Devstral-Small-2505` fails bug ### Your current environment ### 🐛 Describe the bug When calling vLLM /v1/chat/completions with tools, using the local MCP integration, the HTTP 400 is r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: st:8000/v1/chat/completions -H "content-type: application/json" -d '{ "model": "mistralai/Devstral-Small-2505", "stream": false, "tools": [ { "type": "function", "function": { "name": "getWeather_mcp_spring-mcp-server",...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
