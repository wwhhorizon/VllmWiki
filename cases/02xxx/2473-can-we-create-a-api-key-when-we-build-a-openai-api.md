# vllm-project/vllm#2473: Can we create a api_key when we build a openai api?

| 字段 | 值 |
| --- | --- |
| Issue | [#2473](https://github.com/vllm-project/vllm/issues/2473) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can we create a api_key when we build a openai api?

### Issue 正文摘录

目前创建openai-compatible api后，调用api时都是用openai_api_key = "EMPTY"。我们在创建api时可以生成一个唯一的api_key吗？

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Can we create a api_key when we build a openai api? 目前创建openai-compatible api后，调用api时都是用openai_api_key = "EMPTY"。我们在创建api时可以生成一个唯一的api_key吗？

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
