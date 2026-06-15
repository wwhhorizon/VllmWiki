# vllm-project/vllm#40779: [Bug]: [MiniMax] Function call content is not streamed incrementally; buffered until generation completes

| 字段 | 值 |
| --- | --- |
| Issue | [#40779](https://github.com/vllm-project/vllm/issues/40779) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [MiniMax] Function call content is not streamed incrementally; buffered until generation completes

### Issue 正文摘录

### Your current environment ## Environment vLLM version: 0.18.0 Model: MiniMax-M2.5 ### 🐛 Describe the bug ## Description When deploying the MiniMax model via vLLM with streaming enabled` (stream: true)`, the function call (or tool call) payload is not returned token-by-token. Instead, vLLM appears to buffer the entire function call content and only emits it after a noticeable delay, typically right after the generation finishes. This breaks streaming consumers that expect incremental `tool_calls.function.arguments` chunks. ## Steps to Reproduce 1. Serve the MiniMax model using vLLM: vllm serve --enable-auto-tool-choice ... 2. Send a streaming request via the OpenAI-compatible API with a prompt that triggers a function/tool call. ``` { "model": " ", "messages": [{"role": "user", "content": "Please call the weather function for Beijing"}], "tools": [{"type": "function", "function": {"name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}}], "stream": true } ``` 3. Observe the SSE/stream output. ## Expected Behavior Function/tool call tokens (e.g., JSON arguments) should be streamed incrementally as they are generated, consistent wit...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: es bug ### Your current environment ## Environment vLLM version: 0.18.0 Model: MiniMax-M2.5 ### 🐛 Describe the bug ## Description When deploying the MiniMax model via vLLM with streaming enabled` (stream: true)`, the fu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: neration completes bug ### Your current environment ## Environment vLLM version: 0.18.0 Model: MiniMax-M2.5 ### 🐛 Describe the bug ## Description When deploying the MiniMax model via vLLM with streaming enabled` (stream...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: expect incremental `tool_calls.function.arguments` chunks. ## Steps to Reproduce 1. Serve the MiniMax model using vLLM: vllm serve --enable-auto-tool-choice ... 2. Send a streaming request via the OpenAI-compatible API...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PU. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing vLLM: vllm serve --enable-auto-tool-choice ... 2. Send a streaming request via the OpenAI-compatible API with a prompt that triggers a function/tool call. ``` { "model": " ", "messages": [{"role": "user", "content":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
