# vllm-project/vllm#33215: [Bug]: DeepSeek V3.2 `tool_choice==required` in thinking mode gives internal server error.

| 字段 | 值 |
| --- | --- |
| Issue | [#33215](https://github.com/vllm-project/vllm/issues/33215) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2 `tool_choice==required` in thinking mode gives internal server error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following request body causes internal server error with Deepseek V3.2. when calling the `/api/v1/chat/completions` endpoint. ``` { "max_tokens": 128, "messages": [ { "content": "Tell me a joke", "role": "user" } ], "tools": [ { "function": { "description": "API to get jokes", "name": "jokes", "parameters": { "num_jokes": "int" }, "type": "function" } } ], "tool_choice": "required", "model": "deepseek-v3.2", "n": 1, "stream": false, "temperature": 0.5, "chat_template_kwargs": {"thinking": true, "enable_thinking": true} } ``` ## My debugging When setting `stream=True` instead, I found that the tool call content was appearing as reasoning content. I believe the chain of events that caused this issue is as follows: 1. In `vllm/entrypoints/openai/chat_completion/serving.py`, the `self_preprocess_chat` method is called. 2. As defined in `vllm/entrypoints/openai/engine/serving.py`, the `_preprocess_chat` method calls `tool_parser(tokenizer).adjust_request(request=request)` 3. The tool parser defined for Deepseek V3.2 inherits the base `adjust_request` method from the `ToolParser` class. 4. As defined in `vllm/tool_parsers/abstract_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g the JSON schema to a regex schema using the `outlines_core.json_schema.build_regex_from_schema` function. Then if the request specified thinking, prepend a ` .* \n\n` to the resulting regex. I would imagine the `deeps...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ad. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": "required", "model": "deepseek-v3.2", "n": 1, "stream": false, "temperature": 0.5, "chat_template_kwargs": {"thinking": true, "enable_thinking": true} } ``` ## My debugging When setting `stream=True` instead, I found...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion" } } ], "tool_choice": "required", "model": "deepseek-v3.2", "n": 1, "stream": false, "temperature": 0.5, "chat_template_kwargs": {"thinking": true, "enable_thinking": true} } ``` ## My debugging When setting `stre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g ### Your current environment ### 🐛 Describe the bug The following request body causes internal server error with Deepseek V3.2. when calling the `/api/v1/chat/completions` endpoint. ``` { "max_tokens": 128, "messages"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
