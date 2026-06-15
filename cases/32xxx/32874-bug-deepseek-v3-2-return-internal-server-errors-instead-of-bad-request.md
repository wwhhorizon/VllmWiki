# vllm-project/vllm#32874: [Bug]: DeepSeek V3.2 return Internal Server Errors instead of Bad Request in reasoning mode

| 字段 | 值 |
| --- | --- |
| Issue | [#32874](https://github.com/vllm-project/vllm/issues/32874) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2 return Internal Server Errors instead of Bad Request in reasoning mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug DeepSeek V3.2. tokeninzer uses asserts for validations. These asserts are translated to 500 Internal Server Error responses instead of 400 Bad request. https://github.com/vllm-project/vllm/blob/main/vllm/tokenizers/deepseek_v32_encoding.py **Example**: ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer EMPTY" \ --verbose -d '{ "model": "deepseek-ai/DeepSeek-V3.2", "temperature": 0.0, "max_tokens": 400, "tool_choice": "auto", "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get weather for a city on a given date.", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "City name, e.g. Amsterdam" }, "date": { "type": "string", "description": "Date in YYYY-MM-DD" } }, "required": ["location", "date"] } } } ], "chat_template_kwargs": { "thinking": true }, "messages": [ { "role": "system", "content": "You are a helpful travel assistant. Use tools when needed. If you call a tool, do not guess the tool result." }, { "role": "user", "content": "Hey! I’ll be in Amsterdam on Friday. What’s the we...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "name": "get_weather", "description": "Get weather for a city on a given date.", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "City name, e.g. Amsterdam" }, "date"
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: DeepSeek V3.2 return Internal Server Errors instead of Bad Request in reasoning mode bug ### Your current environment ### 🐛 Describe the bug DeepSeek V3.2. tokeninzer uses asserts for validations. These asserts a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: gits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
