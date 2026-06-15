# vllm-project/vllm#31443: [Bug]: Tool name is lost in chat_completion_stream_generator

| 字段 | 值 |
| --- | --- |
| Issue | [#31443](https://github.com/vllm-project/vllm/issues/31443) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tool name is lost in chat_completion_stream_generator

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when using tool calling sometimes I got something like `[ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments='{"code": "print(114 * 514)"}', name=None), type=None)]` which only have arguments but have no name. After debuging I found this part in [https://github.com/vllm-project/vllm/blob/62def07d6786b39cd51b896b254fb2a40cc0f503/vllm/entrypoints/openai/serving_chat.py#L4](url) causes this bug ```python if ( self._should_check_for_unstreamed_tool_arg_tokens( delta_message, output ) and tool_parser ): latest_delta_len = 0 if ( isinstance( delta_message.tool_calls[0].function, DeltaFunctionCall, ) ) and isinstance( delta_message.tool_calls[0].function.arguments, str ): latest_delta_len = len( delta_message.tool_calls[0].function.arguments ) # get the expected call based on partial JSON # parsing which "autocompletes" the JSON expected_call = json.dumps( tool_parser.prev_tool_call_arr[index].get( "arguments", {} ), ensure_ascii=False, ) # get what we've streamed so far for arguments # for the current tool actual_call = tool_parser.streamed_args_for_tool[index] if latest_delta_len > 0: actual_call = act...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ndex].get( "arguments", {} ), ensure_ascii=False, ) # get what we've streamed so far for arguments # for the current tool actual_call = tool_parser.streamed_args_for_tool[index] if latest_delta_len > 0: actual_call =
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: get( "arguments", {} ), ensure_ascii=False, ) # get what we've streamed so far for arguments # for the current tool actual_call = tool_parser.streamed_args_for_tool[index] if latest_delta_len > 0: actual_call = actua
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Call( arguments=remaining_call ).model_dump(exclude_none=True), ) ] ) # >>>>>>>>>>>>> 调试点 2 开始 >>>>>>>>>>>> 调试点 2 结束 , so we must have got full json. Maybe it is designed for other parsers. but however this thing br
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: delta_message, output ) and tool_parser ): latest_delta_len = 0 if ( isinstance( delta_message.tool_calls[0].function, DeltaFunctionCall, ) ) and isinstance( delta_message.tool_calls[0].function.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
