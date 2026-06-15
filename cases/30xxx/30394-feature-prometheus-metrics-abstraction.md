# vllm-project/vllm#30394: [Feature]: Prometheus Metrics Abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#30394](https://github.com/vllm-project/vllm/issues/30394) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prometheus Metrics Abstraction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There is a need for OpenTelemetry metrics support. See this post describing the increasing Prometheus/OpenTelemetry alignment - https://prometheus.io/blog/2024/03/14/commitment-to-opentelemetry Just adding OTel metrics support on top of current state of the project is going to increase maintenance effort. Any metric added to OTel needs to be added to Prometheus and vise-versa. To simplify it - instead of adding metric to a single place, it needs to be added to two places. Because of above reasoning, the idea is to create metrics abstraction so that metrics are maintainable. To change or add new metrics - modification is needed only in one place. User can decide further whether he'd like to use Prometheus based metrics (default) or opt for OTel metrics or both. ### Alternatives _No response_ ### Additional context For more context check this PR https://github.com/vllm-project/vllm/pull/30258 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Prometheus Metrics Abstraction feature request;unstale ### 🚀 The feature, motivation and pitch There is a need for OpenTelemetry metrics support. See this post describing the increasing Prometheus/OpenTelemet...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r add new metrics - modification is needed only in one place. User can decide further whether he'd like to use Prometheus based metrics (default) or opt for OTel metrics or both. ### Alternatives _No response_ ### Addit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 258 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
