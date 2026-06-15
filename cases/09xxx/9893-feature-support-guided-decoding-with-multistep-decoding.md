# vllm-project/vllm#9893: [Feature]: Support guided decoding with multistep decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#9893](https://github.com/vllm-project/vllm/issues/9893) |
| 状态 | closed |
| 标签 | feature request;structured-output;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support guided decoding with multistep decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch See https://github.com/vllm-project/vllm/issues/8985. It would be great if we could get the speedup from multi-step decoding without having to disallow users from using guided decoding. I have no idea how feasible that is to do, but if anybody has a sketch of how it would be done I could be up for learning and helping to implement. I'm mostly opening this issue so it's documented and I can link it from the feature compatibility matrix in the docs. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support guided decoding with multistep decoding feature request;structured-output;stale ### 🚀 The feature, motivation and pitch See https://github.com/vllm-project/vllm/issues/8985. It would be great if we co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to implement. I'm mostly opening this issue so it's documented and I can link it from the feature compatibility matrix in the docs. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
