# vllm-project/vllm#13530: [Bug]:  Tool calling stuck with Llama 3.1 405B INT4 Quantized

| 字段 | 值 |
| --- | --- |
| Issue | [#13530](https://github.com/vllm-project/vllm/issues/13530) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Tool calling stuck with Llama 3.1 405B INT4 Quantized

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to enable tool calling on Llama 3.1 8B and 405B INT4 on vLLM to get it to work with this code ```python from openai import OpenAI import json client = OpenAI(base_url="http://localhost:8080/v1", api_key="dumm") def get_weather(location: str, unit: str): return f"Getting the weather for {location} in {unit}..." tool_functions = {"get_weather": get_weather} tools = [{ "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]} }, "required": ["location", "unit"] } } }] response = client.chat.completions.create( model="hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4", messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}], tools=tools, # tool_choice="auto", # max_tokens=150 ) print(response) tool_call = response.choices[0].message.tool_calls[0].function print(f"Function called: {tool_call.name}") print(f"Arguments: {tool_call.argumen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 05B INT4 on vLLM to get it to work with this code ```python from openai import OpenAI import json client = OpenAI(base_url="http://localhost:8080/v1", api_key="dumm") def get_weather(location: str, unit: str): return f"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Tool calling stuck with Llama 3.1 405B INT4 Quantized bug ### Your current environment ### 🐛 Describe the bug I tried to enable tool calling on Llama 3.1 8B and 405B INT4 on vLLM to get it to work with this code...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Tool calling stuck with Llama 3.1 405B INT4 Quantized bug ### Your current environment ### 🐛 Describe the bug I tried to enable tool calling on Llama 3.1 8B and 405B INT4 on vLLM to get it to work with this code...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: )}") ``` ### vLLM output ``` INFO 02-19 00:34:45 logger.py:37] Received request chatcmpl-439500bfa28c46869e5ef9e42aebe695: prompt: ' system \n\nEnvironment: ipython\nCutting Knowledge Date: December 2023\nToday Date: 19...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: our ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
