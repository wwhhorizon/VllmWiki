# vllm-project/vllm#16393: [Bug]: Qwen2.5 tool call failed

| 字段 | 值 |
| --- | --- |
| Issue | [#16393](https://github.com/vllm-project/vllm/issues/16393) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 tool call failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the tool is called in auto mode, the Qwen2.5-7B-Instruct model **cannot return content normally in the tool_calls field**, and the following **error** is thrown in the log: ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] Error in extracting tool call from response. ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] Traceback (most recent call last): ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] File "/usr/local/miniconda3/envs/vllm8/lib/python3.10/site-packages/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py", line 87, in extract_tool_calls ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] raw_function_calls = [ ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] File "/usr/local/miniconda3/envs/vllm8/lib/python3.10/site-packages/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py", line 88, in ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] json.loads(match[0] if match[0] else match[1]) ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] File "/usr/local/miniconda3/envs/vllm8/lib/python3.10/json/__init__.py", line 346, in loads ERROR 04-10 14:44:33 [hermes_tool_parser.py:110] return _default_decoder.decode(s)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: {"role": "user", "content": "What's the temperature in San Francisco now? How about tomorrow?"} ], "tools": [ { "type": "function", "function": { "name": "get_current_temperature", "description": "Get current temperatur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen2.5 tool call failed bug;stale ### Your current environment ### 🐛 Describe the bug When the tool is called in auto mode, the Qwen2.5-7B-Instruct model **cannot return content normally in the tool_calls field*...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen2.5 tool call failed bug;stale ### Your current environment ### 🐛 Describe the bug When the tool is called in auto mode, the Qwen2.5-7B-Instruct model **cannot return content normally in the tool_calls field*...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rontend_api;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
