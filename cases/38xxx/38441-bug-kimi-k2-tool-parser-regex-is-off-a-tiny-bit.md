# vllm-project/vllm#38441: [Bug]: kimi-k2 tool parser regex is off a tiny bit

| 字段 | 值 |
| --- | --- |
| Issue | [#38441](https://github.com/vllm-project/vllm/issues/38441) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi-k2 tool parser regex is off a tiny bit

### Issue 正文摘录

### Your current environment current main - irrespective of env ### 🐛 Describe the bug Sometimes with Kimi K2.5, the parser drops the tool calls in `tool_choice: auto` (without constrained decoding). When the model generates tool calls during streaming, the model sometimes emits a `\n` (newline) between the ` ` token and the function name. For example, instead of producing: ``` functions.edit:15 {"path": "..."} ``` it produces: ``` functions.edit:15 {"path": "..."} ``` (I am unable to provide the full trace here because it has a lot of personal crap in it, and I only observe this with long contexts and unable to repro as a canonical example). --- https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/kimi_k2_tool_parser.py#L70 ```py self.stream_tool_call_portion_regex = re.compile( r"(?P .+:\d+)\s* \s*(?P .*)" ) self.stream_tool_call_name_regex = re.compile(r"(?P .+:\d+)\s*") ``` From my reading: 1. `stream_tool_call_portion_regex` -- matches the full pattern: tool call ID + arguments 2. `stream_tool_call_name_regex` -- matches just the tool call ID portion Both use `.+` to match the tool call ID (e.g. `functions.edit:15`). The problem is that in Python, `.` does not mat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: etween the ` ` token and the function name. For example, instead of producing: ``` functions.edit:15 {"path": "..."} ``` it produces: ``` functions.edit:15 {"path": "..."} ``` (I am unable to provide the full trace here...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l calls in `tool_choice: auto` (without constrained decoding). When the model generates tool calls during streaming, the model sometimes emits a `\n` (newline) between the ` ` token and the function name. For example, i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ll for further investigation: I dont think this has side-effects from my testing on Kimi K2.5. But maybe, something leaks into Kimi K2 Thinking - but I cannot find enough time to get this testing in. ### Before submitti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
