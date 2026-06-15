# vllm-project/vllm#28219: [Bug]: DeepSeek-R1-Distill-Llama-8B tool calls returned in content instead of tool_calls array

| 字段 | 值 |
| --- | --- |
| Issue | [#28219](https://github.com/vllm-project/vllm/issues/28219) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1-Distill-Llama-8B tool calls returned in content instead of tool_calls array

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Issue Summary:** Tool calls are not being properly parsed for the `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` model, despite configuring the server with `enable_auto_tool_choice=True` and `tool_call_parser='llama3_json'`. **Expected Behavior:** The model should return structured tool calls in the `tool_calls` array of the response, following the OpenAI API format. **Actual Behavior:** The model generates the correct JSON structure for the tool call in the `content` field, but the `tool_calls` array remains empty. The response includes: - The tool call JSON in the message `content` instead of being parsed into `tool_calls` - An empty `tool_calls` array: `"tool_calls":[]` - `finish_reason` is set to `"stop"` instead of `"tool_calls"` **Request Example:** ```bash curl -X POST \ -H "Content-Type: application/json" \ "http://vllm-deepkseek-r1-llama-8b-service/v1/chat/completions" \ -d '{ "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B", "stream": false, "messages": [ { "role": "user", "content": "How is the current weather in Bangalore in celsius?" } ], "tools": [ { "type": "function", "function": { "name": "get_current_weather",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: DeepSeek-R1-Distill-Llama-8B tool calls returned in content instead of tool_calls array bug;stale ### Your current environment ### 🐛 Describe the bug **Issue Summary:** Tool calls are not being properly parsed fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -Llama-8B tool calls returned in content instead of tool_calls array bug;stale ### Your current environment ### 🐛 Describe the bug **Issue Summary:** Tool calls are not being properly parsed for the `deepseek-ai/DeepSee...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng them properly. This could be due to: 1. The DeepSeek-R1 model using a different output format than Llama 3.1 2. The presence of ` ` tags in the output interfering with parsing 3. The chat template not being compatibl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: { "type": "string", "description": "The city and country, eg. San Francisco, USA" }, "format": { "type": "string", "enum": ["celsius", "fahrenheit"] } } } }
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mat ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
