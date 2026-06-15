# vllm-project/vllm#19268: [Feature]: Under non-streaming output, add background heartbeat detection

| 字段 | 值 |
| --- | --- |
| Issue | [#19268](https://github.com/vllm-project/vllm/issues/19268) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Under non-streaming output, add background heartbeat detection

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Under stream output, when the client actively disconnects, the server can capture it and then release the resources. Under non-streaming output, it is hoped that background heartbeat detection can be added to monitor the client status and actively release resources ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Under non-streaming output, add background heartbeat detection feature request;stale ### 🚀 The feature, motivation and pitch Under stream output, when the client actively disconnects, the server can capture it and the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
