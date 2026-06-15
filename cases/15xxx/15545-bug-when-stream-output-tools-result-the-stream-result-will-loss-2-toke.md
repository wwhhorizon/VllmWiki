# vllm-project/vllm#15545: [Bug]: when stream output tools result, the stream result will loss 2 token tool data

| 字段 | 值 |
| --- | --- |
| Issue | [#15545](https://github.com/vllm-project/vllm/issues/15545) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when stream output tools result, the stream result will loss 2 token tool data

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when stream request tool model like qwen model, the output stream tool result will lose 2 tokens request ```shell curl "http://127.0.0.1:8080/v1/chat/completions" \ -X POST \ -H "Content-Type: application/json" \ -d '{ "messages": [ { "role": "user", "content": "What is the weather like in New York now?" } ], "model": "Qwen/Qwen2.5-3B-Instruct", "stream": true, "temperature": 0.7, "tools": [ { "type": "function", "function": { "description": "Get weather alerts for a US state. Input is Two-letter US state code (e.g. CA, NY)", "name": "getAlerts", "parameters": { "$schema": "https://json-schema.org/draft/2020-12/schema", "additionalProperties": false, "type": "object", "properties": { "arg0": { "type": "string" } }, "required": [ "arg0" ] } } }, { "type": "function", "function": { "description": "Get weather forecast for a specific latitude/longitude", "name": "getWeatherForecastByLocation", "parameters": { "$schema": "https://json-schema.org/draft/2020-12/schema", "additionalProperties": false, "type": "object", "properties": { "arg0": { "type": "number", "format": "double" }, "arg1": { "type": "number", "format": "double" } }, "...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: m output tools result, the stream result will loss 2 token tool data bug;stale ### Your current environment ### 🐛 Describe the bug when stream request tool model like qwen model, the output stream tool result will lose...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "function": { "description": "Get weather forecast for a specific latitude/longitude", "name": "getWeatherForecastByLocation", "parameters": { "$schema": "https://json-schema.org/draft/2020-12/schema", "additionalProper...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment ### 🐛 Describe the bug when stream request tool model like qwen model, the output stream tool result will lose 2 tokens request ```shell curl "http://127.0.0.1:8080/v1/chat/completions" \ -X POST \ -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d 0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
