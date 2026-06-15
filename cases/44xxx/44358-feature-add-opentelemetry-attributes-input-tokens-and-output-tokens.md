# vllm-project/vllm#44358: [Feature]: Add OpenTelemetry attributes input_tokens and output_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#44358](https://github.com/vllm-project/vllm/issues/44358) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add OpenTelemetry attributes input_tokens and output_tokens

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary (This is not really a feature request, but I couldn't find a better label.) vLLM tracing emits two span attributes deprecated by the OTel GenAI conventions: - `gen_ai.usage.prompt_tokens` → `gen_ai.usage.input_tokens` - `gen_ai.usage.completion_tokens` → `gen_ai.usage.output_tokens` Ref: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ Defined in `vllm/tracing/utils.py`, emitted in `OutputProcessor.do_tracing`. https://github.com/vllm-project/vllm/blob/0cbc48c4f98873acb88ab220db4540ffe99cbc1e/vllm/tracing/utils.py#L24-L25 ### Proposal I suggest emitting both new and old attributes until they are removed from the opentelemetry. This will also give the backends and dashboards some time to migrate with maximum coverage. ### Questions for maintainers - Dual-emit vs. hard replace? - Deprecation window / removal target? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s until they are removed from the opentelemetry. This will also give the backends and dashboards some time to migrate with maximum coverage. ### Questions for maintainers - Dual-emit vs. hard replace? - Deprecation wind...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: really a feature request, but I couldn't find a better label.) vLLM tracing emits two span attributes deprecated by the OTel GenAI conventions: - `gen_ai.usage.prompt_tokens` → `gen_ai.usage.input_tokens` - `gen_ai.usag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re]: Add OpenTelemetry attributes input_tokens and output_tokens feature request ### 🚀 The feature, motivation and pitch ### Summary (This is not really a feature request, but I couldn't find a better label.) vLLM traci...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
