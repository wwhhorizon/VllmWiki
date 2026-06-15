# vllm-project/vllm#35165: [Feature]: Add TCP support to MORI KV connector

| 字段 | 值 |
| --- | --- |
| Issue | [#35165](https://github.com/vllm-project/vllm/issues/35165) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add TCP support to MORI KV connector

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is useful for two reasons: 1) Ease of development since IBV capable devices won't be required to develop 2) CI machines don't always have IBV capable cards, so TCP could be used in testing as a backend. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add TCP support to MORI KV connector feature request;stale ### 🚀 The feature, motivation and pitch This is useful for two reasons: 1) Ease of development since IBV capable devices won't be required to develop...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on't always have IBV capable cards, so TCP could be used in testing as a backend. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sear...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: of development since IBV capable devices won't be required to develop 2) CI machines don't always have IBV capable cards, so TCP could be used in testing as a backend. ### Alternatives _No response_ ### Additional conte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: CI machines don't always have IBV capable cards, so TCP could be used in testing as a backend. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
