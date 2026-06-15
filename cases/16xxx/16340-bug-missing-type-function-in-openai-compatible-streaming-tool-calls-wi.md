# vllm-project/vllm#16340: [Bug]: Missing "type":"function" in OpenAI-Compatible Streaming Tool Calls with specific tool_choice

| 字段 | 值 |
| --- | --- |
| Issue | [#16340](https://github.com/vllm-project/vllm/issues/16340) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing "type":"function" in OpenAI-Compatible Streaming Tool Calls with specific tool_choice

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Issue Overview When using streaming responses with a specific tool choice (`"tool_choice": {"type": "function", "function": {"name": "xxx"}}`), VLLM's streaming output format doesn't comply with the OpenAI API standard. Specifically, the first tool call chunk is missing the required `"type":"function"` field. # Steps to Reproduce 1. Start VLLM server with the following command: ```bash vllm serve Qwen/Qwen2.5-7B-Instruct-AWQ \ --quantization awq \ --served-model-name qwen2.5-7b-instruct \ --api-key xxx \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --gpu-memory-utilization 0.9 \ --max-model-len 8192 \ --max-num-seqs 512 ``` 2. Make a request with specific `tool_choice`: ```bash curl --location --request POST 'http://127.0.0.1:8000/v1/chat/completions' \ --header 'Authorization: Bearer xxx' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "qwen2.5-7b-instruct", "messages": [{"role": "user", "content": "What is the weather like in Boston today?"}], "tools": [{ "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: sing "type":"function" in OpenAI-Compatible Streaming Tool Calls with specific tool_choice bug ### Your current environment ### 🐛 Describe the bug # Issue Overview When using streaming responses with a specific tool cho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pe": "function", "function": {"name": "xxx"}}`), VLLM's streaming output format doesn't comply with the OpenAI API standard. Specifically, the first tool call chunk is missing the required `"type":"function"` field. # S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: at. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: \ --max-model-len 8192 \ --max-num-seqs 512 ``` 2. Make a request with specific `tool_choice`: ```bash curl --location --request POST 'http://127.0.0.1:8000/v1/chat/completions' \ --header 'Authorization: Bearer xxx' \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;quantization;speculative_decoding cuda;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
