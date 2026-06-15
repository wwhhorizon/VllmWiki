# vllm-project/vllm#25538: [Bug]: performance regression caused by frequently preempting and resuming a request

| 字段 | 值 |
| --- | --- |
| Issue | [#25538](https://github.com/vllm-project/vllm/issues/25538) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: performance regression caused by frequently preempting and resuming a request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/sched/scheduler.py#L473 Allocate slots for `token_budget` (max_num_batched_tokens < prefill_len) tokens, causing the preempted request to be resume and preempted again in the next step due to no enough kvcache to store the long prefill. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: performance regression caused by frequently preempting and resuming a request bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/sched/scheduler....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: performance regression caused by frequently preempting and resuming a request bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/sched/schedu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lm-project/vllm/blob/main/vllm/v1/core/sched/scheduler.py#L473 Allocate slots for `token_budget` (max_num_batched_tokens < prefill_len) tokens, causing the preempted request to be resume and preempted again in the next...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
