# vllm-project/vllm#1582: how to use chat function

| 字段 | 值 |
| --- | --- |
| Issue | [#1582](https://github.com/vllm-project/vllm/issues/1582) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to use chat function

### Issue 正文摘录

I found that vllm could only use the generate method. like llm.generate(prompts, sampling_params)..I now want to use the chat method of qwen-chat-7b like llm.chat(prompts, sampling_params)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: generate(prompts, sampling_params)..I now want to use the chat method of qwen-chat-7b like llm.chat(prompts, sampling_params)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
