# vllm-project/vllm#1414: Any way to cache prefix across different queries?

| 字段 | 值 |
| --- | --- |
| Issue | [#1414](https://github.com/vllm-project/vllm/issues/1414) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Any way to cache prefix across different queries?

### Issue 正文摘录

vllm does not cache prefixes across different queries. That is, if one query is "Here is a recipe for making cakes. The cake we want to make is a lemon cake" and the other query is "Here is a recipe for making cakes. The cake we want to make is a strawberry cake" when it encounters the second query, it does not make use of its computations for the first query. I understand vllm does not want to support this. But, I have a use case which my queries have lots of shared prefixes. I want to ask how hard it would be for me to change the vllm implementation to support this feature? What a rough sketch of this idea would look like?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: refixes across different queries. That is, if one query is "Here is a recipe for making cakes. The cake we want to make is a lemon cake" and the other query is "Here is a recipe for making cakes. The cake we want to mak...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
