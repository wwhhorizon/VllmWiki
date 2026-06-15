# vllm-project/vllm#16678: [RFC]: tool_calls and None types.

| 字段 | 值 |
| --- | --- |
| Issue | [#16678](https://github.com/vllm-project/vllm/issues/16678) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: tool_calls and None types.

### Issue 正文摘录

### Motivation. ### Summary Exploring tool_calls in VLLM. Seems to be a need for additional handling of non-iterable None type responses in the tool_calls field. ### Motivation I've been testing with Google's new ADK (backed by LiteLLM) against a VLLM hosted Qwen 2.5 Instruct model and the Hermes parser. (Using Kserve). https://github.com/google/adk-python/blob/290058eb05211ef531b1752c6290da3f365e4e73/src/google/adk/models/lite_llm.py#L194 ADK explicitly returns a None in the tool_calls field. ` tool_calls=tool_calls or None,` From what I understand, some models and hosting do expect this None type, however VLLM does not. This means that on the second message of the chat, you get the following: `ERROR - fast_api.py:616 - Error in event_generator: litellm.BadRequestError: OpenAIException - 'NoneType' object is not iterable` This seems to bring us to https://github.com/vllm-project/vllm/blob/54a66e5fee4a1ea62f1e4c79a078b20668e408c6/vllm/entrypoints/chat_utils.py#L1072 in which the iteration takes place here. https://github.com/vllm-project/vllm/blob/54a66e5fee4a1ea62f1e4c79a078b20668e408c6/vllm/entrypoints/chat_utils.py#L1097 It would be nice if VLLM could work cleanly with ADK and...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: testing with Google's new ADK (backed by LiteLLM) against a VLLM hosted Qwen 2.5 Instruct model and the Hermes parser. (Using Kserve). https://github.com/google/adk-python/blob/290058eb05211ef531b1752c6290da3f365e4e73/s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 31b1752c6290da3f365e4e73/src/google/adk/models/lite_llm.py#L194 ADK explicitly returns a None in the tool_calls field. ` tool_calls=tool_calls or None,` From what I understand, some models and hosting do expect this Non...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: owing: `ERROR - fast_api.py:616 - Error in event_generator: litellm.BadRequestError: OpenAIException - 'NoneType' object is not iterable` This seems to bring us to https://github.com/vllm-project/vllm/blob/54a66e5fee4a1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: one type responses in the tool_calls field. ### Motivation I've been testing with Google's new ADK (backed by LiteLLM) against a VLLM hosted Qwen 2.5 Instruct model and the Hermes parser. (Using Kserve). https://github....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
