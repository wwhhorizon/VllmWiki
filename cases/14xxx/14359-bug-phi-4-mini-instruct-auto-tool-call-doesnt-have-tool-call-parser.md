# vllm-project/vllm#14359: [Bug]: phi-4-mini-instruct auto tool call doesnt have tool-call-parser

| 字段 | 值 |
| --- | --- |
| Issue | [#14359](https://github.com/vllm-project/vllm/issues/14359) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: phi-4-mini-instruct auto tool call doesnt have tool-call-parser

### Issue 正文摘录

### 🐛 Describe the bug vllm serve unsloth/Phi-4-mini-instruct-unsloth-bnb-4bit --dtype bfloat16 --quantization bitsandbytes --load-format bitsandbytes --enforce-eager --max-model-len 4096 --gpu-memory-utilization 0.8 ```python from openai import OpenAI import json client = OpenAI(base_url="http://localhost:8000/v1",api_key="none") def get_weather(location: str, unit: str): return f"Getting the weather for {location} in {unit}..." tool_functions = {"get_weather": get_weather} tools = [{ "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]} }, "required": ["location", "unit"] } } }] # tools = [{"name": "get_weather_updates", "description": "Fetches weather updates for a given city using the RapidAPI Weather API.", "parameters": {"city": {"description": "The name of the city for which to retrieve weather information.", "type": "str", "default": "London"}}}] response = client.chat.completions.create( model=client.models....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cribe the bug vllm serve unsloth/Phi-4-mini-instruct-unsloth-bnb-4bit --dtype bfloat16 --quantization bitsandbytes --load-format bitsandbytes --enforce-eager --max-model-len 4096 --gpu-memory-utilization 0.8 ```python f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: --max-model-len 4096 --gpu-memory-utilization 0.8 ```python from openai import OpenAI import json client = OpenAI(base_url="http://localhost:8000/v1",api_key="none") def get_weather(location: str, unit: str): return f"G...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uct-unsloth-bnb-4bit --dtype bfloat16 --quantization bitsandbytes --load-format bitsandbytes --enforce-eager --max-model-len 4096 --gpu-memory-utilization 0.8 ```python from openai import OpenAI import json client = Ope...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: phi-4-mini-instruct auto tool call doesnt have tool-call-parser bug;stale ### 🐛 Describe the bug vllm serve unsloth/Phi-4-mini-instruct-unsloth-bnb-4bit --dtype bfloat16 --quantization bitsandbytes --load-format bi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 00} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
