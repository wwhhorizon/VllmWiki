# vllm-project/vllm#14530: [Feature]: Audit and Update Examples To Use `VLLM_USE_V1=1`

| 字段 | 值 |
| --- | --- |
| Issue | [#14530](https://github.com/vllm-project/vllm/issues/14530) |
| 状态 | closed |
| 标签 | good first issue;feature request;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Audit and Update Examples To Use `VLLM_USE_V1=1`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Many of the examples leverage V0 internals. We should: - raise `NotImplementedError` if `envs.VLLM_USE_V1` with these - convert them to use `V1` if we can ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: udit and Update Examples To Use `VLLM_USE_V1=1` good first issue;feature request;unstale ### 🚀 The feature, motivation and pitch Many of the examples leverage V0 internals. We should: - raise `NotImplementedError` if `e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
