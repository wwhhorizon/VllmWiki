# vllm-project/vllm#19073: [Feature]: Metal support

| 字段 | 值 |
| --- | --- |
| Issue | [#19073](https://github.com/vllm-project/vllm/issues/19073) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Metal support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With current apple's hardware (especially with the latest Mac studio's unified memory), we believe vLLM support for metal is a must. Do you have any plans to add this anytime soon? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Metal support feature request;unstale ### 🚀 The feature, motivation and pitch With current apple's hardware (especially with the latest Mac studio's unified memory), we believe vLLM support for metal is a mus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 🚀 The feature, motivation and pitch With current apple's hardware (especially with the latest Mac studio's unified memory), we believe vLLM support for metal is a must. Do you have any plans to add this anytime soon? ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tivation and pitch With current apple's hardware (especially with the latest Mac studio's unified memory), we believe vLLM support for metal is a must. Do you have any plans to add this anytime soon? ### Alternatives _N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
