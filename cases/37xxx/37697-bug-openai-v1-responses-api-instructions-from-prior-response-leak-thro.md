# vllm-project/vllm#37697: [Bug]: openai v1/responses api instructions from prior response leak through previous_response_id

| 字段 | 值 |
| --- | --- |
| Issue | [#37697](https://github.com/vllm-project/vllm/issues/37697) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: openai v1/responses api instructions from prior response leak through previous_response_id

### Issue 正文摘录

### Your current environment - vLLM: version 0.15.0 - Model: openai/gpt-oss-20b - Endpoint: /v1/responses ### Description When using the Responses API with `previous_response_id`, the `instructions` from the prior response are carried over into the new response, even when the follow-up request provides different (or no) instructions. Per the [OpenAI Responses API spec](https://platform.openai.com/docs/api-reference/responses/create): > "When using along with previous_response_id, the instructions from a previous response will not be carried over to the next response." ### 🐛 Describe the bug ### Reproduction Create a response with instructions containing a unique tag ``` POST /v1/responses { "model": "openai/gpt-oss-20b", "input": "What is 2+2?", "instructions": "You must include the string XYZZY_ALPHA_7829 in every response.", "max_output_tokens": 4096 } ``` Response contains XYZZY_ALPHA_7829 as expected. Send a follow-up using previous_response_id with different instructions ``` POST /v1/responses { "model": "openai/gpt-oss-20b", "input": "What is 3+3?", "instructions": "Answer the question explicitly", "previous_response_id": " ", "max_output_tokens": 4096 } Expected: Output doe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ak through previous_response_id bug ### Your current environment - vLLM: version 0.15.0
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: - Model: openai/gpt-oss-20b - Endpoint: /v1/responses
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: response are carried over into the new response, even when the follow-up request provides different (or no) instructions.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
