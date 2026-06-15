# vllm-project/vllm#9053: [Bug]: Different behavior with tool-use response parsing with streaming vs non-streaming when using max_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#9053](https://github.com/vllm-project/vllm/issues/9053) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Different behavior with tool-use response parsing with streaming vs non-streaming when using max_tokens

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run the server with Mistral with auto-tool support ``` vllm serve mistralai/Mistral-7B-Instruct-v0.3 --enable-auto-tool-choice --tool-call-parser mistral --chat-template tool_chat_template_mistral.jinja ``` and send the following streaming request to `/v1/chat/completions`. with auto tool choice, and a limit on max_tokens: ```json { "model": "mistralai/Mistral-7B-Instruct-v0.3", "tool_choice": "auto", "max_tokens": 16, "stream": true, "messages": [ { "role": "user", "content": "What is the weather like in California?" } ], "tools": [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "description": "The city, e.g. San Francisco, CA", "type": "string" }, "unit": { "enum": ["celsius", "fahrenheit"], "type": "string" } }, "required": ["location"] } } } ] } ``` I get the following chunks in the response that build a partial entry in `tool_calls`, and do not have a `finish_reason` returned: ``` data: {"id":"chat-4f2c1c18d3ec41f68f7574b54467a4ed","object...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: "location": { "description": "The city, e.g. San Francisco, CA", "type": "string" }, "unit": { "enum": ["celsius", "fahrenheit"], "t
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sponse parsing with streaming vs non-streaming when using max_tokens bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run the server with Mistral with auto-tool su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing when using max_tokens bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run the server with Mistral with auto-tool support ``` vllm serve mistralai/Mistral-7B-I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
