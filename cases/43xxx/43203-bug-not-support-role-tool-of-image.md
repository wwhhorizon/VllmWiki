# vllm-project/vllm#43203: [Bug]: Not support role tool of image

| 字段 | 值 |
| --- | --- |
| Issue | [#43203](https://github.com/vllm-project/vllm/issues/43203) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Not support role tool of image

### Issue 正文摘录

### Your current environment ## Title Kimi K2.5/K2.6 vision model rejects `image_url` content in `role: "tool"` messages, although image input works in user messages ## Description When serving Kimi K2.5/K2.6 with vLLM OpenAI-compatible Chat Completions API, I found that multimodal `image_url` content is accepted in `role: "user"` messages, but rejected when the same `image_url` content is returned from a tool message using `role: "tool"`. The error says that tool message content only supports text content. I would like to clarify whether this is expected behavior, and if so, whether vLLM plans to support multimodal tool results for vision-capable models such as Kimi K2.5/K2.6. ## Reproduction A tool call flow where the assistant calls a tool, and the tool returns an image: ```json { "role": "tool", "tool_call_id": "functions.get_image:0", "content": [ { "type": "image_url", "image_url": { "url": "https://example.com/image.png" } } ] } ``` ### 🐛 Describe the bug { "role": "tool", "tool_call_id": "functions.get_image:0", "content": [ { "type": "image_url", "image_url": { "url": "https://example.com/image.png" } } ] } ### Before submitting a new issue...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: image bug ### Your current environment ## Title Kimi K2.5/K2.6 vision model rejects `image_url` content in `role: "tool"` messages, although image input works in user messages ## Description When serving Kimi K2.5/K2.6...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
