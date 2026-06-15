# vllm-project/vllm#37086: [Feature]: Expose stable request completion hook in streaming serving paths

| 字段 | 值 |
| --- | --- |
| Issue | [#37086](https://github.com/vllm-project/vllm/issues/37086) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose stable request completion hook in streaming serving paths

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Feature Request: Stable request completion hook for streaming requests ### Motivation While tracing vLLM's streaming serving paths, I noticed that there is currently no stable lifecycle boundary exposed when a streaming request fully completes. Across multiple entrypoints, request completion appears to be detected inside Python generator control flow where the serving layer consumes streamed items and checks for the terminal `[DONE]` sentinel before yielding the final response events. For example, in the Anthropic serving path (`vllm/entrypoints/anthropic/serving.py`), completion is currently handled inside the streaming generator: ```python async for item in generator: if item.startswith("data:"): data_str = item[5:].strip().rstrip("\n") if data_str == "[DONE]": stop_message = AnthropicStreamEvent( type="message_stop", ) data = stop_message.model_dump_json( exclude_unset=True, exclude_none=True ) yield wrap_data_with_event(data, "message_stop") yield "data: [DONE]\n\n" ``` This pattern appears across entrypoints where the serving layer inspects the streamed output and detects completion when the [DONE] sentinel is encountered. Because re...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eaming behavior. The hook could be extremely lightweight (for example a small function call or symbol triggered when the request completes), though I'm mainly raising the architectural gap here rather than prescribing a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bility and runtime instrumentation, including: - measuring full request latency for streaming responses - correlating token emission with request completion - tracking request completion rate under load - integrating ex...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: request completion hook for streaming requests ### Motivation While tracing vLLM's streaming serving paths, I noticed that there is currently no stable lifecycle boundary exposed when a streaming request fully completes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: type="message_stop", ) data = stop_message.model_dump_json( exclude_unset=True, exclude_none=True ) yield wrap_data_with_event(data, "message_stop") yield "data: [DONE]\n\n" ``` This pattern appears across entr
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Expose stable request completion hook in streaming serving paths feature request ### 🚀 The feature, motivation and pitch ## Feature Request: Stable request completion hook for streaming requests ### Motivatio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
