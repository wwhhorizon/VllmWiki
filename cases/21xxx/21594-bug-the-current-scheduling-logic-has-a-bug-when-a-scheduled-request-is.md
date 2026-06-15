# vllm-project/vllm#21594: [Bug]: The current scheduling logic has a bug: when a scheduled request is evicted, ...

| 字段 | 值 |
| --- | --- |
| Issue | [#21594](https://github.com/vllm-project/vllm/issues/21594) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The current scheduling logic has a bug: when a scheduled request is evicted, ...

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a preempted request has already been scheduled, critical state-tracking operations fail to roll back, including updates to: - `scheduled_running_reqs` - `req_to_new_block_ids` - `num_scheduled_tokens` This inconsistency causes various anomalies. ### Operations involved in the scheduled request:： ### When releasing, only block resources are released:： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: The current scheduling logic has a bug: when a scheduled request is evicted, ... bug;stale ### Your current environment ### 🐛 Describe the bug When a preempted request has already been scheduled, critical state-t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: back, including updates to: - `scheduled_running_reqs` - `req_to_new_block_ids` - `num_scheduled_tokens` This inconsistency causes various anomalies. ### Operations involved in the scheduled request:： ### When releasing...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
