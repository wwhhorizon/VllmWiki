# vllm-project/vllm#9754: [Bug]: vLLM ignore the response from a tool call

| 字段 | 值 |
| --- | --- |
| Issue | [#9754](https://github.com/vllm-project/vllm/issues/9754) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM ignore the response from a tool call

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the tool call example - weather prediction. I'm using vLLM 0.63 with meta-llama/Meta-Llama-3.1-8B-Instruct ( vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --dtype auto --port 5001 --disable-log-stats --uvicorn-log-level warning --disable-log-requests --enable-auto-tool-choice --tool-call-parser llama3_json ) 1. I starts with system and user messages. 2. vLLM response with a tool_calls 3. I execute the call 4. I send the response to vLLM I expect to get a content response like "The wheather in SF is sunny" but instead i get another tool_calls response The code below just send the 4 messages at once and get the wrong (tool_calls) response. ```code import requests messages = [{'content': 'You are a helpful bot named Fred.', 'role': 'system'}, {'content': "What is your name and what is the weather in SF?", 'role': 'user'}, {'content': None, 'role': 'assistant', 'tool_calls': [{'type': 'function', 'id': 'chatcmpl-tool-e8cdb13de9204716960f82368dbc191d', 'function': {'name': 'check_weather', 'arguments': '{"location": "SF"}'}}]}, {'content': "It is always sunny in SF", 'role': 'tool', 'to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the 4 messages at once and get the wrong (tool_calls) response. ```code import requests messages = [{'content': 'You are a helpful bot named Fred.', 'role': 'system'}, {'content': "What is your name and what is the weat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM ignore the response from a tool call bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the tool call example - weather prediction. I'm using vLLM 0.6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ... ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: response from a tool call bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the tool call example - weather prediction. I'm using vLLM 0.63 with meta-llama/Meta-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
