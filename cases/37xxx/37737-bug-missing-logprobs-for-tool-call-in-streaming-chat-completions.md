# vllm-project/vllm#37737: [Bug]: Missing logprobs for `<tool_call>` in streaming chat completions

| 字段 | 值 |
| --- | --- |
| Issue | [#37737](https://github.com/vllm-project/vllm/issues/37737) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Missing logprobs for `<tool_call>` in streaming chat completions

### Issue 正文摘录

### Your current environment - vLLM version: v0.15.0, v0.17.1 - Serving mode: OpenAI-compatible API server - Model: Qwen/Qwen3-VL-8B-Thinking - Request mode: streaming chat completions with logprobs=true ### 🐛 Describe the bug We reproduced this with `Qwen/Qwen3-VL-8B-Thinking`. The tool call is parsed successfully, but the ` ` token is missing from streamed `logprobs`. We observed the same issue on both vLLM `v0.15.0` and `v0.17.1`. This is intermittent. With the same request, it reproduces roughly once every 3 to 5 runs. This depends on streaming chunk boundaries. vLLM may return multiple tokens in one streamed chunk, and that grouping can vary across runs. If ` ` is grouped with visible reasoning or content tokens, the chunk is emitted and its logprob is preserved. If ` ` falls into a chunk that only contains tool-call control tokens, the parser may suppress that chunk, and the ` ` logprob is dropped even though tool parsing still succeeds. Expected: - the stream includes the tool call delta - the corresponding ` ` token also appears in `choices[0].logprobs.content` Actual: - the stream includes `delta.tool_calls` - ` ` is missing from `choices[0].logprobs.content` - when it re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ` in streaming chat completions bug ### Your current environment - vLLM version: v0.15.0, v0.17.1 - Serving mode: OpenAI-compatible API server - Model: Qwen/Qwen3-VL-8B-Thinking - Request mode: streaming chat completion...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: version: v0.15.0, v0.17.1 - Serving mode: OpenAI-compatible API server - Model: Qwen/Qwen3-VL-8B-Thinking - Request mode: streaming chat completions with logprobs=true ### 🐛 Describe the bug We reproduced this with `Qwe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: treaming chat completions with logprobs=true ### 🐛 Describe the bug We reproduced this with `Qwen/Qwen3-VL-8B-Thinking`. The tool call is parsed successfully, but the ` ` token is missing from streamed `logprobs`. We ob...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mode: OpenAI-compatible API server - Model: Qwen/Qwen3-VL-8B-Thinking - Request mode: streaming chat completions with logprobs=true ### 🐛 Describe the bug We reproduced this with `Qwen/Qwen3-VL-8B-Thinking`. The tool ca...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
