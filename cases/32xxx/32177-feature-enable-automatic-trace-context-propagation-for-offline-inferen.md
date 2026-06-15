# vllm-project/vllm#32177: [Feature]: Enable automatic trace context propagation for offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#32177](https://github.com/vllm-project/vllm/issues/32177) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable automatic trace context propagation for offline inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Enable automatic trace context propagation for offline inference APIs (`LLM.generate()`, etc.) by extracting trace headers from the current OpenTelemetry context. Currently, vLLM has two usage modes with different tracing support: 1. Online serving(entry point: `http://localhost:8000/v1/completions`) can extract trace context from HTTP headers 2. Offline inference(`LLM.generate()`): there is no way to pass or auto-detect trace context The low-level `InputProcessor.process_inputs()` already supports `trace_headers`, but offline inference APIs don't utilize it. ### Expected Behavior ```python with tracer.start_as_current_span("rag-pipeline"): # vLLM automatically detects active span and links to it outputs = llm.generate("Hello, world!") ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: elemetry context. Currently, vLLM has two usage modes with different tracing support: 1. Online serving(entry point: `http://localhost:8000/v1/completions`) can extract trace context from HTTP headers 2. Offline inferen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Enable automatic trace context propagation for offline inference feature request;stale ### 🚀 The feature, motivation and pitch Enable automatic trace context propagation for offline inference APIs (`LLM.generate()`, etc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
