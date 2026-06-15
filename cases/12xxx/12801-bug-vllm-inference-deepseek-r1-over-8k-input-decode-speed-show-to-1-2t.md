# vllm-project/vllm#12801: [Bug]: vllm inference deepseek r1 over 8k input ，decode speed show to 1.2tok/s

| 字段 | 值 |
| --- | --- |
| Issue | [#12801](https://github.com/vllm-project/vllm/issues/12801) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm inference deepseek r1 over 8k input ，decode speed show to 1.2tok/s

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm inference deepseek r1 over 8k input ，decode speed show to 1.2tok/s ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm inference deepseek r1 over 8k input ，decode speed show to 1.2tok/s bug;stale ### Your current environment ### 🐛 Describe the bug vllm inference deepseek r1 over 8k input ，decode speed show to 1.2tok/s ### Be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: k/s ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
