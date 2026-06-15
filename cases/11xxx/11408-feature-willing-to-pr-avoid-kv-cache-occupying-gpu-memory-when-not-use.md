# vllm-project/vllm#11408: [Feature]: (Willing to PR) Avoid KV cache occupying GPU memory when not used

| 字段 | 值 |
| --- | --- |
| Issue | [#11408](https://github.com/vllm-project/vllm/issues/11408) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: (Willing to PR) Avoid KV cache occupying GPU memory when not used

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi thank you for the library! The use case is that, when doing online PPO, I hope to use vllm to generate llm completions, and then use RL to do gradient descent on those completions. The problem is, to do this on a single GPU, the timeline is "vllm generate - Torch backward - repeat it". Thus, when torch doing backprop, I hope vllm can free its KV cache memory consumption, otherwise torch will not have enough memory. Thanks for any suggestions! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: (Willing to PR) Avoid KV cache occupying GPU memory when not used feature request;stale ### 🚀 The feature, motivation and pitch Hi thank you for the library! The use case is that, when doing online PPO, I hop...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Willing to PR) Avoid KV cache occupying GPU memory when not used feature request;stale ### 🚀 The feature, motivation and pitch Hi thank you for the library! The use case is that, when doing online PPO, I hope to use vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
