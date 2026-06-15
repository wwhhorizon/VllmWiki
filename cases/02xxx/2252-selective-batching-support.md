# vllm-project/vllm#2252: Selective batching support

| 字段 | 值 |
| --- | --- |
| Issue | [#2252](https://github.com/vllm-project/vllm/issues/2252) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Selective batching support

### Issue 正文摘录

Hello, Does vLLM currently support Selective batching? In other words, if each sequence in a batch of inputs specifies a different max_new_tokens, can Selective batching be used to obtain varying output lengths within the same batch during generation? Typically, in the traditional batch processing approach, a uniform max value needs to be specified for generating within a batch. Thank you.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ctive batching? In other words, if each sequence in a batch of inputs specifies a different max_new_tokens, can Selective batching be used to obtain varying output lengths within the same batch during generation? Typica...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
