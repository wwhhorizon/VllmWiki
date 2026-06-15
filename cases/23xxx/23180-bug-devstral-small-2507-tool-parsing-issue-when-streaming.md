# vllm-project/vllm#23180: [Bug]: Devstral-Small-2507 tool parsing issue when streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#23180](https://github.com/vllm-project/vllm/issues/23180) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Devstral-Small-2507 tool parsing issue when streaming

### Issue 正文摘录

### Your current environment docker image `vllm-openai:v0.10.1` ### 🐛 Describe the bug The following snippet: ```python model = "mistralai/Devstral-Small-2507" tools = [{ "type": "function", "function": { "name": "get_weather", "description": "Get the weather forecast in a given location", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}, "days": {"type": "integer", "description":"Amount of days to forecast"} }, "required": ["location", "unit", "days"] } } }] messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What's the weather for the next 5 days in San Francisco and in Miami?"} ] stream = client.chat.completions.create( model=model, messages=[{"role": "user", "content": "What's the weather for the next 5 days in San Francisco and in Miami?"}], tools=tools, tool_choice="auto", stream=True, ) print(list(stream)) ``` Raises the following vLLM error: ``` │ (APIServer pid=1) ERROR 08-19 06:54:43 [mistral_tool_parser.py:365] json.decoder.JSONDecodeError: Expecting value: line 1 co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ool parsing issue when streaming bug;stale ### Your current environment docker image `vllm-openai:v0.10.1` ### 🐛 Describe the bug The following snippet: ```python model = "mistralai/Devstral-Small-2507" tools = [{ "type...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Devstral-Small-2507 tool parsing issue when streaming bug;stale ### Your current environment docker image `vllm-openai:v0.10.1` ### 🐛 Describe the bug The following snippet: ```python model = "mistralai/Devstral-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Devstral-Small-2507 tool parsing issue when streaming bug;stale ### Your current environment docker image `vllm-openai:v0.10.1` ### 🐛 Describe the bug The following snippet: ```python model = "mistralai/Devstral-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: penai:v0.10.1` ### 🐛 Describe the bug The following snippet: ```python model = "mistralai/Devstral-Small-2507" tools = [{ "type": "function", "function": { "name": "get_weather", "description": "Get the weather forecast...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
