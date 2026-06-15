# vllm-project/vllm#31437: [Bug]: Streaming tool calls missing id/type/name in finish chunk

| 字段 | 值 |
| --- | --- |
| Issue | [#31437](https://github.com/vllm-project/vllm/issues/31437) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming tool calls missing id/type/name in finish chunk

### Issue 正文摘录

### Your current environment vLLM 0.14.0rc1.dev3 (but also affects main branch as of today) ### Model GLM-4.7-AWQ with `--tool-call-parser glm47` (also affects other parsers that emit complete tool calls) ### What is the issue? When streaming tool calls, the finish chunk code in `serving_chat.py` overwrites the tool parser's properly-formatted `DeltaMessage` with a stripped-down version that only contains `index` and `function.arguments`, losing the `id`, `type`, and `function.name` fields. This breaks OpenAI-compatible clients that expect `id` to be present in tool call responses. ### Root cause In `serving_chat.py` around line 1237, when `_should_check_for_unstreamed_tool_arg_tokens()` returns true: ```python remaining_call = expected_call.replace(actual_call, "", 1) delta_message = DeltaMessage( tool_calls=[ DeltaToolCall( index=index, function=DeltaFunctionCall( arguments=remaining_call ).model_dump(exclude_none=True), ) ] ) ``` This creates a new `DeltaMessage` without preserving `id`, `type`, or `function.name` from the original `delta_message` that the tool parser returned. ### Proposed fix Preserve the fields from the original delta: ```python remaining_call = expected_cal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent vLLM 0.14.0rc1.dev3 (but also affects main branch as of today) ### Model GLM-4.7-AWQ with `--tool-call-parser glm47` (also affects other parsers that emit complete tool calls) ### What is the issue? When streaming t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the tool parser's properly-formatted `DeltaMessage` with a stripped-down version that only contains `index` and `function.arguments`, losing the `id`, `type`, and `function.name` fields. This breaks OpenAI-compatible cl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ht. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: message.tool_calls[0] original_fn = original_tc.function if original_tc else None delta_message = DeltaMessage( tool_calls=[ DeltaToolCall( index=index, id=original_tc.id if original_tc else None, type=original_tc.type...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
