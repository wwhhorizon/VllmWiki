# vllm-project/vllm#30252: [Feature]: OpenTelemetry Metrics Support

| 字段 | 值 |
| --- | --- |
| Issue | [#30252](https://github.com/vllm-project/vllm/issues/30252) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: OpenTelemetry Metrics Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Problem: vLLM currently only supports Prometheus metrics, which require: - External scrapers to pull metrics from each instance - Direct network access to vLLM instances for scraping - Manual service discovery and configuration Solution: OpenTelemetry provides: - Push-based metrics export to centralized collectors - Standardized protocol (OTLP) supported by major observability platforms - Simplified deployment in containerized/distributed environments - Unified observability with traces and logs in OTel-native stacks ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: OpenTelemetry Metrics Support feature request;stale ### 🚀 The feature, motivation and pitch Problem: vLLM currently only supports Prometheus metrics, which require: - External scrapers to pull metrics from ea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: k access to vLLM instances for scraping - Manual service discovery and configuration Solution: OpenTelemetry provides: - Push-based metrics export to centralized collectors - Standardized protocol (OTLP) supported by ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
