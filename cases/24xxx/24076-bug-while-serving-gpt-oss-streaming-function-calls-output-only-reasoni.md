# vllm-project/vllm#24076: [Bug]: While serving GPT-OSS, Streaming function calls output only reasoning_text, without function tool call

| 字段 | 值 |
| --- | --- |
| Issue | [#24076](https://github.com/vllm-project/vllm/issues/24076) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: While serving GPT-OSS, Streaming function calls output only reasoning_text, without function tool call

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug after serving gpt-oss-120b using vllm, I tried streaming function call examples according to openai cookbook [streaming function call](https://platform.openai.com/docs/guides/function-calling#streaming). - if set `stream=True` in CLIENT.responses.create(...), the output event contains reasoning_text, but function tool call is not included. like this, ``` ResponseCreatedEvent(response=Response(id='resp_f76035824b624b3da83ce3cb6eefdf8f', created_at=1756783814.0, error=None, incomplete_details=None, instructions=None, metadata=None, model='gpt-oss-120b', object='response', output=[], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='get_weather', parameters={'type': 'object', 'properties': {'location': {'type': 'string', 'description': 'City and country e.g. Bogotá, Colombia'}}, 'required': ['location'], 'additionalProperties': False}, strict=None, type='function', description='Get current temperature for a given location.')], top_p=1.0, background=False, max_output_tokens=130933, max_tool_calls=None, previous_response_id=None, prompt=None, prompt_cache_key=None, reasoning=None, safety_identifi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 'object', 'properties': {'location': {'type': 'string', 'description': 'City and country e.g. Bogotá, Colombia'}}, 'required': ['location'], 'additionalProperties': False}, strict=None, type='function', description='Get...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: at=1756783814.0, error=None, incomplete_details=None, instructions=None, metadata=None, model='gpt-oss-120b', object='response', output=[], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[FunctionT...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: While serving GPT-OSS, Streaming function calls output only reasoning_text, without function tool call bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug after serving gpt-oss-120b using vllm,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: unction calls output only reasoning_text, without function tool call bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug after serving gpt-oss-120b using vllm, I tried streaming function call examples...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
