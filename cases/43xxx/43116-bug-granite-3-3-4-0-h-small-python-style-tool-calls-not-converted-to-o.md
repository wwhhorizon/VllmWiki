# vllm-project/vllm#43116: [Bug]: Granite 3.3 / 4.0 H-Small Python-style tool calls not converted to OpenAI tool_calls format

| 字段 | 值 |
| --- | --- |
| Issue | [#43116](https://github.com/vllm-project/vllm/issues/43116) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Granite 3.3 / 4.0 H-Small Python-style tool calls not converted to OpenAI tool_calls format

### Issue 正文摘录

### 🐛 Describe the bug When using `ibm-granite/granite-3.3-8b-instruct` or `ibm-granite/granite-4.0-h-small` with vLLM's OpenAI-compatible server, the model generates **Python-style function calls** as plain text in the `content` field instead of populating the `tool_calls` array in the OpenAI format. This breaks all agent frameworks and clients that rely on the OpenAI tool-calling protocol. --- ### Root Cause Granite 3.3 and Granite 4.0 H-Small use a **Python-style** tool call format natively: ```python get_weather(location="San Francisco", unit="celsius") search_web(query="vLLM release notes") ``` The existing `Granite4ToolParser` (registered as `granite4`) handles the **XML ` ` format** used by Granite 4.0 Tiny/Base — it does **not** handle the Python-style output of Granite 3.3 or H-Small. Passing `--tool-call-parser granite4` to these models has no effect since the ` ` tokens never appear in their output. --- ### Steps to Reproduce ```bash vllm serve ibm-granite/granite-3.3-8b-instruct \ --tool-call-parser granite4 \ --chat-template examples/tool_chat_template_granite.jinja ``` ```python import openai client = openai.OpenAI(base_url="http://localhost:8000/v1", api_key="x") to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: le** tool call format natively: ```python get_weather(location="San Francisco", unit="celsius") search_web(query="vLLM release notes") ``` The existing `Granite4ToolParser` (registered as `granite4`) handles the **XML `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Granite 3.3 / 4.0 H-Small Python-style tool calls not converted to OpenAI tool_calls format ### 🐛 Describe the bug When using `ibm-granite/granite-3.3-8b-instruct` or `ibm-granite/granite-4.0-h-small` with vLLM's...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: / 4.0 H-Small Python-style tool calls not converted to OpenAI tool_calls format ### 🐛 Describe the bug When using `ibm-granite/granite-3.3-8b-instruct` or `ibm-granite/granite-4.0-h-small` with vLLM's OpenAI-compatible...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ct since the ` ` tokens never appear in their output. --- ### Steps to Reproduce ```bash vllm serve ibm-granite/granite-3.3-8b-instruct \ --tool-call-parser granite4 \ --chat-template examples/tool_chat_template_granite...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .0 H-Small Python-style tool calls_ The parser: - Uses `ast.parse` (no `eval`) to safely extract keyword arguments - Supports both batch and streaming modes - Is tokenizer-agnostic (no special tokens required) - Convert...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
