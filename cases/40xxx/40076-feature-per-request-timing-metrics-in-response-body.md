# vllm-project/vllm#40076: [Feature]: Per-request timing metrics in response body

| 字段 | 值 |
| --- | --- |
| Issue | [#40076](https://github.com/vllm-project/vllm/issues/40076) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Per-request timing metrics in response body

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary Add an opt-in capability for vLLM to return per-request timing and compute metrics **in the response body** of OpenAI-compatible completion endpoints. The feature would be gated by a server-level flag (e.g. `--enable-per-request-metrics`) plus a per-request parameter (e.g. `include_metrics: true`), and would expose a structured `metrics` object alongside the normal response payload. This issue is intentionally filed as a companion / counter-proposal to #36189, which proposes exposing the same information via HTTP response headers. A draft implementation of the body-based approach already exists in #36383. ## Motivation (The motivation here largely overlaps with #36189; only real difference is delivery mechanism) vLLM already tracks detailed per-request timing internally (queue time, prefill time, decode time, inter-token latency, etc.) via `RequestStateStats`, and surfaces aggregated versions of this data through Prometheus metrics and OpenTelemetry traces. Those are backend-only, aggregate observability tools — they do not let an API consumer see where time was spent on _their specific request_. Exposing this data to API consumer...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Feature]: Per-request timing metrics in response body feature request ### 🚀 The feature, motivation and pitch ## Summary Add an opt-in capability for vLLM to return per-request timing and compute metrics **in the respo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: quest ### 🚀 The feature, motivation and pitch ## Summary Add an opt-in capability for vLLM to return per-request timing and compute metrics **in the response body** of OpenAI-compatible completion endpoints. The feature...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: er-token latency, etc.) via `RequestStateStats`, and surfaces aggregated versions of this data through Prometheus metrics and OpenTelemetry traces. Those are backend-only, aggregate observability tools — they do not let...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: st timing internally (queue time, prefill time, decode time, inter-token latency, etc.) via `RequestStateStats`, and surfaces aggregated versions of this data through Prometheus metrics and OpenTelemetry traces. Those a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mpanion / counter-proposal to #36189, which proposes exposing the same information via HTTP response headers. A draft implementation of the body-based approach already exists in #36383. ## Motivation (The motivation her...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
