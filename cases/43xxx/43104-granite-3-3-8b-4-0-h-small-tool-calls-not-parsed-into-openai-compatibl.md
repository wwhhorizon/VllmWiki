# vllm-project/vllm#43104: Granite 3.3 8B / 4.0 H-Small tool calls not parsed into OpenAI-compatible format

| 字段 | 值 |
| --- | --- |
| Issue | [#43104](https://github.com/vllm-project/vllm/issues/43104) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Granite 3.3 8B / 4.0 H-Small tool calls not parsed into OpenAI-compatible format

### Issue 正文摘录

## Description When using Granite 3.3 8B or Granite 4.0 H-Small (ibm-granite/granite-4.0-h-small) with vLLM's OpenAI-compatible server, the model does NOT emit proper OpenAI-compatible `tool_calls` in responses. Instead, it writes Python code that attempts to call the tools directly. ## Environment - vLLM version: tested against vllm/vllm-openai:v0.20.1 - Model: ibm-granite/granite-3.3-8b-instruct, ibm-granite/granite-4.0-h-small - API: OpenAI-compatible chat completions endpoint (`/v1/chat/completions`) ## Expected Behavior When tools are provided in the request and the model decides to use one, the response should contain a proper `tool_calls` array in the OpenAI format: ```json { "choices": [{ "message": { "role": "assistant", "content": null, "tool_calls": [{ "id": "call_abc123", "type": "function", "function": { "name": "get_weather", "arguments": "{\"location\": \"San Francisco\"}" } }] } }] } ``` ## Actual Behavior The model generates Python code in the `content` field instead of using the `tool_calls` structure: ```python get_weather(location="San Francisco") ``` This appears to be the model's native tool-calling format, but it's not being parsed into OpenAI-compatible `to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ranite 3.3 8B / 4.0 H-Small tool calls not parsed into OpenAI-compatible format ## Description When using Granite 3.3 8B or Granite 4.0 H-Small (ibm-granite/granite-4.0-h-small) with vLLM's OpenAI-compatible server, the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n code that attempts to call the tools directly. ## Environment - vLLM version: tested against vllm/vllm-openai:v0.20.1 - Model: ibm-granite/granite-3.3-8b-instruct, ibm-granite/granite-4.0-h-small - API: OpenAI-compati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Granite 3.3 8B / 4.0 H-Small tool calls not parsed into OpenAI-compatible format ## Description When using Granite 3.3 8B or Granite 4.0 H-Small (ibm-granite/granite-4.0-h-small) with vLLM's OpenAI-compatible server, th...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: pattern. ## Related - Other models with custom tool formats (DeepSeek, Gemma4, etc.) have dedicated parsers - Issue #27661 discusses consolidated tool call parser implementations
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: chat/completions`) ## Expected Behavior When tools are provided in the request and the model decides to use one, the response should contain a proper `tool_calls` array in the OpenAI format: ```json { "choices": [{ "mes...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
