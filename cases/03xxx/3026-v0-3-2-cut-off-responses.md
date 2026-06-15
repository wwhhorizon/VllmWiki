# vllm-project/vllm#3026: v0.3.2 cut off responses

| 字段 | 值 |
| --- | --- |
| Issue | [#3026](https://github.com/vllm-project/vllm/issues/3026) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> v0.3.2 cut off responses

### Issue 正文摘录

It seems like sometimes (not 100% reproducible) the responses in 0.3.2 gets cut off at the last token when using stop ID and stop words. It happens sometimes, but cannot figure out a 100% reliable trigger. Something to flag in case others run into it. It happened on default (non-eager mode).

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: v0.3.2 cut off responses It seems like sometimes (not 100% reproducible) the responses in 0.3.2 gets cut off at the last token when using stop ID and stop words. It happens sometimes, but cannot figure out a 100% reliab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: v0.3.2 cut off responses It seems like sometimes (not 100% reproducible) the responses in 0.3.2 gets cut off at the last token when using stop ID and stop words. It happens sometimes, but cannot figure out a 100% reliab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
