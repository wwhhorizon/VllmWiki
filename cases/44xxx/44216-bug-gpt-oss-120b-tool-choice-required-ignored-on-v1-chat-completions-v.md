# vllm-project/vllm#44216: [Bug]: [gpt-oss-120b] tool_choice="required" ignored on /v1/chat/completions (v0.20.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#44216](https://github.com/vllm-project/vllm/issues/44216) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [gpt-oss-120b] tool_choice="required" ignored on /v1/chat/completions (v0.20.1)

### Issue 正文摘录

### Summary On `gpt-oss-120b` via `/v1/chat/completions`, `tool_choice="required"` is silently ignored: vLLM returns a normal prose assistant message with empty `tool_calls` and `finish_reason="stop"` instead of forcing a tool call. Related (closed): #22578. Maintainer comment indicated the original chat-completions tool-call regression was fixed in v0.10.2+, but `tool_choice="required"` specifically is still broken on this model. ### Env - vLLM image: `vllm/vllm-openai:v0.20.1` - Model: `openai/gpt-oss-120b` - Flags: `--enable-auto-tool-choice --tool-call-parser openai` - 2x H100-80GB, TP=2, max_model_len=131072 ### Repro ```bash curl -s -X POST $URL/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "openai/gpt-oss-120b", "messages": [ {"role":"system","content":"You are a helpful assistant."}, {"role":"user","content":"Hello, how are you?"} ], "tools": [ {"type":"function","function":{"name":"calculate","description":"arith","parameters":{"type":"object","properties":{"operation":{"type":"string"},"x":{"type":"number"},"y":{"type":"number"}},"required":["operation","x","y"]}}}, {"type":"function","function":{"name":"get_weather","description":"weather","para...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [gpt-oss-120b] tool_choice="required" ignored on /v1/chat/completions (v0.20.1) ### Summary On `gpt-oss-120b` via `/v1/chat/completions`, `tool_choice="required"` is silently ignored: vLLM returns a normal prose...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uired` constraint is not being propagated to the harmony/guided-decoding backend for this model.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: message with empty `tool_calls` and `finish_reason="stop"` instead of forcing a tool call. Related (closed): #22578. Maintainer comment indicated the original chat-completions tool-call regression was fixed in v0.10.2+,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 20b` - Flags: `--enable-auto-tool-choice --tool-call-parser openai` - 2x H100-80GB, TP=2, max_model_len=131072 ### Repro ```bash curl -s -X POST $URL/v1/chat/completions -H "Content-Type: application/json" -d '{ "model"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 78. Maintainer comment indicated the original chat-completions tool-call regression was fixed in v0.10.2+, but `tool_choice="required"` specifically is still broken on this model. ### Env - vLLM image: `vllm/vllm-openai...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
