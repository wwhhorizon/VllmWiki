# vllm-project/vllm#23767: [Feature]: Add LORA Model Name in Open Telemetry

| 字段 | 值 |
| --- | --- |
| Issue | [#23767](https://github.com/vllm-project/vllm/issues/23767) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add LORA Model Name in Open Telemetry

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using LORAs with vLLM , when calling the LORA model name (**phh/Qwen3-0.6B-TLDR-Lora**), the event generated via OpenTelemetry registers only the base model (**Qwen/Qwen3-0.6B**) name and not the LORA model name. A new field with the LORA name should be included when calling LORAs. The following LORA call: ``` curl -X POST http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer KEY" \ -H "X-Request-Id: custom-request-id-ale-LORA" \ -H "X-Request-Ale: LORA" \ -d '{ "model": "phh/Qwen3-0.6B-TLDR-Lora", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello, how are you today?"} ] }' ``` emits: ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add LORA Model Name in Open Telemetry feature request;stale ### 🚀 The feature, motivation and pitch When using LORAs with vLLM , when calling the LORA model name (**phh/Qwen3-0.6B-TLDR-Lora**), the event gene...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add LORA Model Name in Open Telemetry feature request;stale ### 🚀 The feature, motivation and pitch When using LORAs with vLLM , when calling the LORA model name (**phh/Qwen3-0.6B-TLDR-Lora**), the event gene...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
