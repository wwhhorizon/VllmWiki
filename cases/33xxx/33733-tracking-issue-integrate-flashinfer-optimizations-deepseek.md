# vllm-project/vllm#33733: [Tracking issue]: Integrate flashinfer optimizations (DeepSeek)

| 字段 | 值 |
| --- | --- |
| Issue | [#33733](https://github.com/vllm-project/vllm/issues/33733) |
| 状态 | open |
| 标签 | performance;feature request;stale;deepseek |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking issue]: Integrate flashinfer optimizations (DeepSeek)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Nonexhaustive list of new flashinfer features that may be integrated into vLLM. - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2019 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2099 - wip: https://github.com/vllm-project/vllm/pull/33890 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2233 - wip: https://github.com/vllm-project/vllm/pull/32957 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2037 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2398 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2035 and https://github.com/flashinfer-ai/flashinfer/pull/2352 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/2102 - wip: https://github.com/vllm-project/vllm/pull/32217 - [ ] https://github.com/flashinfer-ai/flashinfer/pull/1213 - wip: @hjjq ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ssue]: Integrate flashinfer optimizations (DeepSeek) performance;feature request;stale;deepseek ### 🚀 The feature, motivation and pitch Nonexhaustive list of new flashinfer features that may be integrated into vLLM. - [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Tracking issue]: Integrate flashinfer optimizations (DeepSeek) performance;feature request;stale;deepseek ### 🚀 The feature, motivation and pitch Nonexhaustive list of new flashinfer features that may be integrated int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
