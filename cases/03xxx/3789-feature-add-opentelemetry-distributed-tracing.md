# vllm-project/vllm#3789: [Feature]: Add OpenTelemetry distributed tracing

| 字段 | 值 |
| --- | --- |
| Issue | [#3789](https://github.com/vllm-project/vllm/issues/3789) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add OpenTelemetry distributed tracing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This proposal suggests adding distributed tracing with [OepnTelemetry](https://opentelemetry.io/), which will enable operators to export traces in a standard protocol and seamlessly connect them with visualization tools such as [Jaeger](https://www.jaegertracing.io/), [Zipkin](https://zipkin.io/) and [Instana](https://www.ibm.com/products/instana/opentelemetry) As an initial implementation, I suggest emitting a trace for each request, including the following data: * Model name * Request ID * Sampling params * Latency * Number of input tokens * Number of generated tokens This approach will greatly enhance the observability and troubleshooting capabilities of vLLM. I am willing to work on this and contribute it to the community. I welcome any feedback or suggestions. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Add OpenTelemetry distributed tracing feature request ### 🚀 The feature, motivation and pitch This proposal suggests adding distributed tracing with [OepnTelemetry](https://opentelemetry.io/), which will enab...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gest emitting a trace for each request, including the following data: * Model name * Request ID * Sampling params * Latency * Number of input tokens * Number of generated tokens This approach will greatly enhance the ob...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add OpenTelemetry distributed tracing feature request ### 🚀 The feature, motivation and pitch This proposal suggests adding distributed tracing with [OepnTelemetry](https://opentelemetry.io/), which will enab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: uding the following data: * Model name * Request ID * Sampling params * Latency * Number of input tokens * Number of generated tokens This approach will greatly enhance the observability and troubleshooting capabilities...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
