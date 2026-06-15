# vllm-project/vllm#1363: How to deploy vllm model across multiple nodes in kubernetes?

| 字段 | 值 |
| --- | --- |
| Issue | [#1363](https://github.com/vllm-project/vllm/issues/1363) |
| 状态 | closed |
| 标签 |  |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to deploy vllm model across multiple nodes in kubernetes?

### Issue 正文摘录

I've managed to deploy vllm using vllm openai compatible entrypoint with success between all the gpus available in my kubernetes node. However, how i have a question, can i leverage ray between multiple nodes? With different GPU types? I was wondering in order to leverage bigger LLM models. My current cluster has something like 36 gpus, however they're split in sets of 4 gpus per each node.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to deploy vllm model across multiple nodes in kubernetes? I've managed to deploy vllm using vllm openai compatible entrypoint with success between all the gpus available in my kubernetes node. However, how i have a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
