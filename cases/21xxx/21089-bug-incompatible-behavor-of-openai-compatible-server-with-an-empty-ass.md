# vllm-project/vllm#21089: [Bug]: Incompatible behavor of OpenAI-compatible server with an empty assistant content

| 字段 | 值 |
| --- | --- |
| Issue | [#21089](https://github.com/vllm-project/vllm/issues/21089) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incompatible behavor of OpenAI-compatible server with an empty assistant content

### Issue 正文摘录

### Your current environment I use the official docker image `vllm/vllm-openai:v0.9.1` as-is. ### 🐛 Describe the bug vLLM's OpenAI-compatible server raises an error when I query an empty assistant message to `/v1/chat/completions`. ```console $ curl -H 'content-type: application/json' /v1/chat/completions -d '{"model": " ", "messages": [{"role": "user", "content": "A"}, {"role": "assistant", "content": ""}, {"role": "user", "content": "B"}]}' {"object":"error","message":"Invalid assistant message: role='assistant' content=None tool_calls=None prefix=False Invalid assistant message: role='assistant' content=None tool_calls=None prefix=False","type":"BadRequestError","param":null,"code":400} ``` OpenAI can handle this request. ```console $ curl -H "authorization: Bearer ${OPENAI_API_KEY}" -H 'content-type: application/json' https://api.openai.com/v1/chat/completions -d '{"model": "gpt-4.1-nano", "messages": [{"role": "user", "content": "A"}, {"role": "assistant", "content": ""}, {"role": "user", "content": "B"}]}' { "id": "chatcmpl-Bu8RqqJICBAM7ZunxEhb19ReJSOYv", "object": "chat.completion", "created": 1752718542, "model": "gpt-4.1-nano-2025-04-14", "choices": [ { "index": 0, "messa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: empty assistant content bug ### Your current environment I use the official docker image `vllm/vllm-openai:v0.9.1` as-is. ### 🐛 Describe the bug vLLM's OpenAI-compatible server raises an error when I query an empty assi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ssistant message: role='assistant' content=None tool_calls=None prefix=False Invalid assistant message: role='assistant' content=None tool_calls=None prefix=False","type":"BadRequestError","param":null,"code":400} ``` O...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e $ curl -H 'content-type: application/json' /v1/chat/completions -d '{"model": " ", "messages": [{"role": "user", "content": "A"}, {"role": "assistant", "content": ""}, {"role": "user", "content": "B"}]}' {"object":"er...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : role='assistant' content=None tool_calls=None prefix=False","type":"BadRequestError","param":null,"code":400} ``` OpenAI can handle this request. ```console $ curl -H "authorization: Bearer ${OPENAI_API_KEY}" -H 'cont...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
