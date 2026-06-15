# vllm-project/vllm#18412: [Bug]: tool_calls.id is Missing in Streaming Responses (stream=true) but Present in Non-Streaming Responses

| 字段 | 值 |
| --- | --- |
| Issue | [#18412](https://github.com/vllm-project/vllm/issues/18412) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_calls.id is Missing in Streaming Responses (stream=true) but Present in Non-Streaming Responses

### Issue 正文摘录

### 🐛 Describe the bug When making an API call to the chat completions endpoint with tools and stream=true, the tool_calls objects within the streamed chunks (delta.tool_calls) do not include the id field for each tool call. However, when stream=false, the tool_calls.id field is correctly present in the response. This inconsistency makes it difficult to uniquely identify and track tool calls when processing streamed responses, which is crucial for many applications that rely on tool usage. The OpenAI API, which vLLM aims to be compatible with, includes the tool_call_id (or equivalent id) in streaming chunks. Steps to Reproduce: Make a request with stream=false: Request Body: ``` { "model": "Qwen/Qwen3-14B-AWQ", "messages": [ { "role": "user", "content": "What is the weather like in Boston today?" } ], "tools": [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA" }, "unit": { "type": "string", "enum": [ "celsius", "fahrenheit" ] } }, "required": [ "location" ] } } }...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Reproduce: Make a request with stream=false: Request Body: ``` { "model": "Qwen/Qwen3-14B-AWQ", "messages": [ { "role": "user", "content": "What is the weather like in Boston today?" } ], "tools": [ { "type": "func
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: aming Responses (stream=true) but Present in Non-Streaming Responses bug;stale;tool-calling ### 🐛 Describe the bug When making an API call to the chat completions endpoint with tools and stream=true, the tool_calls obje...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ludes the tool_call_id (or equivalent id) in streaming chunks. Steps to Reproduce: Make a request with stream=false: Request Body: ``` { "model": "Qwen/Qwen3-14B-AWQ", "messages": [ { "role": "user", "content": "What is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ify and track tool calls when processing streamed responses, which is crucial for many applications that rely on tool usage. The OpenAI API, which vLLM aims to be compatible with, includes the tool_call_id (or equivalen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
