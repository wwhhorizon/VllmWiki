# vllm-project/vllm#1850: Profile and optimize list operations in scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#1850](https://github.com/vllm-project/vllm/issues/1850) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Profile and optimize list operations in scheduling

### Issue 正文摘录

BTW, we are considering using Numpy to reduce the list operations. I believe this can be done in another PR. _Originally posted by @WoosukKwon in https://github.com/vllm-project/vllm/pull/1843#discussion_r1410054638_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Profile and optimize list operations in scheduling performance BTW, we are considering using Numpy to reduce the list operations. I believe this can be done in another PR. _Originally posted by @WoosukKwon in https://gi

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
