# vllm-project/vllm#39282: [Feature]: Qwen3.5 训练是否计划支持 Multi-Token Prediction (MTP)

| 字段 | 值 |
| --- | --- |
| Issue | [#39282](https://github.com/vllm-project/vllm/issues/39282) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen3.5 训练是否计划支持 Multi-Token Prediction (MTP)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 我想请教一下，Qwen3.5 的训练流程是否有计划支持 Multi-Token Prediction（MTP）。 根据我目前的观察，现有训练代码中似乎还没有看到比较明确的 MTP 支持，包括： 相关文档说明； 训练参数或配置项； 多 future-token prediction head / loss 的示例实现。 我的使用场景主要是希望在 Qwen3.5 训练栈上探索 MTP，用于后训练 实验； 我主要想确认以下几点： 目前是否已经有支持 MTP 的计划？ 如果有，是否有大致 roadmap 或时间预期？ 感谢。 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Qwen3.5 训练是否计划支持 Multi-Token Prediction (MTP) feature request ### 🚀 The feature, motivation and pitch 我想请教一下，Qwen3.5 的训练流程是否有计划支持 Multi-Token Prediction（MTP）。 根据我目前的观察，现有训练代码中似乎还没有看到比较明确的 MTP 支持，包括： 相关文档说明； 训...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Qwen3.5 训练是否计划支持 Multi-Token Prediction (MTP) feature request ### 🚀 The feature, motivation and pitch 我想请教一下，Qwen3.5 的训练流程是否有计划支持 Multi-Token Prediction（MTP）。 根据我目前的观察，现有训练代码中似乎还没有看到比较明确的 MTP 支持，包括： 相关文档说明； 训...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
