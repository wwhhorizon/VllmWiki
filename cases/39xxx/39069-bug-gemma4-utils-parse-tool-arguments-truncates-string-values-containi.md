# vllm-project/vllm#39069: [Bug]: gemma4_utils._parse_tool_arguments truncates string values containing internal quotes

| 字段 | 值 |
| --- | --- |
| Issue | [#39069](https://github.com/vllm-project/vllm/issues/39069) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gemma4_utils._parse_tool_arguments truncates string values containing internal quotes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm/tool_parsers/gemma4_utils._parse_tool_arguments()` (the **offline inference** tool call parser) truncates string values when they contain `"` (double quotes). **Root cause**: The function replaces ` ` delimiters with `"`, then uses a fallback regex `[^"]*` that stops at the first internal quote character. **Affected file**: `vllm/tool_parsers/gemma4_utils.py` **Not affected**: `vllm/tool_parsers/gemma4_tool_parser.py` (the API server parser handles ` ` delimiters natively without replacement, so it works correctly) #### Minimal reproduction ```python import regex as re # Extracted from vllm/tool_parsers/gemma4_utils.py (L52-90) _ESCAPE_TOKEN = ' ' def _parse_tool_arguments(args_str): if not args_str or not args_str.strip(): return {} cleaned = args_str.replace(_ESCAPE_TOKEN, '"') import json try: parsed = json.loads("{" + cleaned + "}") return {k: str(v) if not isinstance(v, str) else v for k, v in parsed.items()} except (json.JSONDecodeError, ValueError): pass arguments = {} for key, value in re.findall(r'(\w+):\s*"([^"]*)"', cleaned): arguments[key] = value if not arguments: for key, value in re.findall(r'(\w+):\s*([^,}]+...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gemma4_utils._parse_tool_arguments truncates string values containing internal quotes ### Your current environment ### 🐛 Describe the bug `vllm/tool_parsers/gemma4_utils._parse_tool_arguments()` (the **offline in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: eplacement, so it works correctly) #### Minimal reproduction ```python import regex as re # Extracted from vllm/tool_parsers/gemma4_utils.py (L52-90) _ESCAPE_TOKEN = ' ' def _parse_tool_arguments(args_str): if not args_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: instance(v, str) else v for k, v in parsed.items()} except (json.JSONDecodeError, ValueError): pass arguments = {} for key, value in re.findall(r'(\w+):\s*"([^"]*)"', cleaned): arguments[key] = value if not arguments: f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Root cause**: The function replaces ` ` delimiters with `"`, then uses a fallback regex `[^"]*` that stops at the first internal quote character. **Affected file**: `vllm/tool_parsers/gemma4_utils.py` **Not affected**:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: {" + cleaned + "}") return {k: str(v) if not isinstance(v, str) else v for k, v in parsed.items()} except (json.JSONDecodeError, ValueError): pass arguments = {} for key, value in re.findall(r'(\w+):\s*"([^"]*)"', clean...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
