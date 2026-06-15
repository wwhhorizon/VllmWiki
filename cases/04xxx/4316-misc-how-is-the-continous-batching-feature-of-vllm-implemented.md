# vllm-project/vllm#4316: [Misc]: How is the continous batching feature of vLLM implemented?

| 字段 | 值 |
| --- | --- |
| Issue | [#4316](https://github.com/vllm-project/vllm/issues/4316) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How is the continous batching feature of vLLM implemented?

### Issue 正文摘录

Hi, I'm curious about the imlementation of **continous batching**. It is not mentioned in detail in the vLLM paper, and the code can only use this feature, but there is no detailed code on exactly how it is implemented. Is it a serial execution of the attention layer like Orca, or is it implemented like collapsing all requests within a batch into 1 dimension, then using tree-attention-mask to control valid attention score? Thank you very much!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: How is the continous batching feature of vLLM implemented? stale Hi, I'm curious about the imlementation of **continous batching**. It is not mentioned in detail in the vLLM paper, and the code can only use this...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
