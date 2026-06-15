# vllm-project/vllm#16297: [Feature]: Can you provide a formula for gpu memory usage when deploying a model using VLLM, while providing the number of model parameters, online text length, batchsize, and quantization accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#16297](https://github.com/vllm-project/vllm/issues/16297) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Can you provide a formula for gpu memory usage when deploying a model using VLLM, while providing the number of model parameters, online text length, batchsize, and quantization accuracy

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Before the project starts, it is necessary to estimate the equipment resources ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: meters, online text length, batchsize, and quantization accuracy feature request;stale ### 🚀 The feature, motivation and pitch Before the project starts, it is necessary to estimate the equipment resources ### Alternati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ber of model parameters, online text length, batchsize, and quantization accuracy feature request;stale ### 🚀 The feature, motivation and pitch Before the project starts, it is necessary to estimate the equipment resour...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ber of model parameters, online text length, batchsize, and quantization accuracy feature request;stale ### 🚀 The feature, motivation and pitch Before the project starts, it is necessary to estimate the equipment resour...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: iding the number of model parameters, online text length, batchsize, and quantization accuracy feature request;stale ### 🚀 The feature, motivation and pitch Before the project starts, it is necessary to estimate the equ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
