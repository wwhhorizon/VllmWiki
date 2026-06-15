# vllm-project/vllm#40147: [Bug]: forced tool_choice asserts when reasoning extraction returns content=None

| 字段 | 值 |
| --- | --- |
| Issue | [#40147](https://github.com/vllm-project/vllm/issues/40147) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: forced tool_choice asserts when reasoning extraction returns content=None

### Issue 正文摘录

## Summary Forced tool choice can crash with `AssertionError` when a reasoning parser returns `content=None`. This is reachable for parsers such as `glm45` / `DeepSeekV3ReasoningWithThinkingParser`, whose full-output reasoning extraction returns `(reasoning, None)` when the model output contains only reasoning text or ends immediately after ` `. ## Affected code - `vllm/entrypoints/openai/engine/serving.py` - `vllm/parser/abstract_parser.py` Both paths currently do this for forced function calls: - named chat tool choice: `{"type":"function","function":{"name":"..."}}` - responses tool choice: `{"type":"function","name":"..."}` They assert that `content is not None` before constructing `FunctionCall(...)`. ## Why this is a bug Reasoning extraction is allowed to consume the entire model output and return `content=None`. For example, the basic thinking parser returns `(reasoning, None)` when no post-reasoning content exists. That makes the following assertion reachable and it bubbles up as a server-side failure instead of a valid tool-call response with empty arguments. ## Minimal reproducer ### Chat-completions code path ```python from vllm.entrypoints.openai.chat_completion.protoc...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: penAIServing req = ChatCompletionRequest.model_validate({ "model": "test-model", "messages": [{"role": "user", "content": "test"}], "tools": [{ "type": "function", "function": { "name": "get_weather", "parameters": {"ty...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: instead of a valid tool-call response with empty arguments. ## Minimal reproducer ### Chat-completions code path ```python from vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest from vllm.ent...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: de path ```python from vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest from vllm.entrypoints.openai.engine.serving import OpenAIServing req = ChatCompletionRequest.model_validate({ "model":...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: se full-output reasoning extraction returns `(reasoning, None)` when the model output contains only reasoning text or ends immediately after ` `. ## Affected code - `vllm/entrypoints/openai/engine/serving.py` - `vllm/pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: om vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest from vllm.entrypoints.openai.engine.serving import OpenAIServing req = ChatCompletionRequest.model_validate({ "model": "test-model", "mess...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
