# vllm-project/vllm#1802: Feature request: prompt lookup decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#1802](https://github.com/vllm-project/vllm/issues/1802) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature request: prompt lookup decoding

### Issue 正文摘录

Prompt lookup decoding (PLD) is a variant of speculative decoding that replaces the draft model with a prefix lookup in the current sequence, resulting in a 2-4x throughput boost for input-grounded tasks like summarization and code modification. Because PLD doesn't require a secondary model, it might be easier to implement in VLLM? See https://github.com/apoorvumang/prompt-lookup-decoding for details.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Feature request: prompt lookup decoding feature request;stale Prompt lookup decoding (PLD) is a variant of speculative decoding that replaces the draft model with a prefix lookup in the current sequence, resulting in a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oding (PLD) is a variant of speculative decoding that replaces the draft model with a prefix lookup in the current sequence, resulting in a 2-4x throughput boost for input-grounded tasks like summarization and code modi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: model with a prefix lookup in the current sequence, resulting in a 2-4x throughput boost for input-grounded tasks like summarization and code modification. Because PLD doesn't require a secondary model, it might be easi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
