# vllm-project/vllm#18257: [Bug]: Phi-4-multimodal-instruct with function calling + streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#18257](https://github.com/vllm-project/vllm/issues/18257) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi-4-multimodal-instruct with function calling + streaming

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I would like to run Phi4-MM with function calling. I load the model using docker (v0.8.5): ``` --model $MODEL_PATH --trust-remote-code --enable-auto-tool-choice --tool-call-parser phi4_mini_json --chat-template tool_chat_template_phi4_mini.jinja ``` Now I send queries like this: ``` curl IP:8000/v1/chat/completions -X POST -H 'Content-Type: application/json' -d '{ "model": "/secondary/thies/Phi-4-multimodal-instruct/", "max_tokens": 1024, "temperature": 0.1, "messages": [ { "role": "user", "content": "How is the temperature in Atlanta in Celsius?" } ], "tools" : [{ "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "City and state, e.g., San Francisco, CA"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]} }, "required": ["location", "unit"] } } }], "tool_choice": "auto", "stream": true }' ``` Output: ``` data: {"id":"chatcmpl-86c2b3f5345d46798a8ad26068400ebc","object":"chat.completion.chunk","created":1747389923,"model":"/secondary/thies/Phi-4-multimodal-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: would like to run Phi4-MM with function calling. I load the model using docker (v0.8.5): ``` --model $MODEL_PATH --trust-remote-code --enable-auto-tool-choice --tool-call-parser phi4_mini_json --chat-template tool_chat_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Phi-4-multimodal-instruct with function calling + streaming bug;stale ### Your current environment ### 🐛 Describe the bug I would like to run Phi4-MM with function calling. I load the model using docker (v0.8.5):...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: data: [DONE] ``` Note: streaming is switched on. When I switch it to false it works. ``` {"id":"chatcmpl-b6122b3dfe7c4200b860eba1f1e95979","object":"chat.completion","created":1747390014,"model":"/secondary/thies/Phi-4-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Phi-4-multimodal-instruct with function calling + streaming bug;stale ### Your current environment ### 🐛 Describe the bug I would like to run Phi4-MM with function calling. I load the model using docker (v0.8.5):...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
