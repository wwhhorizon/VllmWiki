# vllm-project/vllm#33089: [Feature]: Support multi-turn conversation for OpenAI Response API

| 字段 | 值 |
| --- | --- |
| Issue | [#33089](https://github.com/vllm-project/vllm/issues/33089) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multi-turn conversation for OpenAI Response API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I wanted to test **GPT-OSS-120B** served via **vLLM** using AI coding agents such as **opencode** and **codex**. For these agents, **tool calling and multi-turn conversations are essential**, and according to OpenAI's documentation, the **`/v1/responses` endpoint** is the recommended API for this use case. #### Observed behavior When configuring both agents (opencode and codex) to call the model through the **`/v1/responses` endpoint**, everything works smoothly for the **first request**: vLLM responds correctly and returns a valid output. However, when continuing the conversation (**multi-turn interaction**), at the very second request, vLLM fails and returns **validation errors**. The failure seems to occur because these agents send the conversation history using the **OpenAI Responses API format**, which vLLM does **not currently support**. vLLM expects inputs formatted according to the **Chat Completions API**: ```json { "messages": [ {"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there!"}, {"role": "user", "content": "How are you?"} ] } ``` The agents send requests using the **Responses API format**: ```json...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ture request ### 🚀 The feature, motivation and pitch I wanted to test **GPT-OSS-120B** served via **vLLM** using AI coding agents such as **opencode** and **codex**. For these agents, **tool calling and multi-turn conve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ally others that rely on this API. ### Steps to reproduce | Agent | Version | Command | Result | | -------- | ------- | -----------------------------------
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: all the model through the **`/v1/responses` endpoint**, everything works smoothly for the **first request**: vLLM responds correctly and returns a valid output. However, when continuing the conversation (**multi-turn in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: , **codex**, and potentially others that rely on this API. ### Steps to reproduce | Agent | Version | Command | Result | | -------- | ------- | -----------
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: Support multi-turn conversation for OpenAI Response API feature request ### 🚀 The feature, motivation and pitch I wanted to test **GPT-OSS-120B** served via **vLLM** using AI coding agents such as **opencode**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
