# vllm-project/vllm#21565: [Bug]: Qwen3 failed to get function with stream and named function calling when thinking is disabled

| 字段 | 值 |
| --- | --- |
| Issue | [#21565](https://github.com/vllm-project/vllm/issues/21565) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 failed to get function with stream and named function calling when thinking is disabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using Qwen3 by online serving with tool choice enabled, the model failed to get the function with streaming output and named function calling when thinking is disabled. Online serving command: ``` vllm serve Qwen/Qwen3-4B --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser Hermes ``` Code: ```Python from openai import OpenAI # Now, simulate a tool call def get_current_weather(city: str, state: str, unit: "str"): return ( "The weather in Dallas, Texas is 85 degrees fahrenheit. It is " "partly cloudly, with highs in the 90's." ) available_tools = {"get_current_weather": get_current_weather} # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" properties = { "city": { "type": "string", "description": "The city to find the weather for, e.g. 'San Francisco'", }, "state": { "type": "string", "description": "the two-letter abbreviation for the state that the city is" " in, e.g. 'CA' which would mean 'California'", }, "unit": { "type": "string", "description": "The unit to fetch the temperature in", "enum": ["celsius", "fahrenheit"],...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: o-tool-choice --tool-call-parser Hermes ``` Code: ```Python from openai import OpenAI # Now, simulate a tool call def get_current_weather(city: str, state: str, unit: "str"): return ( "The weather in Dallas, Texas is 85...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 failed to get function with stream and named function calling when thinking is disabled bug ### Your current environment ### 🐛 Describe the bug When using Qwen3 by online serving with tool choice enabled, t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: arguments[tool_call_idx] += tool_call.function.arguments else: if hasattr(chunk.choices[0].delta, "reasoning_content"): reasoning_content += chunk.choices[0].delta.reasoning_content return reasoning_content, arguments,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
