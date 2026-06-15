# vllm-project/vllm#72: Support FP32

| 字段 | 值 |
| --- | --- |
| Issue | [#72](https://github.com/vllm-project/vllm/issues/72) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support FP32

### Issue 正文摘录

Yes, it does. It is our attention kernel that does not support FP32. More precisely, our attention kernel currently does not support some block sizes when FP32 is used. I will fix this in the future. _Originally posted by @WoosukKwon in https://github.com/WoosukKwon/cacheflow/pull/70#discussion_r1185857849_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: it does. It is our attention kernel that does not support FP32. More precisely, our attention kernel currently does not support some block sizes when FP32 is used. I will fix this in the future. _Originally posted by @W...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 32. More precisely, our attention kernel currently does not support some block sizes when FP32 is used. I will fix this in the future. _Originally posted by @WoosukKwon in https://github.com/WoosukKwon/cacheflow/pull/70...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
