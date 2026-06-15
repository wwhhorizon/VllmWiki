# vllm-project/vllm#42840: [Feature]: shuffle safetensor weight files

| 字段 | 值 |
| --- | --- |
| Issue | [#42840](https://github.com/vllm-project/vllm/issues/42840) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: shuffle safetensor weight files

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### 1.Target improve startup speed in big EP scenario. ### Implementation safetenstor files are randomly shuffled based on the distributed rank, which can improve weight loading speed in startup scenarios. This reduces I/O contention by ensuring different ranks load different files in a randomized order. ### Test Result device: NPU A3 model: deepseek v3.1 p instance: 1 d instance: 1 Longing weights took **1463** senconds =>Longing weights took **101** senconds ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: fferent files in a randomized order. ### Test Result device: NPU A3 model: deepseek v3.1 p instance: 1 d instance: 1 Longing weights took **1463** senconds =>Longing weights took **101** senconds ### Alternatives _No re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: shuffle safetensor weight files feature request ### 🚀 The feature, motivation and pitch ### 1.Target improve startup speed in big EP scenario. ### Implementation safetenstor files are randomly shuffled based...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ring different ranks load different files in a randomized order. ### Test Result device: NPU A3 model: deepseek v3.1 p instance: 1 d instance: 1 Longing weights took **1463** senconds =>Longing weights took **101** senc...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
