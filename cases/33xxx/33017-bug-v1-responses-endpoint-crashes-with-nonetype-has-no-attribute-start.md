# vllm-project/vllm#33017: [Bug] /v1/responses endpoint crashes with 'NoneType has no attribute startswith' when input contains function_call items

| 字段 | 值 |
| --- | --- |
| Issue | [#33017](https://github.com/vllm-project/vllm/issues/33017) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] /v1/responses endpoint crashes with 'NoneType has no attribute startswith' when input contains function_call items

### Issue 正文摘录

## Description The `/v1/responses` endpoint returns a 500 Internal Server Error when the `input` array contains items with `"type": "function_call"`. This breaks compatibility with clients that send conversation history including tool calls (e.g., ClawdBot, OpenAI SDK). ## Minimal Reproduction ```bash curl -X POST http://localhost:8000/v1/responses \ -H "Content-Type: application/json" \ -d '{"model": "YOUR_MODEL_NAME", "input": [{"role": "user", "content": [{"type": "input_text", "text": "hi"}]}, {"type": "function_call", "call_id": "call_123", "name": "read", "arguments": "{\"path\":\"/etc/hostname\"}"}], "stream": true}' ``` ## Expected Behavior The endpoint should parse `function_call` items correctly and include them in the conversation context, similar to how `/v1/chat/completions` handles `tool_calls`. ## Actual Behavior ```json {"error":{"message":"'NoneType' object has no attribute 'startswith'","type":"Internal Server Error","param":null,"code":500}} ``` ## Environment - vLLM version: 0.8.5.post1 (latest docker image `vllm/vllm-openai:latest`) - Model: MiniMax-M2.1-AWQ (but issue is model-agnostic) - OS: Ubuntu 24.04 - GPU: 8x RTX 4090 ## Additional Context - Requests WI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rnal Server Error","param":null,"code":500}} ``` ## Environment - vLLM version: 0.8.5.post1 (latest docker image `vllm/vllm-openai:latest`) - Model: MiniMax-M2.1-AWQ (but issue is model-agnostic) - OS: Ubuntu 24.04 - GP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ype has no attribute startswith' when input contains function_call items stale ## Description The `/v1/responses` endpoint returns a 500 Internal Server Error when the `input` array contains items with `"type": "functio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: at/completions` instead. development ci_build;frontend_api;model_support;quantization quantization crash Description
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: iMax-M2.1-AWQ (but issue is model-agnostic) - OS: Ubuntu 24.04 - GPU: 8x RTX 4090 ## Additional Context - Requests WITHOUT `function_call` items work perfectly - `"type": "message"` items with `role: "assistant"` work f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: The `/v1/chat/completions` endpoint handles tool calls correctly - This blocks using vLLM with clients that rely on the Responses API for multi-turn tool-calling conversations ## Workaround None currently. Users must av...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
