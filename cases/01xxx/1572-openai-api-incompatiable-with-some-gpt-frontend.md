# vllm-project/vllm#1572: OpenAI API incompatiable with some GPT Frontend

| 字段 | 值 |
| --- | --- |
| Issue | [#1572](https://github.com/vllm-project/vllm/issues/1572) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> OpenAI API incompatiable with some GPT Frontend

### Issue 正文摘录

- The API that used by https://github.com/Yidadaa/ChatGPT-Next-Web is `/v1/chat/completions?xxx` - The API Server created by vllm offerring api like `/v1/completions?xxx` Why is that? Can't VLLM load model for chatting purpose?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m offerring api like `/v1/completions?xxx` Why is that? Can't VLLM load model for chatting purpose?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
