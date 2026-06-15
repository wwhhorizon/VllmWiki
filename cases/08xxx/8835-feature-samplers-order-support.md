# vllm-project/vllm#8835: [Feature]: Samplers Order support

| 字段 | 值 |
| --- | --- |
| Issue | [#8835](https://github.com/vllm-project/vllm/issues/8835) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Samplers Order support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Many local inference model frameworks currently have a sequential configuration for samplers. In a discussion I saw on [Reddit,](https://www.reddit.com/r/LocalLLaMA/comments/17vonjo/your_settings_are_probably_hurting_your_model_why/) it was mentioned that the numerical configuration and order of samplers can affect the model's performance. Could we add a request parameter to control the execution order of the samplers ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: uest;stale ### 🚀 The feature, motivation and pitch Many local inference model frameworks currently have a sequential configuration for samplers. In a discussion I saw on [Reddit,](https://www.reddit.com/r/LocalLLaMA/com...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: settings_are_probably_hurting_your_model_why/) it was mentioned that the numerical configuration and order of samplers can affect the model's performance. Could we add a request parameter to control the execution order...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Samplers Order support feature request;stale ### 🚀 The feature, motivation and pitch Many local inference model frameworks currently have a sequential configuration for samplers. In a discussion I saw on [Red...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
