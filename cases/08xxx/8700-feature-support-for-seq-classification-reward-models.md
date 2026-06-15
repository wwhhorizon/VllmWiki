# vllm-project/vllm#8700: [Feature]: Support for Seq classification/Reward models

| 字段 | 值 |
| --- | --- |
| Issue | [#8700](https://github.com/vllm-project/vllm/issues/8700) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Seq classification/Reward models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Verifier/reward models are going to be very important moving forward for building: - High quality synthetic data pipelines - Verifying model reasoning - Multi agent systems Could we add support for sequence classification models like Skywork/Skywork-Reward-Llama-3.1-8B ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ature, motivation and pitch Verifier/reward models are going to be very important moving forward for building: - High quality synthetic data pipelines - Verifying model reasoning - Multi agent systems Could we add suppo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support for Seq classification/Reward models feature request ### 🚀 The feature, motivation and pitch Verifier/reward models are going to be very important moving forward for building: - High quality synthetic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for Seq classification/Reward models feature request ### 🚀 The feature, motivation and pitch Verifier/reward models are going to be very important moving forward for building: - High quality synthetic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
