# vllm-project/vllm#11498: [Bug]: 'int' object has no attribute 'parser_state'

| 字段 | 值 |
| --- | --- |
| Issue | [#11498](https://github.com/vllm-project/vllm/issues/11498) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'int' object has no attribute 'parser_state'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am deploying Qwen2.5-72B-AWQ using vLLM version 0.6.5 on an A800 GPU to provide services for other users within a company. One of the users encountered a crash in the model service when they attempted to use `response_format` with `outlines` as the `guided_decoding_backend`. This caused the model service to exit unexpectedly. The user's request parameters are roughly as follows: ```json { "model": "Qwen2.5-72B", "messages": [ { "role": "user", "content": "我想知道现在北京天气怎么样" } ], "response_format": { "type": "json_object", "json_schema": { "name": "get_weather", "description": "Fetches the weather in the given location", "strict": true, "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The location to get the weather for" } }, "additionalProperties": false, "required": [ "location" ] } } }, "guided_decoding_backend": "outlines" } ``` I tried to use `xgrammer`, and it works fine. Tracebacks as follows: ``` AttributeError("Error in model execution: 'int' object has no attribute 'parser_state'") Traceback (most recent call last): File "/usr/local/lib/py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onse_ ### 🐛 Describe the bug I am deploying Qwen2.5-72B-AWQ using vLLM version 0.6.5 on an A800 GPU to provide services for other users within a company. One of the users encountered a crash in the model service when th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t_instruction( File "/usr/local/lib/python3.10/dist-packages/outlines/fsm/guide.py", line 149, in get_next_instruction if state.parser_state is None: AttributeError: 'int' object has no attribute 'parser_state' ``` ![im...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: attribute 'parser_state' bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am deploying Qwen2.5-72B-AWQ using vLLM version 0.6.5 on an A800 GPU to provide services for o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: 'int' object has no attribute 'parser_state' bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am deploying Qwen2.5-72B-AWQ using vLLM version 0.6.5 on an A800 GP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tempted to use `response_format` with `outlines` as the `guided_decoding_backend`. This caused the model service to exit unexpectedly. The user's request parameters are roughly as follows: ```json { "model": "Qwen2.5-72...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
