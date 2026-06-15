# vllm-project/vllm#2150: torch.distributed.all_reduce does not free memory

| 字段 | 值 |
| --- | --- |
| Issue | [#2150](https://github.com/vllm-project/vllm/issues/2150) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> torch.distributed.all_reduce does not free memory

### Issue 正文摘录

I've visualized the memory usage: * llama 7B, TP=1 The activation memory is reused after every layer. * llama-70B, TP=8 **However, when using TP, the activation memory for all reduce is not reused** _Originally posted by @WoosukKwon in https://github.com/vllm-project/vllm/pull/2031#discussion_r1429046645_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: all_reduce does not free memory bug I've visualized the memory usage: * llama 7B, TP=1 The activation memory is reused after every layer. * llama-70B, TP=8 **However, when using TP, the activation memory for all reduce...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
