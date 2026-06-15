# vllm-project/vllm#38910: [Bug]: Gemma4 tool parser duplicates HTML tag prefixes in streamed tool arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#38910](https://github.com/vllm-project/vllm/issues/38910) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 tool parser duplicates HTML tag prefixes in streamed tool arguments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `Gemma4ToolParser.extract_tool_calls_streaming()` can corrupt normal text that appears after or inside streamed tool calls. The simplest visible symptom is that plain text such as: ```text ``` can be turned into: ```text ``` A more serious real-world symptom shows up when a tool argument contains HTML content, for example `write_file(content=...)`. In that case tags such as ` ` and ` ` can be corrupted into malformed output like: ```html ``` and can further degrade into duplicated tag names such as ` ... call:write_file{ path: index.html , content: \n \n \n \n \n } ``` Observed corrupted output (with old logic): ```html html lang="zh-CN"> meta charset="UTF-8"> ``` Expected output: ```html ``` ### Suggested fix Keep `current_text` from the upstream streaming state and use buffered `delta_text` only for emission. Do not reconstruct `current_text` from `previous_text + buffered_delta_text`. ### Additional context I already searched for existing issues/PRs around this Gemma4 streaming duplication path and did not find an open match. A proposed fix is available in: - PR #38909

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: evious_text + buffered_delta_text`. ### Additional context I already searched for existing issues/PRs around this Gemma4 streaming duplication path and did not find an open match. A proposed fix is available in: - PR #3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Gemma4 tool parser duplicates HTML tag prefixes in streamed tool arguments ### Your current environment ### 🐛 Describe the bug `Gemma4ToolParser.extract_tool_calls_streaming()` can corrupt normal text that appear...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma4 tool parser duplicates HTML tag prefixes in streamed tool arguments ### Your current environment ### 🐛 Describe the bug `Gemma4ToolParser.extract_tool_calls_streaming()` can corrupt normal text that appear...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
