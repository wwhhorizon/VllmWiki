# vllm-project/vllm#41788: [Feature]: Add request-level OTel span attribute for cached prefix-cache input tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#41788](https://github.com/vllm-project/vllm/issues/41788) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add request-level OTel span attribute for cached prefix-cache input tokens

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM already exposes useful global Prometheus metrics for prefix caching, including `vllm:prefix_cache_hits`, `vllm:prefix_cache_queries`, and cached prompt-token metrics such as `vllm:prompt_tokens_cached`. The V1 request path also carries per-request cached-token information through `RequestOutput.num_cached_tokens`. From the current tracing docs/source, request-level OpenTelemetry spans appear to include prompt/completion token usage and latency attributes, but I could not find an emitted cache-read / cached-token attribute. This makes it difficult for enterprise observability and FinOps systems to correlate prefix-cache savings with individual request traces. I propose adding a request-level OpenTelemetry span attribute for cached input tokens, using the existing per-request `num_cached_tokens` value already available in the V1 output path. Suggested attribute: `gen_ai.usage.cache_read.input_tokens` This aligns with the current OpenTelemetry GenAI semantic conventions for cached input tokens and keeps the change isolated to observability/tracing. It would allow trace backends such as Grafana Tempo, Datadog, Honeycomb, Jaeger, or OpenTele...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: OpenTelemetry spans appear to include prompt/completion token usage and latency attributes, but I could not find an emitted cache-read / cached-token attribute. This makes it difficult for enterprise observability and F...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: keeps the change isolated to observability/tracing. It would allow trace backends such as Grafana Tempo, Datadog, Honeycomb, Jaeger, or OpenTelemetry Collector pipelines to correlate cached-token savings with request ID...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ormation through `RequestOutput.num_cached_tokens`. From the current tracing docs/source, request-level OpenTelemetry spans appear to include prompt/completion token usage and latency attributes, but I could not find an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PR. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: relate cached-token savings with request IDs and upstream gateway/tenant metadata without adding high-cardinality tenant labels to Prometheus metrics. ### Alternatives 1. Rely only on global Prometheus counters such as...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
