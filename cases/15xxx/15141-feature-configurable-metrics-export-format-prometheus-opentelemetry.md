# vllm-project/vllm#15141: [Feature]: Configurable metrics export format - Prometheus, OpenTelemetry

| 字段 | 值 |
| --- | --- |
| Issue | [#15141](https://github.com/vllm-project/vllm/issues/15141) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Configurable metrics export format - Prometheus, OpenTelemetry

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We would like to export metrics from vLLM in the OpenTelemetry format with delta temporality (Prometheus uses only cumulative temporality). For instance Dynatrace can ingest only delta temporality metrics. ### Alternatives Deploy an OpenTelemetry collector with prometheus receiver and cumulativetodelta processor as a sidecar to vLLM and then export the metrics from the collector. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Configurable metrics export format - Prometheus, OpenTelemetry feature request;stale ### 🚀 The feature, motivation and pitch We would like to export metrics from vLLM in the OpenTelemetry format with delta te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Configurable metrics export format - Prometheus, OpenTelemetry feature request;stale ### 🚀 The feature, motivation and pitch We would like to export metrics from vLLM in the OpenTelemetry format with delta temporality...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
