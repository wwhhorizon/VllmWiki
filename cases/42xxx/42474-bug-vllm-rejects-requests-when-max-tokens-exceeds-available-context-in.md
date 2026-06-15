# vllm-project/vllm#42474: [Bug]: vLLM rejects requests when max_tokens exceeds available context instead of clamping

| 字段 | 值 |
| --- | --- |
| Issue | [#42474](https://github.com/vllm-project/vllm/issues/42474) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM rejects requests when max_tokens exceeds available context instead of clamping

### Issue 正文摘录

**Bug**: vLLM rejects requests when `max_tokens` exceeds available context, treating it as a hard requirement rather than an upper bound **Environment**: - vLLM Version: 0.20.x (latest dev) **Reproduction**: 1. Start vLLM server with `--max-model-len 128000` 2. Send chat completion request with: - `max_tokens: 65535` (streaming safety cap) - Input prompt tokenized to 62466 tokens 3. vLLM returns 400 error: ``` VLLMValidationError: This model's maximum context length is 128000 tokens. However, you requested 65535 output tokens and your prompt contains at least 62466 input tokens, for a total of at least 128001 tokens. ``` Error location: `vllm/renderers/params.py:418` in `_token_len_check()` **Impact**: - **Zed Editor**: AI assistant using `max_tokens: 65535` caps - **Factory.ai**: Agentic code generation - **Opencode**: CLI tool with streaming safety limits GPU-limited deployments cannot use these tools with vLLM. The full context window plus typical token caps exceeds available memory, leaving users stuck at the ceiling. **Current workaround**: Users configure artificially low `max_tokens` in their editor/IDE settings to avoid exceeding the context window, sacrificing the intende...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s a hard requirement rather than an upper bound **Environment**: - vLLM Version: 0.20.x (latest dev) **Reproduction**: 1. Start vLLM server with `--max-model-len 128000` 2. Send chat completion request with: - `max_toke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 0.20.x (latest dev) **Reproduction**: 1. Start vLLM server with `--max-model-len 128000` 2. Send chat completion request with: - `max_tokens: 65535` (streaming safety cap) - Input prompt tokenized to 62466 tokens 3. vLL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM rejects requests when max_tokens exceeds available context instead of clamping **Bug**: vLLM rejects requests when `max_tokens` exceeds available context, treating it as a hard requirement rather than an upp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t rather than an upper bound **Environment**: - vLLM Version: 0.20.x (latest dev) **Reproduction**: 1. Start vLLM server with `--max-model-len 128000` 2. Send chat completion request with: - `max_tokens: 65535` (streami...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
