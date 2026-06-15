# vllm-project/vllm#44104: [Bug]: Chat completions emits empty tool_calls arrays after tool results

| 字段 | 值 |
| --- | --- |
| Issue | [#44104](https://github.com/vllm-project/vllm/issues/44104) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Chat completions emits empty tool_calls arrays after tool results

### Issue 正文摘录

### Your current environment Observed on both: - vLLM 0.20.2 pinned checkout: `bc150f5` - vLLM main/latest checkout tested locally: `7bd738988` ### 🐛 Describe the bug The OpenAI-compatible chat completions API can serialize a normal assistant response with an empty `tool_calls` array after the client returns a tool result. The response is semantically a final assistant message: - `finish_reason` is `"stop"` - `message.content` / stream `delta.content` contains normal text - there is no tool call to execute But the JSON payload still contains `"tool_calls": []`. In the OpenAI Python SDK this becomes a non-`None` `message.tool_calls` value, so common client loops treat the response as another tool-call response and then fail when indexing the empty list. Example client failure: ```python while assistant_output.tool_calls is not None: tool_call = assistant_output.tool_calls[0] ``` Actual vLLM payload shape after the tool result: ```json { "choices": [ { "finish_reason": "stop", "message": { "role": "assistant", "content": "...final answer...", "tool_calls": [] } } ] } ``` Expected payload shape: ```json { "choices": [ { "finish_reason": "stop", "message": { "role": "assistant", "cont...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bserved on both: - vLLM 0.20.2 pinned checkout: `bc150f5` - vLLM main/latest checkout tested locally: `7bd738988` ### 🐛 Describe the bug The OpenAI-compatible chat completions API can serialize a normal assistant respon...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tas. This is not a DeepSeek V4 tool-call parser failure and not a model accuracy issue. The model returns the expected final natural-language answer after the tool result; the API response serializer emits a misleading...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y tool-call field. ### Before submitting a new issue... - [x] I have searched the existing issues and did not find a duplicate.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: xt deltas. This is not a DeepSeek V4 tool-call parser failure and not a model accuracy issue. The model returns the expected final natural-language answer after the tool result; the API response serializer emits a misle...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
