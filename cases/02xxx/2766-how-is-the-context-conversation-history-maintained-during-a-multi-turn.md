# vllm-project/vllm#2766: How is the context (conversation history) maintained during a multi-turn conversation ? 

| 字段 | 值 |
| --- | --- |
| Issue | [#2766](https://github.com/vllm-project/vllm/issues/2766) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How is the context (conversation history) maintained during a multi-turn conversation ? 

### Issue 正文摘录

Hi, Thanks for this awesome repository. I'm curious to know the following, 1. maximum context length (including previous conversation history) supported during a multi-turn conversation. 2. How is it handled in the case of vLLM? 3. Is the conversation history maintained similar to the Langchain (Memory Buffer, Summary Buffer, Context window buffer, Hybrid)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
