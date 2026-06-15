# vllm-project/vllm#2048: Mixtral generation speed performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#2048](https://github.com/vllm-project/vllm/issues/2048) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral generation speed performance.

### Issue 正文摘录

I tried to deploy the Mixtral 7bx8 model on eight T4 GPUs, but the generation speed is only 6 tokens/s, while a 34B model achieves 14 tokens/s. I've heard someone mention that Mixtral 7bx8's generation performance is comparable to a 12B model, but I'm unsure what the issue might be.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Mixtral generation speed performance. I tried to deploy the Mixtral 7bx8 model on eight T4 GPUs, but the generation speed is only 6 tokens/s, while a 34B model achieves 14 tokens/s. I've heard someone mention that Mixtr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
