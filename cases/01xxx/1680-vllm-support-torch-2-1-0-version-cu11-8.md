# vllm-project/vllm#1680: vllm support torch==2.1.0 version cu11.8?

| 字段 | 值 |
| --- | --- |
| Issue | [#1680](https://github.com/vllm-project/vllm/issues/1680) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm support torch==2.1.0 version cu11.8?

### Issue 正文摘录

I don't see a vllm package in torch cu118 in the [URL](https://download.pytorch.org/whl/cu118)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm support torch==2.1.0 version cu11.8? I don't see a vllm package in torch cu118 in the [URL](https://download.pytorch.org/whl/cu118)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
