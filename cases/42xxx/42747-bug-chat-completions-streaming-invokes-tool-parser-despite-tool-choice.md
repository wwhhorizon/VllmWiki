# vllm-project/vllm#42747: [Bug]: Chat Completions streaming invokes tool parser despite `tool_choice="none"`

| 字段 | 值 |
| --- | --- |
| Issue | [#42747](https://github.com/vllm-project/vllm/issues/42747) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Chat Completions streaming invokes tool parser despite `tool_choice="none"`

### Issue 正文摘录

### Your current environment ## Current environment ```text vLLM v0.21.0 ``` ### 🐛 Describe the bug # The bug When using the OpenAI-compatible Chat Completions API in streaming mode, `tool_choice="none"` does not prevent tool parsing if the server was launched with a tool parser. In non-streaming Chat Completions, `tool_choice="none"` is respected: generated tool-call-looking text remains in `message.content` and is not converted into `message.tool_calls`. In streaming Chat Completions, after the migration to the unified `DelegatingParser.parse_delta()` path, the streaming parser can still enter the tool-call phase and call `extract_tool_calls_streaming(...)` even when the request has `tool_choice="none"`. If the model output matches the configured parser's tool-call format, vLLM can emit `delta.tool_calls` and finish with `finish_reason="tool_calls"` despite the explicit `tool_choice="none"` request. **Expected behavior:** - tool_choice="none" should prevent streamed delta.tool_calls. - Model-generated tool-call-looking text should remain ordinary content, matching non-streaming behavior. - The final streaming chunk should not use finish_reason="tool_calls". **Actual behavior:**...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: s_streaming(...)` even when the request has `tool_choice="none"`. If the model output matches the configured parser's tool-call format, vLLM can emit `delta.tool_calls` and finish with `finish_reason="tool_calls"` despi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ool_calls` and finish with `finish_reason="tool_calls"` despite the explicit `tool_choice="none"` request. **Expected behavior:** - tool_choice="none" should prevent streamed delta.tool_calls. - Model-generated tool-cal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e for other parser/model pairs such as Qwen XML/Coder, DeepSeek, Hermes, Gemma, etc. ## Example API request ```json { "model": "moonshotai/Kimi-K2.6", "stream": true, "tool_choice": "none", "messages": [ { "role": "syst...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ol-call phase and call `extract_tool_calls_streaming(...)` even when the request has `tool_choice="none"`. If the model output matches the configured parser's tool-call format, vLLM can emit `delta.tool_calls` and finis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
