# vllm-project/vllm#23365: [Feature]: Add support for /v1/responses API benchmarking backend

| 字段 | 值 |
| --- | --- |
| Issue | [#23365](https://github.com/vllm-project/vllm/issues/23365) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for /v1/responses API benchmarking backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The recommended way to run openai/gpt-oss is by using the /v1/responses endpoint, but currently, benchmarking only works for these kind of endpoint types: - "openai": async_request_openai_completions, - "openai-chat": async_request_openai_chat_completions, - "openai-audio": async_request_openai_audio, ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Add support for /v1/responses API benchmarking backend feature request;stale ### 🚀 The feature, motivation and pitch The recommended way to run openai/gpt-oss is by using the /v1/responses endpoint, but curren...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Add support for /v1/responses API benchmarking backend feature request;stale ### 🚀 The feature, motivation and pitch The recommended way to run openai/gpt-oss is by using the /v1/responses endpoint, but curre...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Add support for /v1/responses API benchmarking backend feature request;stale ### 🚀 The feature, motivation and pitch The recommended way to run openai/gpt-oss is by using the /v1/responses endpoint, but curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # 🚀 The feature, motivation and pitch The recommended way to run openai/gpt-oss is by using the /v1/responses endpoint, but currently, benchmarking only works for these kind of endpoint types: - "openai": async_request_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
