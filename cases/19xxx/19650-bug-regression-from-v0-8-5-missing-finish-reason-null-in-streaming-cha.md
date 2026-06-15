# vllm-project/vllm#19650: [Bug]: (regression from v0.8.5) missing "finish_reason": null in streaming chat completion outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#19650](https://github.com/vllm-project/vllm/issues/19650) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: (regression from v0.8.5) missing "finish_reason": null in streaming chat completion outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Streaming chat completion outputs in openai-compatible serving since vllm==0.9.0 does not include the `"finish_reason": null` field in its HTTP response stream like the following: ```log data: {"id":"chatcmpl-c4eefdc442064e16be757120a2ec7703","object":"chat.completion.chunk","created":1749904375,"model":"meta-llama/llama-4-scout-17b-16e-instruct","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-c4eefdc442064e16be757120a2ec7703","object":"chat.completion.chunk","created":1749904375,"model":"meta-llama/llama-4-scout-17b-16e-instruct","choices":[{"index":0,"delta":{"content":"안","tool_calls":[]}}]} data: {"id":"chatcmpl-c4eefdc442064e16be757120a2ec7703","object":"chat.completion.chunk","created":1749904375,"model":"meta-llama/llama-4-scout-17b-16e-instruct","choices":[{"index":0,"delta":{"content":"녕","tool_calls":[]}}]} ... ``` ### Expected chat completion output (i.e. output from vllm==0.8.5.post1) for comparison: ```log data: {"id":"chatcmpl-0c0dd0fa4fae4544998222ce6edde854","object":"chat.completion.chunk","created":1749904312,"model":"meta-llama/llama-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: be757120a2ec7703","object":"chat.completion.chunk","created":1749904375,"model":"meta-llama/llama-4-scout-17b-16e-instruct","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: (regression from v0.8.5) missing "finish_reason": null in streaming chat completion outputs bug ### Your current environment ### 🐛 Describe the bug Streaming chat completion outputs in openai-compatible serving s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ,"logprobs":null,"finish_reason":null}]} ... ``` According to [the official OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create), `finish_reason` field should be given for each chat completi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
