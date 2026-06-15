# vllm-project/vllm#23479: [Bug]: GLM-4.5-Air's output always start with a newline if streaming and reasoning is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#23479](https://github.com/vllm-project/vllm/issues/23479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5-Air's output always start with a newline if streaming and reasoning is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Request: ``` curl \ -X POST \ --no-buffer \ --data-raw '{ "model": "GLM-4.5-Air", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "Hi" } ], "stream": true, "include_reasoning": true, "chat_template_kwargs": { "enable_thinking": true } }' \ -H 'Content-Type: application/json' \ 'http://127.0.0.1:5000/v1/chat/completions' ``` Relevant output: ``` data: ..."delta":{"role":"assistant","content":""}... data: ..."delta":{"content":"\n"}... data: ..."delta":{"reasoning_content":"The"}... data: ..."delta":{"reasoning_content":" user"}... ``` Some clients assume that `reasoning_content` always happen before the content, so that non-empty `content` line before the reasoning part throws them off. Without streaming the leading newline doesn't appear: ``` "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Hello! How can I assist you today?", "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning_content": "The user just sent a simple greeting \"Hi!\". This is a basic opening message, so I should respond with a fr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug Request: ``` curl \ -X POST \ --no-buffer \ --data-raw '{ "model": "GLM-4.5-Air", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "Hi" } ], "stream": t
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ut always start with a newline if streaming and reasoning is enabled bug;stale ### Your current environment ### 🐛 Describe the bug Request: ``` curl \ -X POST \ --no-buffer \ --data-raw '{ "model": "GLM-4.5-Air", "messa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m. I'll keep my response simple and warm since they haven't asked any specific questions or made any particular requests yet. I'll respond in a way that invites further conversation by asking how I can help them today."...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: {{- '\n ' if (enable_thinking is defined and not enable_thinking) else '' -}} {%- endif -%} ``` Should the template end with `\n` to not output a newline at the start, or should the reasoning parser treat `\n ` as the s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
