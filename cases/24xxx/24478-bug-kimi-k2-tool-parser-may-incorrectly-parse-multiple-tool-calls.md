# vllm-project/vllm#24478: [Bug]: Kimi-K2 tool parser may incorrectly parse multiple tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#24478](https://github.com/vllm-project/vllm/issues/24478) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2 tool parser may incorrectly parse multiple tool calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: I am testing multiple tool calls with the Kimi-K2 model using the following Python example. It seems that the parser may not handle multiple tools correctly, possibly due to a regex issue in the parser. Example Code: ```python import requests def get_weather(latitude, longitude): response = requests.get( f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m" ) data = response.json() return data['current']['temperature_2m'] def get_news(topic: str): """Simulated news API for testing""" url = "https://jsonplaceholder.typicode.com/posts" response = requests.get(url) return response.json() def test_multiple_tools(): """Test multiple tools are enumerated and called (response format validation)""" tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get current weather", "parameters": { "type": "object", "properties": { "latitude": {"type": "number"}, "longitude": {"type": "number"} }, "required": ["latitude", "longitude"], "additionalProperties": False }, "strict": Tr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y, possibly due to a regex issue in the parser. Example Code: ```python import requests def get_weather(latitude, longitude): response = requests.get( f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the bug Description: I am testing multiple tool calls with the Kimi-K2 model using the following Python example. It seems that the parser may not handle multiple tools correctly, possibly due to a regex issue in the par...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: Kimi-K2 tool parser may incorrectly parse multiple tool calls bug;unstale ### Your current environment ### 🐛 Describe the bug Description: I am testing multiple tool calls with the Kimi-K2 model using the following...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: stions. development distributed_parallel;frontend_api;model_support cuda;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
