# vllm-project/vllm#44000: [Bug]: Claude Code CLI >= 2.1.154 sends ctx/msg/system roles and breaks vLLM Anthropic Messages API validation

| 字段 | 值 |
| --- | --- |
| Issue | [#44000](https://github.com/vllm-project/vllm/issues/44000) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Claude Code CLI >= 2.1.154 sends ctx/msg/system roles and breaks vLLM Anthropic Messages API validation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading Claude Code CLI to version `2.1.154` or later, Claude Code appears to send additional message roles such as `ctx`, `msg`, and `system` inside the Anthropic Messages API `messages` array. vLLM's Anthropic protocol currently validates incoming message roles as only `user` or `assistant`. Because of this strict validation, requests from recent Claude Code versions fail before model inference starts. Example error: ```text API Error: 400 { "error": { "message": "1 validation error:\n {'type': 'literal_error', 'loc': ('body', 'messages', 1, 'role'), 'msg': \"Input should be 'user' or 'assistant'\", 'input': 'system', 'ctx': {'expected': \"'user' or 'assistant'\"}}", "type": "Bad Request", "param": null, "code": 400 } } ``` This seems to have started after Claude Code CLI `2.1.154`. A temporary workaround reported by users is to expand the allowed roles in `vllm/entrypoints/anthropic/protocol.py`, but a proper upstream fix should probably normalize these roles instead of only expanding the enum. Possible temporary patch: ```diff - role: Literal["user", "assistant"] + role: Literal["user", "assistant", "ctx", "msg", "sys...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vironment ### 🐛 Describe the bug After upgrading Claude Code CLI to version `2.1.154` or later, Claude Code appears to send additional message roles such as `ctx`, `msg`, and `system` inside the Anthropic Messages API `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: strict validation, requests from recent Claude Code versions fail before model inference starts. Example error: ```text API Error: 400 { "error": { "message": "1 validation error:\n {'type': 'literal_error', 'loc': ('bo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: roles as only `user` or `assistant`. Because of this strict validation, requests from recent Claude Code versions fail before model inference starts. Example error: ```text API Error: 400 { "error": { "message": "1 vali...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
