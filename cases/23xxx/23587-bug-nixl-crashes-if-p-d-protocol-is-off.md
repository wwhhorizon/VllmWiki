# vllm-project/vllm#23587: [Bug]: NIXL Crashes if P/D Protocol is off

| 字段 | 值 |
| --- | --- |
| Issue | [#23587](https://github.com/vllm-project/vllm/issues/23587) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NIXL Crashes if P/D Protocol is off

### Issue 正文摘录

### Your current environment P/D in a cluster ### 🐛 Describe the bug See: https://llm-d.slack.com/archives/C08T1E128PK/p1756154591908149 If there is an issue in the NIXL setup (e.g. P uses FlashInfer / D uses FlashAttention), we cause the server to crash. We should remove these assets and more gracefully reject using P/D in those cases ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: K/p1756154591908149 If there is an issue in the NIXL setup (e.g. P uses FlashInfer / D uses FlashAttention), we cause the server to crash. We should remove these assets and more gracefully reject using P/D in those case...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: P/D in a cluster ### 🐛 Describe the bug See: https://llm-d.slack.com/archives/C08T1E128PK/p1756154591908149 If there is an issue in the NIXL setup (e.g. P uses FlashInfer / D uses FlashAttention), we cause the server to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: NIXL Crashes if P/D Protocol is off bug;stale ### Your current environment P/D in a cluster ### 🐛 Describe the bug See: https://llm-d.slack.com/archives/C08T1E128PK/p1756154591908149 If there is an issue in the N...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
