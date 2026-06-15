# vllm-project/vllm#32213: [Bug]: GLM4 tool parser crashes with TypeError when parsing tools with no arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#32213](https://github.com/vllm-project/vllm/issues/32213) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM4 tool parser crashes with TypeError when parsing tools with no arguments

### Issue 正文摘录

### 🐛 Describe the bug When using the GLM4 tool parser (`--tool-call-parser glm47`) with tools that have **no required or optional arguments**, the parser crashes with a `TypeError`. **Error traceback:** ``` ERROR [glm4_moe_tool_parser.py:123] Failed to extract tool call spec Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/tool_parsers/glm4_moe_tool_parser.py", line 104, in extract_tool_calls pairs = self.func_arg_regex.findall(tc_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ TypeError: expected string or buffer WARNING [glm4_moe_tool_parser.py:172] Failed to extract any tool calls. ``` **Root cause:** In `glm4_moe_tool_parser.py` line 104, when a tool has no arguments, the model outputs a tool call without any ` / ` pairs. The regex `func_detail_regex.search(match).group(2)` returns `None` or an empty match, and passing this to `func_arg_regex.findall(tc_args)` raises the TypeError because `findall()` expects a string, not `None`. **Affected code (lines 102-106):** ```python tc_detail = self.func_detail_regex.search(match) tc_name = tc_detail.group(1) tc_args = tc_detail.group(2) # Can be None for zero-argument tools pairs = self.func_arg_regex....

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: = self.func_arg_regex.findall(tc_args) # TypeError here ``` ### How to reproduce 1. Start vLLM with GLM4 model and tool parser: ```bash vllm serve zai-org/GLM-4.7-FP8 \ --tool-call-parser glm47 \ --enable-auto-tool-choi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vLLM with GLM4 model and tool parser: ```bash vllm serve zai-org/GLM-4.7-FP8 \ --tool-call-parser glm47 \ --enable-auto-tool-choice ``` 2. Send a request with a tool that has no arguments: ```python tools = [ { "type":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: puts a tool call without any ` / ` pairs. The regex `func_detail_regex.search(match).group(2)` returns `None` or an empty match, and passing this to `func_arg_regex.findall(tc_args)` raises the TypeError because `findal...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: detail.group(2) pairs = self.func_arg_regex.findall(tc_args) if tc_args else [] ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: In `glm4_moe_tool_parser.py` line 104, when a tool has no arguments, the model outputs a tool call without any ` / ` pairs. The regex `func_detail_regex.search(match).group(2)` returns `None` or an empty match, and pass...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
