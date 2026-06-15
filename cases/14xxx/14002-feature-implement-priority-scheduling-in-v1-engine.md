# vllm-project/vllm#14002: [Feature]: Implement Priority Scheduling In V1 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#14002](https://github.com/vllm-project/vllm/issues/14002) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implement Priority Scheduling In V1 Engine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In V0, we support request priority. I would like to see this in V1 cc @WoosukKwon ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature]: Implement Priority Scheduling In V1 Engine help wanted;feature request ### 🚀 The feature, motivation and pitch In V0, we support request priority. I would like to see this in V1 cc @WoosukKwon ### Alternatives...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
