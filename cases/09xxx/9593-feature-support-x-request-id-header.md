# vllm-project/vllm#9593: [Feature]: support `x-request-id` header

| 字段 | 值 |
| --- | --- |
| Issue | [#9593](https://github.com/vllm-project/vllm/issues/9593) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support `x-request-id` header

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Related: #9550 It is a common approach for server admin to backtrack client requests via a "request id"(cf. [this SE post](https://stackoverflow.com/questions/25433258/what-is-the-x-request-id-http-header)). It is a unique identifier assigned to each HTTP request which helps grepping the request info from server log. OpenAI supports this in the form of response header (cf. [API Reference - OpenAI API](https://platform.openai.com/docs/api-reference/debugging-requests)). Any response from OpenAI API server has `x-request-id` header, and `openai-python` package provides a convenient way to retrieve this header. (cf. [openai/_models.py](https://github.com/openai/openai-python/blob/main/src/openai/_models.py#L105-L120)) In the referenced PR, we observed the need for request identification (a typical usecase of `x-request-id`), so it may be a good time to support this optional HTTP header in online serving. Suggestion: - Each API response is sent with a `x-request-id` header - When `x-request-id` header is given in user request, send it back to the response header ("Idempotency") - Otherwise, `x-request-id` is a random uuid hex value ("compatibili...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: package provides a convenient way to retrieve this header. (cf. [openai/_models.py](https://github.com/openai/openai-python/blob/main/src/openai/_models.py#L105-L120)) In the referenced PR, we observed the need for requ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s)) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support `x-request-id` header feature request ### 🚀 The feature, motivation and pitch Related: #9550 It is a common approach for server admin to backtrack client requests via a "request id"(cf. [this SE post]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
