# vllm-project/vllm#33923: [Feature]: Report cached tokens in Anthropic `/v1/messages` API

| 字段 | 值 |
| --- | --- |
| Issue | [#33923](https://github.com/vllm-project/vllm/issues/33923) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Report cached tokens in Anthropic `/v1/messages` API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM implements the Anthropic `/v1/messages` API since #22627. However, the API, as implemented in this PR, does not report cached tokens. The upstream Anthropic API does. The cached tokens should be reported via the already-available fields: ```py class AnthropicUsage(BaseModel): """Token usage information""" input_tokens: int output_tokens: int cache_creation_input_tokens: int | None = None # here cache_read_input_tokens: int | None = None # and here ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ported via the already-available fields: ```py class AnthropicUsage(BaseModel): """Token usage information""" input_tokens: int output_tokens: int cache_creation_input_tokens: int | None = None # here cache_read_input_t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Report cached tokens in Anthropic `/v1/messages` API feature request;unstale ### 🚀 The feature, motivation and pitch vLLM implements the Anthropic `/v1/messages` API since #22627. However, the API, as impleme...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
