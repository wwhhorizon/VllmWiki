# vllm-project/vllm#27572: [Bug]: chat/completions stream intermittently returns null as finish_reason

| 字段 | 值 |
| --- | --- |
| Issue | [#27572](https://github.com/vllm-project/vllm/issues/27572) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: chat/completions stream intermittently returns null as finish_reason

### Issue 正文摘录

### Your current environment ``` My env: vllm 0.10.0 ``` ### 🐛 Describe the bug ``` + curl -kLsS https://127.0.0.1:7888/v1/chat/completions -H 'Content-Type: application/json' --data '{ "model": "ibm/granite-3-8b-instruct", "stream": true, "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "What is the weather like in Warsaw?" } ], "tools": [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA" }, "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] } } }, "required": ["location"] } } ], "tool_choice": "auto" }' data: {"id":"chatcmpl-6ca98c2f19c13c19f39013dfb78bcece","object":"chat.completion.chunk","created":1761566772,"model":"ibm/granite-3-8b-instruct","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-6ca98c2f19c13c19f39013dfb78bcece","object":"chat.completion.chunk","created":1761566772,"model":"ibm/granite-3-8b-instruct","...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: chat/completions stream intermittently returns null as finish_reason bug;stale ### Your current environment ``` My env: vllm 0.10.0 ``` ### 🐛 Describe the bug ``` + curl -kLsS https://127.0.0.1:7888/v1/chat/completions...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on": { "type": "string", "description": "The city and state, e.g. San Francisco, CA" }, "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] } } }, "required": ["loc
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 888/v1/chat/completions -H 'Content-Type: application/json' --data '{ "model": "ibm/granite-3-8b-instruct", "stream": true, "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
