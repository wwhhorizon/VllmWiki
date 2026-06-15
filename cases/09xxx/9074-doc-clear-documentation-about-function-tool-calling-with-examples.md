# vllm-project/vllm#9074: [Doc]: Clear documentation about function / tool calling with examples

| 字段 | 值 |
| --- | --- |
| Issue | [#9074](https://github.com/vllm-project/vllm/issues/9074) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Clear documentation about function / tool calling with examples

### Issue 正文摘录

### 📚 The doc issue Hello, I'm using vllm serve to serve a open AI server like with Mistral-Small-Instruct-2409 as model. When serving I use following arguments "--enable-auto-tool-choice --tool-call-parser mistral" and when I'm trying to use a tool like this ```python tools = [{ "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "city": { "type": "string", "description": "The city to find the weather for, e.g. 'San Francisco'" }, "state": { "type": "string", "description": "the two-letter abbreviation for the state that the city is" " in, e.g. 'CA' which would mean 'California'" }, "unit": { "type": "string", "description": "The unit to fetch the temperature in", "enum": ["celsius", "fahrenheit"] } }, "required": ["city", "state", "unit"] } } }] messages = [{ "role": "user", "content": "Hi! How are you doing today?" }, { "role": "assistant", "content": "I'm doing well! How can I help you?" }, { "role": "user", "content": "Can you tell me what the temperate will be in Dallas, in fahrenheit?" }] chat_completion = client.chat.completions.create(messages=messa...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ello, I'm using vllm serve to serve a open AI server like with Mistral-Small-Instruct-2409 as model. When serving I use following arguments "--enable-auto-tool-choice --tool-call-parser mistral" and when I'm trying to u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: documentation about function / tool calling with examples documentation;stale ### 📚 The doc issue Hello, I'm using vllm serve to serve a open AI server like with Mistral-Small-Instruct-2409 as model. When serving I use...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "type": "object", "properties": { "city": { "type": "string", "description": "The city to find the weather for, e.g. 'San Francisco'" }, "state
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: serve to serve a open AI server like with Mistral-Small-Instruct-2409 as model. When serving I use following arguments "--enable-auto-tool-choice --tool-call-parser mistral" and when I'm trying to use a tool like this `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: mentation here it's said tools are supported : https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#tool-calling-in-the-chat-completion-api Thanks in advance. ### Suggest a potential alternative/fix Clea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
