# vllm-project/vllm#29126: [Feature]: Batch invariant: Enable TRITON_MLA with prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#29126](https://github.com/vllm-project/vllm/issues/29126) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Batch invariant: Enable TRITON_MLA with prefix-caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch A follow up issue for https://github.com/vllm-project/vllm/pull/29125 Developing TritonMLA kernel with prefix-caching support for batch invariant ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Batch invariant: Enable TRITON_MLA with prefix-caching feature request;stale ### 🚀 The feature, motivation and pitch A follow up issue for https://github.com/vllm-project/vllm/pull/29125 Developing TritonMLA k...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Batch invariant: Enable TRITON_MLA with prefix-caching feature request;stale ### 🚀 The feature, motivation and pitch A follow up issue for https://github.com/vllm-project/vllm/pull/29125 Developing TritonMLA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
