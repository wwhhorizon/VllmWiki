# vllm-project/vllm#88: Support various sampling parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#88](https://github.com/vllm-project/vllm/issues/88) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support various sampling parameters

### Issue 正文摘录

The parameters such as `repetition_penalty` and `top_k` are often used for sampling. It'd be nice to support them using the HuggingFace logit processors.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: p_k` are often used for sampling. It'd be nice to support them using the HuggingFace logit processors.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
