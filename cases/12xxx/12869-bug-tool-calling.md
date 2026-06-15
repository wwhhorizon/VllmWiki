# vllm-project/vllm#12869: [Bug]: Tool Calling

| 字段 | 值 |
| --- | --- |
| Issue | [#12869](https://github.com/vllm-project/vllm/issues/12869) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tool Calling

### Issue 正文摘录

### Your current environment There is a bug when the function description contains Chinese。Normal when describing in English。 tools = [{ "type": "function", "function": { "name": "get_weather", "description": "查询天气信息时非常有用", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "城市名，比如北京、杭州"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]} }, "required": ["location", "unit"] } } }] vllm option: --tool-call-parser llama3_json --chat-template tool_chat_template_llama3.2_json.jinja ``` ERROR 02-07 14:44:37 llama_tool_parser.py:97] Error in extracting tool call from response. ERROR 02-07 14:44:37 llama_tool_parser.py:97] Traceback (most recent call last): ERROR 02-07 14:44:37 llama_tool_parser.py:97] File "/usr/python/lib/python3.11/site-packages/vllm/entrypoints/openai/tool_parsers/llama_tool_parser.py", line 74, in extract_tool_calls ERROR 02-07 14:44:37 llama_tool_parser.py:97] (obj, end_idx) = dec.raw_decode(model_output[start_idx:]) ERROR 02-07 14:44:37 llama_tool_parser.py:97] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-07 14:44:37 llama_tool_parser.py:97] File "/usr/python/lib/python3.11/json/decoder.py", line 355, i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ocation", "unit"] } } }] vllm option: --tool-call-parser llama3_json --chat-template tool_chat_template_llama3.2_json.jinja ``` ERROR 02-07 14:44:37 llama_tool_parser.py:97] Error in extracting tool call from response....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nja ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ROR 02-07 14:44:37 llama_tool_parser.py:97] (obj, end_idx) = dec.raw_decode(model_output[start_idx:]) ERROR 02-07 14:44:37 llama_tool_parser.py:97] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-07 14:44:37 llama_too...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
