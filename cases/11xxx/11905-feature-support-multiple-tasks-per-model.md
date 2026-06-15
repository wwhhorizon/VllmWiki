# vllm-project/vllm#11905: [Feature]: Support Multiple Tasks Per Model

| 字段 | 值 |
| --- | --- |
| Issue | [#11905](https://github.com/vllm-project/vllm/issues/11905) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Multiple Tasks Per Model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Requesting this for **V1** #11862 The idea is pretty simple, it would be nice to be able to, e.g., get generations and embeddings out of a single model. An example use case is when you have a LoRA for generation and a LoRA for embedding on top of the same base model. Deploying two vLLM servers is really inefficient for accomplishing this. ### Alternatives A lesser feature would be one task per LoRA, but it's better to be general if possible. ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Multiple Tasks Per Model feature request;unstale ### 🚀 The feature, motivation and pitch Requesting this for **V1** #11862 The idea is pretty simple, it would be nice to be able to, e.g., get generati...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n top of the same base model. Deploying two vLLM servers is really inefficient for accomplishing this. ### Alternatives A lesser feature would be one task per LoRA, but it's better to be general if possible. ### Additio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support Multiple Tasks Per Model feature request;unstale ### 🚀 The feature, motivation and pitch Requesting this for **V1** #11862 The idea is pretty simple, it would be nice to be able to, e.g., get generati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
