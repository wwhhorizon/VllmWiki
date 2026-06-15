# vllm-project/vllm#25212: [RFC]: Renaming vllm metric name

| 字段 | 值 |
| --- | --- |
| Issue | [#25212](https://github.com/vllm-project/vllm/issues/25212) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Renaming vllm metric name

### Issue 正文摘录

### Motivation. VLLM metrics are built on top of Ray’s metric infrastructure, and their names currently use the prefix "vllm:": https://github.com/vllm-project/vllm/blob/9fac6aa30b669de75d8718164cd99676d3530e7d/vllm/engine/metrics.py#L57-L78. Ray is migrating its metric infrastructure to an OpenTelemetry backend in upcoming releases (as OpenCensus has been deprecated for a few years). However, OpenTelemetry does not permit the ":" character in metric names (https://github.com/open-telemetry/opentelemetry-cpp/blob/main/sdk/src/metrics/instrument_metadata_validator.cc#L22-L23 ). As a result, Ray will also remove support for ":" in all metric names. ### Proposed Change. To maintain compatibility between vLLM and Ray going forward, would it be possible for the vLLM team to update the metric names from the `vllm:..` format to `vllm_..` instead? Thank you! ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: L57-L78. Ray is migrating its metric infrastructure to an OpenTelemetry backend in upcoming releases (as OpenCensus has been deprecated for a few years). However, OpenTelemetry does not permit the ":" character in metri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: om/open-telemetry/opentelemetry-cpp/blob/main/sdk/src/metrics/instrument_metadata_validator.cc#L22-L23 ). As a result, Ray will also remove support for ":" in all metric names. ### Proposed Change. To maintain compatibi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: possible for the vLLM team to update the metric names from the `vllm:..` format to `vllm_..` instead? Thank you! ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Befo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
