# vllm-project/vllm#7952: [Feature]: Context Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#7952](https://github.com/vllm-project/vllm/issues/7952) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Context Caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Allow saving of kv cache for faster TTFT on long prompts. Another related feature would be to allow a fixed and shared cache across all requests. Perhaps this would be even easier to implement. ### Alternatives I suppose prompt compression, but it's not as quick as context caching. ### Additional context claude and gemini have implemented this. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: feature request ### 🚀 The feature, motivation and pitch Allow saving of kv cache for faster TTFT on long prompts. Another related feature would be to allow a fixed and shared cache across all requests. Perhaps this woul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Context Caching feature request ### 🚀 The feature, motivation and pitch Allow saving of kv cache for faster TTFT on long prompts. Another related feature would be to allow a fixed and shared cache across all...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
