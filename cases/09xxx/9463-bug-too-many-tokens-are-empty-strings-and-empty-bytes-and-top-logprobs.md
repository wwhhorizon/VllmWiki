# vllm-project/vllm#9463: [Bug]: Too Many Tokens are Empty Strings and Empty Bytes, and `top_logprobs` Can't Identify End-of-Text (EOT) Tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#9463](https://github.com/vllm-project/vllm/issues/9463) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Too Many Tokens are Empty Strings and Empty Bytes, and `top_logprobs` Can't Identify End-of-Text (EOT) Tokens

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When multiple tokens correspond to a single character (e.g., `replay 🧎`), all tokens except the last one are represented as empty strings and empty bytes. In contrast, the OpenAI API provides none-empty strings or bytes for almost every token. Additionally, in `top_logprobs`, End-of-Text tokens are also displayed as empty strings, making it impossible to distinguish between End-of-Text tokens and empty tokens. OpenAI, however, displays end tokens as ` `. ### Reproduction and Problem Description: ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Meta-Llama-3-8B-Instruct", "stream": false, "max_tokens": 20, "logprobs": true, "top_logprobs": 3, "messages": [ { "role": "user", "content": "just reply `🧎`" } ] }' ``` Response: ```json { "id": "chat-c98e3a5a65f14fb482f6209fe04dd38d", "object": "chat.completion", "created": 1729082443, "model": "meta-llama/Meta-Llama-3-8B-Instruct", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "🧎", "tool_calls": [] }, "logprobs": { "content": [ { "token": ""...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: End-of-Text (EOT) Tokens bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When multiple tokens correspond to a single character (e.g., `replay 🧎`), all tokens except the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ty Bytes, and `top_logprobs` Can't Identify End-of-Text (EOT) Tokens bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When multiple tokens correspond to a single characte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
