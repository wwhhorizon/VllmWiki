# vllm-project/vllm#32006: [Bug]: vLLM  hangs on specific request each time (qwen-coder-480b-fp8)

| 字段 | 值 |
| --- | --- |
| Issue | [#32006](https://github.com/vllm-project/vllm/issues/32006) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM  hangs on specific request each time (qwen-coder-480b-fp8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sending a /chat/completions request that contains `"response_format": { "type": "json_object" }`, `"tool_choice": "required"` and any results in: ``` WARNING 01-08 17:30:59 [protocol.py:116] The following fields were present in the request but ignored: f'strict'] APIServer pid=1) INFO 01-98 17:30:59 [qwen3coder_tool_parser.py:83] vLLM Successfully import tool parser Qwen3CoderToolParser EngineCore _DP0 pid=266) Exception in thread Thread-4 (process_input_sockets): EngineCore_DPO pid=266) Traceback (most recent call last): 32 + EngineCore_OP8 pid=266 (EngineCore_DPO pid=266) File "/usr/local/lib/python3.12/dist-packages/vllm/sampling_params.py", line 65, in __post_init_ raise ValueError ValueError: You can only use one kind of structured outputs constraint but multiple are specified: t'json': f"type': 'array', "minItems' items': f'type': 'object', 'anyOf': [f'properties': ('name': f'type': 'string', 'enum': ['get_temperature'], 'parameters': f'type': 'object', 'properties' ('city': ('type': 'string', 'description': 'City name.'", "required': ['city']], 'required': ['name', 'parameters']]]), 'regex': None, 'choice': None, 'grammar...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: vLLM hangs on specific request each time (qwen-coder-480b-fp8) bug ### Your current environment ### 🐛 Describe the bug Sending a /chat/completions request that contains `"response_format": { "type": "json_object"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM hangs on specific request each time (qwen-coder-480b-fp8) bug ### Your current environment ### 🐛 Describe the bug Sending a /chat/completions request that contains `"response_format": { "type": "json_object"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gex': None, 'choice': None, 'grammar None, 'json_object': True, 'disable_fallback': False, 'disable_any_whitespace': False, 'disable_additional_properties': False, 'whitespace_pattern': None, 'str Jctural_tag': None, '_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: vLLM hangs on specific request each time (qwen-coder-480b-fp8) bug ### Your current environment ### 🐛 Describe the bug Sending a /chat/completions request that contains `"response_format": { "type": "json_object"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
