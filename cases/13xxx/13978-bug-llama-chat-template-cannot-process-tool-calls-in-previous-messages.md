# vllm-project/vllm#13978: [Bug]: Llama chat template cannot process tool_calls=[] in previous messages

| 字段 | 值 |
| --- | --- |
| Issue | [#13978](https://github.com/vllm-project/vllm/issues/13978) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama chat template cannot process tool_calls=[] in previous messages

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The chat template for Llama 3.1 and 3.2 asserts that `len(tool_calls) == 1` for each message with attribute `tool_calls` in the request. If `tool_calls: []` is provided in an assistant message as part of the request, the chat template throws and vLLM rejects the request. To reproduce: ```bash vllm serve meta-llama/Llama-3.1-8B-Instruct \ --enable-auto-tool-choice \ --tool-call-parser llama3_json \ --chat-template examples/tool_chat_template_llama3.1_json.jinja ``` ```python from openai import OpenAI import json client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") def get_weather(location: str, unit: str): return f"Getting the weather for {location} in {unit}..." tool_functions = {"get_weather": get_weather} tools = [{ "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]} }, "required": ["location", "unit"] } } }] response = client.chat.completions.c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: amples/tool_chat_template_llama3.1_json.jinja ``` ```python from openai import OpenAI import json client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") def get_weather(location: str, unit: str): return f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama chat template cannot process tool_calls=[] in previous messages bug;stale ### Your current environment ### 🐛 Describe the bug The chat template for Llama 3.1 and 3.2 asserts that `len(tool_calls) == 1` for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lama chat template cannot process tool_calls=[] in previous messages bug;stale ### Your current environment ### 🐛 Describe the bug The chat template for Llama 3.1 and 3.2 asserts that `len(tool_calls) == 1` for each mes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: home/benchislett/Repos/vllm/.venv/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/home/benchislett/Repos/vllm/.venv/lib/python3.12/site-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
