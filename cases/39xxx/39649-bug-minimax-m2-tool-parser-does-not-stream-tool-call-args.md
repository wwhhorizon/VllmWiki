# vllm-project/vllm#39649: [Bug]: minimax_m2_tool_parser does not stream tool call args

| 字段 | 值 |
| --- | --- |
| Issue | [#39649](https://github.com/vllm-project/vllm/issues/39649) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: minimax_m2_tool_parser does not stream tool call args

### Issue 正文摘录

### Your current environment current main - irrespective of env ### 🐛 Describe the bug The core issue is in `_extract_delta_tool_calls` and how `extract_tool_calls_streaming` uses it. Two key locations: **1. The regex-based batch extraction (lines 303-306)** -- only finds *completed* invoke blocks: https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/minimax_m2_tool_parser.py#L304 ```py complete_invokes = self.invoke_complete_regex.findall(current_text) delta_tool_calls: list[DeltaToolCall] = [] while len(complete_invokes) > self.current_tool_index: ``` It calls `invoke_complete_regex` (` `) which only matches when the entire ` ` closing tag has arrived. Until then, `complete_invokes` stays empty and nothing is emitted. --- **2. The streaming method returns `None` for all intermediate tokens (lines 434 onwards)**: https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/minimax_m2_tool_parser.py#L434 ```py # Extract newly completed blocks as DeltaToolCalls. delta_tool_calls = self._extract_delta_tool_calls(current_text, request) if delta_tool_calls or content_before: return DeltaMessage( content=content_before, tool_calls=delta_tool_calls, ) ``` When `delta_too...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the fix would need to: 1. Track partial ` ` / ` ` state incrementally - link the GLM 4.7 tool parser does 2. Emit the tool call name as soon as ` ` is parsed 3. Stream ` ` content as argument fragments as tokens arrive...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ased batch extraction (lines 303-306)** -- only finds *completed* invoke blocks: https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/minimax_m2_tool_parser.py#L304 ```py complete_invokes = self.invoke_compl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: delta_tool_calls = self._extract_delta_tool_calls(current_text, request) if delta_tool_calls or content_before: return DeltaMessage( content=content_before, tool_calls=delta_tool_calls, ) ``` When `delta_tool_calls` is
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
