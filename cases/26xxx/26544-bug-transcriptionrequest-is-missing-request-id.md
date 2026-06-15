# vllm-project/vllm#26544: [Bug]: TranscriptionRequest is missing `request_id`

| 字段 | 值 |
| --- | --- |
| Issue | [#26544](https://github.com/vllm-project/vllm/issues/26544) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TranscriptionRequest is missing `request_id`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Ref: https://github.com/vllm-project/vllm/blob/c6187f55f7c4844ed9ff5630d41114cbe6fccb6b/vllm/entrypoints/openai/protocol.py#L2484 The protocol types should have an attached request ID for integration with external load balancers, ref: https://github.com/vllm-project/vllm/pull/21009 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: TranscriptionRequest is missing `request_id` bug;stale ### Your current environment ### 🐛 Describe the bug Ref: https://github.com/vllm-project/vllm/blob/c6187f55f7c4844ed9ff5630d41114cbe6fccb6b/vllm/entrypoints/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 009 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
