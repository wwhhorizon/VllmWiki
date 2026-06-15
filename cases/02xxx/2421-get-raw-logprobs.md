# vllm-project/vllm#2421: Get raw logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#2421](https://github.com/vllm-project/vllm/issues/2421) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Get raw logprobs

### Issue 正文摘录

Is there a way to get the raw logprobs like in TGI instead of softmax(logprobs)?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
