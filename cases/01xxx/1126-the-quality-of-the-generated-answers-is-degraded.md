# vllm-project/vllm#1126: The quality of the generated answers is degraded

| 字段 | 值 |
| --- | --- |
| Issue | [#1126](https://github.com/vllm-project/vllm/issues/1126) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The quality of the generated answers is degraded

### Issue 正文摘录

I use baichuan2 as llm. When inputting long text, although the speed is improved, the quality of the generated answers has declined. Some people say that it is caused by different sampling during generation. How can I modify it?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
