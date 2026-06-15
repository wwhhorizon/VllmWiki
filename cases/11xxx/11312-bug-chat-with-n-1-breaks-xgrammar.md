# vllm-project/vllm#11312: [Bug]: Chat with n>1 breaks xgrammar

| 字段 | 值 |
| --- | --- |
| Issue | [#11312](https://github.com/vllm-project/vllm/issues/11312) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chat with n>1 breaks xgrammar

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug On v0.6.5 making a tools call with n>2 will break guided decoding with the xgrammar guided decoding backend. Booting the server with: ``` $ vllm serve mistralai/Mistral-7B-Instruct-v0.3 --tool-call-parser mistral --enable-auto-tool-choice --compilation-config 3 --chat-template examples/tool_chat_template_mistral_parallel.jinja ``` And then sending this request: ``` curl -X 'POST' \ 'http://localhost:8000/v1/chat/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "model": "mistralai/Mistral-7B-Instruct-v0.3", "messages": [ { "content": "What is the temperature in SF?", "role": "user" } ], "tool_choice": { "type": "function", "function": { "name": "get_current_weather" } }, "tools": [{ "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "city": { "type": "string", "description": "The city to find the weather for, e.g. '\''San Francisco'\''" }, "state": { "type": "string", "description": "the two-letter abbreviation for the state that...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "type": "object", "properties": { "city": { "type": "string", "description": "The city to find the weather for, e.g. '\''San Francisco'\''" },
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eaks xgrammar bug;structured-output ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug On v0.6.5 making a tools call with n>2 will break guided decoding with the xgrammar guided deco...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ll with n>2 will break guided decoding with the xgrammar guided decoding backend. Booting the server with: ``` $ vllm serve mistralai/Mistral-7B-Instruct-v0.3 --tool-call-parser mistral --enable-auto-tool-choice --compi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: les/tool_chat_template_mistral_parallel.jinja ``` And then sending this request: ``` curl -X 'POST' \ 'http://localhost:8000/v1/chat/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
