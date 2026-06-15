# vllm-project/vllm#2943: Speculative Streaming: Fast LLM Inference without Auxiliary Models

| 字段 | 值 |
| --- | --- |
| Issue | [#2943](https://github.com/vllm-project/vllm/issues/2943) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Speculative Streaming: Fast LLM Inference without Auxiliary Models

### Issue 正文摘录

This might be of interest: https://arxiv.org/pdf/2402.11131.pdf

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Speculative Streaming: Fast LLM Inference without Auxiliary Models feature request;stale This might be of interest: https://arxiv.org/pdf/2402.11131.pdf
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Speculative Streaming: Fast LLM Inference without Auxiliary Models feature request;stale This might be of interest: https://arxiv.org/pdf/2402.11131.pdf

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
