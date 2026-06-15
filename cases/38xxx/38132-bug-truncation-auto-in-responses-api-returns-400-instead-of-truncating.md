# vllm-project/vllm#38132: [Bug]: truncation: "auto" in Responses API returns 400 instead of truncating input

| 字段 | 值 |
| --- | --- |
| Issue | [#38132](https://github.com/vllm-project/vllm/issues/38132) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: truncation: "auto" in Responses API returns 400 instead of truncating input

### Issue 正文摘录

### Your current environment ``` vLLM: version 0.15.0 Model: openai/gpt-oss-20b Endpoint: /v1/responses ``` ### 🐛 Describe the bug ### Description When using the Responses API with truncation: "auto", sending input that exceeds the model's context window returns a 400 error instead of truncating the input to fit. Per the OpenAI Responses API spec: `auto: If the input to this Response exceeds the model's context window size, the model will truncate the response to fit the context window by dropping items from the beginning of the conversation.` Currently, vLLM passes the full prompt to the engine without applying truncation, resulting in: `{'error': {'message': 'The engine prompt length 1327246 exceeds the max_model_len 131072. Please reduce prompt.', 'type': 'invalid_request_error', 'param': 'input', 'code': 400}} ` ### Reproduction Send a request to /v1/responses with truncation: "auto" and input that exceeds max_model_len: ``` import requests filler_message = "This is filler text to consume tokens. " * 50 num_messages = (131072 // 40) + 1 # enough to exceed 131072 context window oversized_input = [{"role": "user", "content": filler_message} for _ in range(num_messages)] response...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 0 instead of truncating input bug ### Your current environment ``` vLLM: version 0.15.0 Model: openai/gpt-oss-20b Endpoint: /v1/responses ``` ### 🐛 Describe the bug ### Description When using the Responses API with trun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uncating input bug ### Your current environment ``` vLLM: version 0.15.0 Model: openai/gpt-oss-20b Endpoint: /v1/responses ``` ### 🐛 Describe the bug ### Description When using the Responses API with truncation: "auto",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ceeds the max_model_len 131072. Please reduce prompt.', 'type': 'invalid_request_error', 'param': 'input', 'code': 400}} `
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
