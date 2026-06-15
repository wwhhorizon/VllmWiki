# vllm-project/vllm#1773: The effect of the uniformity of sequences in a batch on the performance

| 字段 | 值 |
| --- | --- |
| Issue | [#1773](https://github.com/vllm-project/vllm/issues/1773) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The effect of the uniformity of sequences in a batch on the performance

### Issue 正文摘录

When building a batch，sequences of different lengths are put in. I am wondering does the effectiveness of GPU computing is influenced by the uniformity of sequence lengths？Intuitively it seems the more uniform，the more friendly of GPU computing. Looking for some suggestions, thank you

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: effect of the uniformity of sequences in a batch on the performance When building a batch，sequences of different lengths are put in. I am wondering does the effectiveness of GPU computing is influenced by the uniformity...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
