# vllm-project/vllm#32142: [RFC]: Support function calling using `structural_tag`.

| 字段 | 值 |
| --- | --- |
| Issue | [#32142](https://github.com/vllm-project/vllm/issues/32142) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support function calling using `structural_tag`.

### Issue 正文摘录

### Motivation. 1. When using vLLM’s OpenAI-compatible API, if `tool_choice="required"` is set to force the model to call a tool, the model’s output behavior does not match expectations. **Specific concern:** When `tool_choice="required"` is enabled, vLLM converts the tool schema into a JSON Schema and constrains the model output via `structured_outputs`. Since the schema is defined as `{"type": "array", ...}`, does this mean the model’s first token is forcibly constrained to be `"["`? , this would skip the model’s native `tool_calls_start_token` (e.g. ` `), completely bypassing the model’s native tool-calling format and its thinking output. 2. **Tool parsing logic:** The current function-calling parsing logic looks quite hacky and fragmented. Most of the logic relies on regular expressions to extract the tool-calling portion, and then uses JSON parsing to extract the tool name and arguments. In practice, the tool-calling output produced by the model does not always strictly conform to the expected JSON format, which can lead to parsing failures or incorrect results. Therefore, introducing a `structural_tag` mechanism would allow more reliable marking of the start and end of tool...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: s OpenAI-compatible API, if `tool_choice="required"` is set to force the model to call a tool, the model’s output behavior does not match expectations. **Specific concern:** When `tool_choice="required"` is enabled, vLL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s or incorrect results. Therefore, introducing a `structural_tag` mechanism would allow more reliable marking of the start and end of tool calls, making the parsing process more robust and accurate. ### Proposed Change....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a tool, the model’s output behavior does not match expectations. **Specific concern:** When `tool_choice="required"` is enabled, vLLM converts the tool schema into a JSON Schema and constrains the model output via `stru...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: tiple types of tool_call formats. ----- Llama JSON-based tool calling, Gemma: ``` {"name": "function_name", "parameters": params} ``` Corresponding structural tag: ``` { "type": "structural_tag", "format": { "type": "tr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
