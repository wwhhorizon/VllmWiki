# vllm-project/vllm#35332: [Feature]: Profiler num_steps

| 字段 | 值 |
| --- | --- |
| Issue | [#35332](https://github.com/vllm-project/vllm/issues/35332) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Profiler num_steps

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `/start_profile` and `/stop_profile` are simple toggles with no parameters, some extra switchs (num_steps, merge_profiles, etc.) would be useful to profile a running server. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Profiler num_steps feature request;stale ### 🚀 The feature, motivation and pitch `/start_profile` and `/stop_profile` are simple toggles with no parameters, some extra switchs (num_steps, merge_profiles, etc....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Profiler num_steps feature request;stale ### 🚀 The feature, motivation and pitch `/start_profile` and `/stop_profile` are simple toggles with no parameters, some extra switchs (num_steps, merge_profiles, etc....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
