# vllm-project/vllm#21301: [Bug]: Hermes tool parser returns invalid arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#21301](https://github.com/vllm-project/vllm/issues/21301) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hermes tool parser returns invalid arguments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deal with the qwen3 model and use the tool parser hermes in stream mode. the output result of tool_call do not have the arguments: {} part of tool call Server command: ``` vllm serve /mnt/disk1/qwen3/Qwen3-32B --tensor-parallel-size 8 --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser deepseek_r1 --served-model-name Qwen3-32B ``` Curl with non-stream mode: ``` curl --location 'http://127.0.0.1:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "messages": [ { "content": [ { "type": "text", "text": "what'\''s the time now" } ], "role": "user" } ], "model": "Qwen3-32B", "stream": false, "tools": [ { "type": "function", "function": { "name": "current_time", "description": "Retrieves the current date and time of the server in ISO 8601 format.", "parameters": { "properties": { "timezone_name": { "type": "string" } }, "type": "object" } } } ] }' ``` Result: ``` {"id":"chatcmpl-f30be2a44b414fb789eb5aa61273f3ba","object":"chat.completion","created":1753094863,"model":"Qwen3-32B","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":"\nOkay, the user is asking for t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: But the function requires a timezone_name parameter. The user didn't specify a timezone, so I should probably use the server's default timezone. Wait, but the function might need an explicit timezone. Maybe I should ass...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment ### 🐛 Describe the bug When deal with the qwen3 model and use the tool parser hermes in stream mode. the output result of tool_call do not have the arguments: {} part of tool call Server command...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nse ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Hermes tool parser returns invalid arguments bug;stale ### Your current environment ### 🐛 Describe the bug When deal with the qwen3 model and use the tool parser hermes in stream mode. the output result of tool_c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
