# vllm-project/vllm#23: Add an option to disable Ray when using a single GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#23](https://github.com/vllm-project/vllm/issues/23) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add an option to disable Ray when using a single GPU

### Issue 正文摘录

When working with a single GPU, Ray is not useful. Therefore, it would be beneficial to have an option to disable Ray in such scenarios.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rking with a single GPU, Ray is not useful. Therefore, it would be beneficial to have an option to disable Ray in such scenarios.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
