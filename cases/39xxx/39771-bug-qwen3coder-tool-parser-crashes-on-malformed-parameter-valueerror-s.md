# vllm-project/vllm#39771: [Bug]: Qwen3Coder tool parser crashes on malformed <parameter=...> (ValueError: substring not found)

| 字段 | 值 |
| --- | --- |
| Issue | [#39771](https://github.com/vllm-project/vllm/issues/39771) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3Coder tool parser crashes on malformed <parameter=...> (ValueError: substring not found)

### Issue 正文摘录

### Your current environment vLLM main branch with `Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8` (or any Qwen3-Coder model). ### 🐛 Describe the bug `Qwen3CoderToolParser._parse_xml_function_call` uses `str.index(">")` on each ` ` match. When a parameter is truncated or malformed (no `>` separator between name and value), this raises `ValueError: substring not found`. The error is caught by a broad `except Exception` in `extract_tool_calls`, but the catch causes the **entire tool call extraction to fail** — discarding any well-formed parameters and other tool calls in the same response, and forcing a fallback to plain text content. #### Stack trace ``` ERROR [qwen3coder_tool_parser.py:344] Error in extracting tool call from response. ERROR [qwen3coder_tool_parser.py:344] Traceback (most recent call last): ERROR [qwen3coder_tool_parser.py:344] File ".../qwen3coder_tool_parser.py", line 317, in extract_tool_calls ERROR [qwen3coder_tool_parser.py:344] self._parse_xml_function_call(function_call_str, request.tools) ERROR [qwen3coder_tool_parser.py:344] File ".../qwen3coder_tool_parser.py", line 259, in _parse_xml_function_call ERROR [qwen3coder_tool_parser.py:344] idx = match_text.index(">")...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3Coder tool parser crashes on malformed <parameter=...> (ValueError: substring not found) ### Your current environment vLLM main branch with `Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8` (or any Qwen3-Coder model)....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rmed parameters and other tool calls in the same response, and forcing a fallback to plain text content. #### Stack trace ``` ERROR [qwen3coder_tool_parser.py:344] Error in extracting tool call from response. ERROR [qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: well-formed parameters and other tool calls in the same response, and forcing a fallback to plain text content. #### Stack trace ``` ERROR [qwen3coder_tool_parser.py:344] Error in extracting tool call from response. ERR...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nt environment vLLM main branch with `Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8` (or any Qwen3-Coder model). ### 🐛 Describe the bug `Qwen3CoderToolParser._parse_xml_function_call` uses `str.index(">")` on each ` ` match. Wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tool_parser.py:344] self._parse_xml_function_call(function_call_str, request.tools) ERROR [qwen3coder_tool_parser.py:344] File ".../qwen3coder_tool_parser.py", line 259, in _parse_xml_function_call ERROR [qwen3coder_too...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
