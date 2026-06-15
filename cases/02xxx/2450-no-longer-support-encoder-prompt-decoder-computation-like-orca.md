# vllm-project/vllm#2450: no longer support encoder(prompt) + decoder computation(like ORCA)?

| 字段 | 值 |
| --- | --- |
| Issue | [#2450](https://github.com/vllm-project/vllm/issues/2450) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> no longer support encoder(prompt) + decoder computation(like ORCA)?

### Issue 正文摘录

Hi vllm team. In v0.1.0, There is an implementation of the functionality that when a new prompt comes during decoding, operations except attention are processed in a same batch. https://github.com/vllm-project/vllm/blob/67d96c29fba9b72cb4c4edbc26211c208a00ebdd/vllm/model_executor/layers/attention.py#L121 in v0.2.7, It seems like the prompt and decoing computation are separated. https://github.com/vllm-project/vllm/blob/2e0b6e775756345aa1d39f772c186e00f8c29e92/vllm/model_executor/layers/attention.py#L101 Is this feature no longer supported? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/67d96c29fba9b72cb4c4edbc26211c208a00ebdd/vllm/model_executor/layers/attention.py#L121 in v0.2.7, It seems like the prompt and decoing computation are separated. https://github.com/vllm-project...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: no longer support encoder(prompt) + decoder computation(like ORCA)? Hi vllm team. In v0.1.0, There is an implementation of the functionality that when a new prompt comes during decoding, operations except attention are...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
