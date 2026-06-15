# vllm-project/vllm#1743: chatglm3 will generate 'assistant' tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#1743](https://github.com/vllm-project/vllm/issues/1743) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> chatglm3 will generate 'assistant' tokens

### Issue 正文摘录

when i use the api_openai to serve chatglm3, the response will generate 'assistant' first, then return the corrent response. anyone get same error？ example: 你好啊 assistant 你好👋！我是人工智能助手 ChatGLM3-6B，很高兴见到你，欢迎问我任何问题。 hello assistant Hello! How can I help you today?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
