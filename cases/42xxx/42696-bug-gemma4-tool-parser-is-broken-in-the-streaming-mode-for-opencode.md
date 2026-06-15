# vllm-project/vllm#42696: [Bug]: Gemma4 tool parser is broken in the streaming mode (for OpenCode)

| 字段 | 值 |
| --- | --- |
| Issue | [#42696](https://github.com/vllm-project/vllm/issues/42696) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 tool parser is broken in the streaming mode (for OpenCode)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've observed two failure modes in the streaming gemma4 tool-parser, when using it from opencode: 1. Strict-client id / type / function.name re-emission (the original patch). The OpenAI streaming spec only requires id, type, and function.name to be set on the first DeltaToolCall chunk for a given tool-call index — subsequent chunks are deduped by index and may omit those fields. Stock vLLM 0.20.2's Gemma4ToolParser follows that letter-of-the-spec behaviour: _handle_tool_call_middle emits the trio on the first chunk, then _emit_argument_diff and _handle_tool_call_end emit follow-up chunks with only index + function.arguments set. But @ai-sdk's openai-compatible provider (used by opencode) Zod-validates every chunk against {id: z.string(), type: z.literal('function'), function: {name: z.string(), arguments: z.string()}} and bails out mid-stream the first time any of those is missing/null, surfacing as AI_InvalidResponseDataError: Expected 'id' to be a string (~64% of agents in run 11726821) and then, once id was patched, the sibling Expected 'function.name' to be a string (~42% of agents in run 11730617). The patch stashes the mint...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d bails out mid-stream the first time any of those is missing/null, surfacing as AI_InvalidResponseDataError: Expected 'id' to be a string (~64% of agents in run 11726821) and then, once id was patched, the sibling Expe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lose-marker chunk splits) that run as the existing Dockerfile build-time smoke check. Script below is a conceptual repro: ```python """Regression tests for the datapatcher gemma4 tool-parser patches. Two failure modes a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ToolCall for that index — a no-op for compliant clients (they dedupe), unblocking for strict ones. 2. Multi-boundary delta mis-attribution under load (the new Path A patch). Upstream's _extract_streaming is a single-Cas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 tool parser is broken in the streaming mode (for OpenCode) bug ### Your current environment ### 🐛 Describe the bug I've observed two failure modes in the streaming gemma4 tool-parser, when using it from op...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ool_calls_streaming). Under high concurrency, vLLM's continuous-batching scheduler produces larger per-step text deltas, and a single delta routinely brings end-of-tool-N + start-of-tool-N+1 (or even multiple complete t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
