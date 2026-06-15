# vllm-project/vllm#29725: [Bug]: Responses API: Streaming returns ResponseTextDeltaEvent instead of ResponseFunctionCallArgumentsDeltaEvent for tool calls while using non-harmony models

| 字段 | 值 |
| --- | --- |
| Issue | [#29725](https://github.com/vllm-project/vllm/issues/29725) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Responses API: Streaming returns ResponseTextDeltaEvent instead of ResponseFunctionCallArgumentsDeltaEvent for tool calls while using non-harmony models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the Responses API with streaming enabled and a tool call is expected for non-harmony models, for e.g. Qwen3, the stream emits ResponseTextDeltaEvent chunks instead of ResponseFunctionCallArgumentsDeltaEvent. As a result, the client cannot reliably detect or parse tool call arguments from the stream, since the payload appears as plain text deltas rather than structured function call argument events. ```python from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", # vLLM server URL api_key="not-used", ) tools = [ { "type": "function", "name": "get_weather", "description": "Get current temperature for a given location.", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "City and country, for example Paris, France", }, }, "required": ["location"], "additionalProperties": False, }, } ] stream = client.responses.create( model="Qwen/Qwen3-4B-Instruct-2507", input=[{"role": "user", "content": "What's the weather like in Paris today?"}], tools=tools, stream=True ) for event in stream: print(event) ``` ### Before submitting a new issue... - [x] Make sure yo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er than structured function call argument events. ```python from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", # vLLM server URL api_key="not-used", ) tools = [ { "type": "function", "name":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: seFunctionCallArgumentsDeltaEvent for tool calls while using non-harmony models bug;stale ### Your current environment ### 🐛 Describe the bug When using the Responses API with streaming enabled and a tool call is expect...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "required": ["location"], "additionalProperties": False, }, } ] stream = client.responses.create( model="Qwen/Qwen3-4B-Instruct-2507", input=[{"role": "user", "content": "What's the weather like in Paris today?"}], tool...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: allArgumentsDeltaEvent for tool calls while using non-harmony models bug;stale ### Your current environment ### 🐛 Describe the bug When using the Responses API with streaming enabled and a tool call is expected for non-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
