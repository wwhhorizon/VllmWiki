# vllm-project/vllm#13935: Upgrade to Ray 2.43

| 字段 | 值 |
| --- | --- |
| Issue | [#13935](https://github.com/vllm-project/vllm/issues/13935) |
| 状态 | closed |
| 标签 | ray |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Upgrade to Ray 2.43

### Issue 正文摘录

- Ray 2.41+ has API changes. - Ray 2.42 has a bug that breaks PP in v0 Accordingly, we will wait until Ray 2.43, and upgrade the Ray version in vLLM as well as the APIs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: PP in v0 Accordingly, we will wait until Ray 2.43, and upgrade the Ray version in vLLM as well as the APIs.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
