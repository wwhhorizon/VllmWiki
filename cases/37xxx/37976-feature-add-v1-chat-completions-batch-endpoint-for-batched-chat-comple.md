# vllm-project/vllm#37976: [Feature]: Add `/v1/chat/completions/batch` endpoint for batched chat completions with structured output support

| 字段 | 值 |
| --- | --- |
| Issue | [#37976](https://github.com/vllm-project/vllm/issues/37976) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add `/v1/chat/completions/batch` endpoint for batched chat completions with structured output support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The completions endpoint (/v1/completions) already supports batched prompts but doesn't apply chat templates, which makes it unsuitable for chat tuned models. After discussion in the comments, the better solution is a dedicated /v1/chat/completions/batch endpoint that applies the chat template per conversation and supports structured output (json_schema, regex constraints). A PR implementing this is open at #37976. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t doesn't apply chat templates, which makes it unsuitable for chat tuned models. After discussion in the comments, the better solution is a dedicated /v1/chat/completions/batch endpoint that applies the chat template pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oint for batched chat completions with structured output support feature request ### 🚀 The feature, motivation and pitch The completions endpoint (/v1/completions) already supports batched prompts but doesn't apply chat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
