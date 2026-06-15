# vllm-project/vllm#2051: [bug] chatglm3-6b No corresponding template chat-template

| 字段 | 值 |
| --- | --- |
| Issue | [#2051](https://github.com/vllm-project/vllm/issues/2051) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [bug] chatglm3-6b No corresponding template chat-template

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/main/examples/template_chatml.jinja This template is suitable for chatglm2, but not suitable for chatglm3. The new template address document is. https://github.com/THUDM/ChatGLM3/blob/main/PROMPT.md

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
