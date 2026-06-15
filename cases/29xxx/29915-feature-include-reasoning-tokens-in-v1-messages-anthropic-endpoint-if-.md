# vllm-project/vllm#29915: [Feature]: include reasoning tokens in /v1/messages Anthropic endpoint if model supports it

| 字段 | 值 |
| --- | --- |
| Issue | [#29915](https://github.com/vllm-project/vllm/issues/29915) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: include reasoning tokens in /v1/messages Anthropic endpoint if model supports it

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the Anthropic compatible /v1/messages endpoint doesn't return the reasoning tokens, even if the model supports it. We should make it as compatible as possible with the real API endpoint. For example on gpt-oss-20b , if we call /v1/chat/completions we get the reasoning tokens: ``` curl -X POST "http://localhost:8000/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "stream": false, "model": "openai/gpt-oss-20b", "max_tokens": 2000, "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ {"type": "text", "text": "Name the european capitals"} ]} ] }' | jq ``` the return is ``` { "id": "chatcmpl-46b8a8812f514e72b263ed8e73e39072", "object": "chat.completion", "created": 1764704282, "model": "openai/gpt-oss-20b", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Here’s a comprehensive list of recognized European sovereign states and the capitals of each. (All are UN‑member or widely‑recognized states; the list follows the usual political geography of Europe as of 2025.)\n\n| Country | Capital |\n|---------|---------|\n| Albania | Tirana |\n| Andorr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Feature]: include reasoning tokens in /v1/messages Anthropic endpoint if model supports it feature request ### 🚀 The feature, motivation and pitch Currently the Anthropic compatible /v1/messages endpoint doesn't return...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n Sahara? not part. Also maybe some integrated territories like Andorra, small. Thus list of capitals.\n\nWe can format nicely: bullet list. Mention there are 44 sovereign states in Europe. The user didn't specify \"inc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: chtenstein | Vaduz |\n| Lithuania | Vilnius |\n| Luxembourg | Luxembourg City |\n| Malta | Valletta |\n| Moldova | Chisinau |\n| Monaco | Monaco (city‑state) |\n| Montenegro | Podgorica |\n| Netherlands | Amsterdam (leg...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mpletions" \ -H "Content-Type: application/json" \ -d '{ "stream": false, "model": "openai/gpt-oss-20b", "max_tokens": 2000, "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g tokens in /v1/messages Anthropic endpoint if model supports it feature request ### 🚀 The feature, motivation and pitch Currently the Anthropic compatible /v1/messages endpoint doesn't return the reasoning tokens, even...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
