# vllm-project/vllm#19758: [Feature]: Remove cupy dependency for multi-node Ray deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#19758](https://github.com/vllm-project/vllm/issues/19758) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove cupy dependency for multi-node Ray deployment

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Ray uses cupy under the hood for inter-GPU communication in compiled graphs. We should remove the dependency by creating the collective group using existing vllm APIs and providing a handle to the group to Ray. ### Alternatives - Ray could use provide its own NCCL bindings - note this would not support non-NVIDIA GPUs ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Remove cupy dependency for multi-node Ray deployment feature request;ray;stale ### 🚀 The feature, motivation and pitch Ray uses cupy under the hood for inter-GPU communication in compiled graphs. We should re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Remove cupy dependency for multi-node Ray deployment feature request;ray;stale ### 🚀 The feature, motivation and pitch Ray uses cupy under the hood for inter-GPU communication in compiled graphs. We should re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
