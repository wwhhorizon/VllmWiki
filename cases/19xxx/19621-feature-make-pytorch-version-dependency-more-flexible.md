# vllm-project/vllm#19621: [Feature]: Make pytorch version dependency more flexible

| 字段 | 值 |
| --- | --- |
| Issue | [#19621](https://github.com/vllm-project/vllm/issues/19621) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make pytorch version dependency more flexible

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For reinforcement learning, we usually run pytorch training environment along with vllm for rollout. Latest pytorch version is 2.7.1 which contains some bug fixes to 2.7.0. We'd like to use the latest version on the training side. However vllm strictly pins to 2.7.0 and causes difficulties on project dependency installation. Can vllm adopt something like `^2.7.0` to provide a little flexibility for its dependencies? This would help users introduce bug fix release versions of dependency packages. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Make pytorch version dependency more flexible feature request;stale ### 🚀 The feature, motivation and pitch For reinforcement learning, we usually run pytorch training environment along with vllm for rollout....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Make pytorch version dependency more flexible feature request;stale ### 🚀 The feature, motivation and pitch For reinforcement learning, we usually run pytorch training environment along with vllm for rollout....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: usually run pytorch training environment along with vllm for rollout. Latest pytorch version is 2.7.1 which contains some bug fixes to 2.7.0. We'd like to use the latest version on the training side. However vllm strict...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
