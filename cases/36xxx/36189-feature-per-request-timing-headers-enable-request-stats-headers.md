# vllm-project/vllm#36189: [Feature]: Per-Request Timing Headers (`--enable-request-stats-headers`)

| 字段 | 值 |
| --- | --- |
| Issue | [#36189](https://github.com/vllm-project/vllm/issues/36189) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Per-Request Timing Headers (`--enable-request-stats-headers`)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary Add an opt-in server flag `--enable-request-stats-headers` that returns per-request timing and compute metrics as HTTP response headers on non-streaming completion responses. ## Motivation vLLM already tracks detailed per-request timing internally — queue time, prefill time, decode time, inference time — and exposes these via Prometheus metrics and OpenTelemetry traces. However, these are **aggregate or backend-only** observability tools. There is currently no way for an **API consumer** to see where time was spent on *their specific request* without access to the server's metrics endpoint or tracing backend. This matters for three key use cases: ### 1. Client-Side Observability API consumers (application developers building on top of vLLM) currently see a single number: total request latency. They have no way to distinguish between: - The request was slow because it waited in the scheduler queue (capacity issue) - The request was slow because prefill was expensive (long prompt) - The request was slow because decode took many steps (long generation) With per-request headers, any `curl` or HTTP client immediately shows the breakdow...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: Per-Request Timing Headers (`--enable-request-stats-headers`) feature request ### 🚀 The feature, motivation and pitch ## Summary Add an opt-in server flag `--enable-request-stats-headers` that returns per-req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: balancers and routing layers can use per-request timing headers to make smarter decisions. For example, a router could track `x-queue-time` across instances and shift traffic away from instances with growing queue times...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: heus metrics and OpenTelemetry traces. However, these are **aggregate or backend-only** observability tools. There is currently no way for an **API consumer** to see where time was spent on *their specific request* with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: no way for an **API consumer** to see where time was spent on *their specific request* without access to the server's metrics endpoint or tracing backend. This matters for three key use cases: ### 1. Client-Side Observa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rt **Hugging Face Text Embeddings Inference (TEI)** (https://github.com/huggingface/text-embeddings-inference) already returns similar headers on every response: ``` x-compute-time: 13 x-compute-characters: 22 x-compute...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
