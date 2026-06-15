# vllm-project/vllm#4046: [Bug]: Streaming inference response results cannot be serialized as json normally

| 字段 | 值 |
| --- | --- |
| Issue | [#4046](https://github.com/vllm-project/vllm/issues/4046) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming inference response results cannot be serialized as json normally

### Issue 正文摘录

### Your current environment ```text The output of `Postman` ``` ... data: {"id":"cmpl-154965d939604267b71cfb09c8c24d38","object":"chat.completion.chunk","created":146773,"model":"/models/Baichuan2-13B-chat-FP16","choices":[{"index":0,"delta":{"content":"!"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-154965d939604267b71cfb09c8c24d38","object":"chat.completion.chunk","created":146773,"model":"/models/Baichuan2-13B-chat-FP16","choices":[{"index":0,"delta":{"content":" "},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-154965d939604267b71cfb09c8c24d38","object":"chat.completion.chunk","created":146773,"model":"/models/Baichuan2-13B-chat-FP16","choices":[{"index":0,"delta":{"content":""},"finish_reason":"stop"}],"usage":{"prompt_tokens":30,"total_tokens":264,"completion_tokens":234}} data: [DONE] ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/546e7211684a28bbe53088961b4cf5123e235760/vllm/entrypoints/openai/serving_chat.py#L243 https://github.com/vllm-project/vllm/blob/546e7211684a28bbe53088961b4cf5123e235760/vllm/entrypoints/openai/serving_completion.py#L168 https://github.com/vllm-project/vllm/blob/546e7211684a28bbe53088961b4cf5123e235760/vl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 4267b71cfb09c8c24d38","object":"chat.completion.chunk","created":146773,"model":"/models/Baichuan2-13B-chat-FP16","choices":[{"index":0,"delta":{"content":"!"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
