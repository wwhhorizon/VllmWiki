# vllm-project/vllm#13792: [Feature]: [V1] Parallel sampling should support metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#13792](https://github.com/vllm-project/vllm/issues/13792) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [V1] Parallel sampling should support metrics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch PR #10980 added parallel sampling support. Currently, the v1 engine's parallel sampling capability does not support metrics: a request with `n>1` returns a request output with `null`/`None` in the metrics field. The desired behavior is for parallel sampling request outputs to include metrics; this may require defining how we want metrics to appear for parallel sampling requests in v1. ### Alternatives Currently a user must account for parallel sampling request outputs having no metrics. ### Additional context I was responsible for #10980 ; metrics support was challenging because each child request passes through the engine separately & accrues its own metrics. It was unclear how to synthesize one parent request metrics data structure from `n` child request metrics data structures, in part because I was not clear on the spec for how metrics are supposed to appear for parallel sampling requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently ask...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: parallel sampling support. Currently, the v1 engine's parallel sampling capability does not support metrics: a request with `n>1` returns a request output with `null`/`None` in the metrics field. The desired behavior is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: [V1] Parallel sampling should support metrics feature request;unstale ### 🚀 The feature, motivation and pitch PR #10980 added parallel sampling support. Currently, the v1 engine's parallel sampling capability...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
