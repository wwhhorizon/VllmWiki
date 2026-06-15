# vllm-project/vllm#2380: Understanding about LLM class from vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#2380](https://github.com/vllm-project/vllm/issues/2380) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Understanding about LLM class from vllm

### Issue 正文摘录

is LLM class from vllm is asynchronous by nature ? why am i asking this from the [slides](https://docs.google.com/presentation/d/1QL-XPFXiFpDBh86DbEegFXBXFXjix4v032GhShbKf3s/edit#slide=id.g24ad94a0065_0_84) on the first meetup it has mentioned that llm is synchronous rather api_server and openai_server are asynchronous ? if that is true ,how to call the llm model asynchronously ? correct me if i am wrong ! TIA

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d openai_server are asynchronous ? if that is true ,how to call the llm model asynchronously ? correct me if i am wrong ! TIA

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
