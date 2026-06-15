# vllm-project/vllm#2596: Can't recreate offline inference w/ prefix example

| 字段 | 值 |
| --- | --- |
| Issue | [#2596](https://github.com/vllm-project/vllm/issues/2596) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can't recreate offline inference w/ prefix example

### Issue 正文摘录

When I tried running that example code I got this error: TypeError: generate() got an unexpected keyword argument 'prefix_pos' Is prefix_pos currently not supported? I installed vllm via "pip install vllm" so it should be whatever version is the current python package.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: keyword argument 'prefix_pos' Is prefix_pos currently not supported? I installed vllm via "pip install vllm" so it should be whatever version is the current python package.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
