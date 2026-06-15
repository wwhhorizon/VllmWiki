# vllm-project/vllm#14168: [RFC]: Deprecate `max_num_generation_tokens`

| 字段 | 值 |
| --- | --- |
| Issue | [#14168](https://github.com/vllm-project/vllm/issues/14168) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecate `max_num_generation_tokens`

### Issue 正文摘录

### Motivation. Said by @robertgshaw2-redhat https://github.com/vllm-project/vllm/pull/14055#issuecomment-2695114713 ### Proposed Change. As part of v1, we should deprecate `max_num_generation_tokens`. ### Feedback Period. When agreed _if_ this change should be made. ### CC List. @robertgshaw2-redhat @markmc ### Any Other Things. I will do this if interested. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Deprecate `max_num_generation_tokens` RFC;stale ### Motivation. Said by @robertgshaw2-redhat https://github.com/vllm-project/vllm/pull/14055#issuecomment-2695114713 ### Proposed Change. As part of v1, we should d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
