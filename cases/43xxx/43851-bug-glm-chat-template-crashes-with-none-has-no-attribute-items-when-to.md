# vllm-project/vllm#43851: [Bug]: GLM chat template crashes with "'None' has no attribute 'items'" when tool_call arguments is the string "null"

| 字段 | 值 |
| --- | --- |
| Issue | [#43851](https://github.com/vllm-project/vllm/issues/43851) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM chat template crashes with "'None' has no attribute 'items'" when tool_call arguments is the string "null"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a multi-turn request includes an assistant message whose `tool_calls[].function.arguments` is the JSON string `"null"`, vLLM returns a `400 BadRequestError: 'None' has no attribute 'items'`. The request is valid per the OpenAI wire spec — `arguments` is a string, so it passes Pydantic validation — but the server crashes before producing a response. This surfaces in real chatbot applications where the model calls a zero-argument tool: the client echoes the assistant turn back verbatim on the next round, and `arguments` ends up as the string `"null"`. Note: sending `arguments: null` (JSON null, not string) is correctly rejected by Pydantic with a different error. Only the string `"null"` hits this path. **Minimal reproduction** (no model needed, pure HTTP): ```python import json, urllib.request, urllib.error, os payload = { "model": os.environ["VLLM_MODEL"], "messages": [ {"role": "user", "content": "What time is it?"}, { "role": "assistant", "content": None, "tool_calls": [{ "id": "call_1", "type": "function", "function": {"name": "get_current_time", "arguments": "null"}, }], }, {"role": "tool", "tool_call_id": "call_1", "con...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g, so it passes Pydantic validation — but the server crashes before producing a response. This surfaces in real chatbot applications where the model calls a zero-argument tool: the client echoes the assistant turn back...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: # Your current environment ### 🐛 Describe the bug When a multi-turn request includes an assistant message whose `tool_calls[].function.arguments` is the JSON string `"null"`, vLLM returns a `400 BadRequestError: 'None'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: : null, "code": 400}} ``` ### Before submitting a new issue... - [x] Searched existing issues — closest match is #32213 (parser crash on zero-arg tool output), which is a different code path. No existing issue covers th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oducing a response. This surfaces in real chatbot applications where the model calls a zero-argument tool: the client echoes the assistant turn back verbatim on the next round, and `arguments` ends up as the string `"nu...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
