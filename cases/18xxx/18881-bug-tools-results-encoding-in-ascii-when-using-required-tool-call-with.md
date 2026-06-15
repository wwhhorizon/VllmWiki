# vllm-project/vllm#18881: [Bug]: Tools results encoding in ascii when using "required" tool call with server.

| 字段 | 值 |
| --- | --- |
| Issue | [#18881](https://github.com/vllm-project/vllm/issues/18881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tools results encoding in ascii when using "required" tool call with server.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using tool_choice='required' option in the chat completion API. The arguments of the used function are returned in ascii encoding, which is a problem for non-English languages. ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") def get_weather(location: str, unit: str): return f"Getting the weather for {location} in {unit}..." tool_functions = {"get_weather": get_weather} tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "Имя города на русском языке", }, "unit": {"type": "string", "enum": ["Цельсий", "фаренгейт"]}, }, "required": ["location", "unit"], }, }, } ] response = client.chat.completions.create( model=client.models.list().data[0].id, messages=[{"role": "user", "content": "Какая погода в Москве?"}], tools=tools, tool_choice="required", ) tool_call = response.choices[0].message.tool_calls[0].function print(f"Function called: {tool_call.name}") print(f"Arguments: {tool_call.arguments}") ```...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Tools results encoding in ascii when using "required" tool call with server. bug ### Your current environment ### 🐛 Describe the bug When using tool_choice='required' option in the chat completion API. The argume...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rs. ```python arguments=json.dumps(tool_call.parameters, ensure_ascii=False))) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: }, }, } ] response = client.chat.completions.create( model=client.models.list().data[0].id, messages=[{"role": "user", "content": "Какая погода в Москве?"}], tools=tools, tool_choice="required", ) tool_call = response.c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
