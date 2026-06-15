# vllm-project/vllm#17161: [Bug]: When I use tool call, the "tool_calls" list in the response  is empty, and the value is in "content", which does not conform to the standard provided by OpenAI.

| 字段 | 值 |
| --- | --- |
| Issue | [#17161](https://github.com/vllm-project/vllm/issues/17161) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When I use tool call, the "tool_calls" list in the response  is empty, and the value is in "content", which does not conform to the standard provided by OpenAI.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Post Messages: { "model": "Qwen2.5-72B-Instruct-GPTQ-Int8", "messages": [ { "role": "user", "content": "What is the weather like in Boston today?" } ], "tools": [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA" }, "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] } }, "required": ["location"] } } } ], "tool_choice": "auto" } Response: { "id": "chatcmpl-8270603cf083427a9b78c11e0572f2ae", "object": "chat.completion", "created": 1745559366, "model": "Qwen2.5-72B-Instruct-GPTQ-Int8", "choices": [ { "index": 0, "message": { "role": "assistant", "reasoning_content": null, "content": " \n{\"name\": \"get_current_weather\", \"arguments\": {\"location\": \"Boston, MA\", \"unit\": \"fahrenheit\"}}\n ", "tool_calls": [] }, "logprobs": null, "finish_reason": "stop", "stop_reason": null } ], "usage": { "prompt_tokens": 212, "total_tokens": 242, "completion_tokens": 30, "prompt_tokens_details": null }, "prompt_lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: on": { "type": "string", "description": "The city and state, e.g. San Francisco, CA" }, "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] } }, "required": ["location"]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment ### 🐛 Describe the bug Post Messages: { "model": "Qwen2.5-72B-Instruct-GPTQ-Int8", "messages": [ { "role": "user", "content": "What is the weather like in Boston today?" } ], "tools": [ { "type"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ty. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: content", which does not conform to the standard provided by OpenAI. bug;stale ### Your current environment ### 🐛 Describe the bug Post Messages: { "model": "Qwen2.5-72B-Instruct-GPTQ-Int8", "messages": [ { "role": "use...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
