# vllm-project/vllm#42210: [Bug]: Streaming chat completion drops partial content when stop string interrupts auto tool parsing

| 字段 | 值 |
| --- | --- |
| Issue | [#42210](https://github.com/vllm-project/vllm/issues/42210) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming chat completion drops partial content when stop string interrupts auto tool parsing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Summary When using the OpenAI-compatible chat completions API with streaming, auto tool choice, and the `llama3_json` tool parser, a user-provided stop string can interrupt generation while the model has only produced partial tool-call-looking JSON. In this case, non-streaming returns the partial generated text as assistant `content`, but streaming drops that partial text and sends an empty final delta. This makes streaming and non-streaming behavior inconsistent for the same request. There is also a related finish-reason issue: when the stop was caused by a user-requested stop string, the final streaming response should preserve `finish_reason: "stop"` instead of treating the partial parser state as a completed tool call. # Reproduction Start the server: ```bash vllm serve meta-llama/Llama-3.1-8B-Instruct \ --max-model-len 8192 \ --served-model-name base_model \ --enable-auto-tool-choice \ --tool-call-parser llama3_json ``` Send a streaming request with a stop string: ```bash curl -s http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "base_model", "stream": true, "stop": ["a"], "me...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mpatible chat completions API with streaming, auto tool choice, and the `llama3_json` tool parser, a user-provided stop string can interrupt generation while the model has only produced partial tool-call-looking JSON. I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "role": "user", "content": "What is the weather in San Francisco?" } ], "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get weather for a location", "parameters": {
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ll. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: his makes streaming and non-streaming behavior inconsistent for the same request. There is also a related finish-reason issue: when the stop was caused by a user-requested stop string, the final streaming response shoul...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
