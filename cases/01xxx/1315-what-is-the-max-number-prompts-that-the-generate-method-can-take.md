# vllm-project/vllm#1315: What is the max number prompts that the generate() method can take

| 字段 | 值 |
| --- | --- |
| Issue | [#1315](https://github.com/vllm-project/vllm/issues/1315) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What is the max number prompts that the generate() method can take

### Issue 正文摘录

What is the max number prompts that the llm.generate() method can take? I know vllm uses continus batching, but I want to dobule check if we can feed any num of prompts for this method

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
