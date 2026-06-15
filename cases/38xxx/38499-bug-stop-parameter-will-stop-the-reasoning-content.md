# vllm-project/vllm#38499: [Bug]: "stop" parameter will stop the reasoning_content

| 字段 | 值 |
| --- | --- |
| Issue | [#38499](https://github.com/vllm-project/vllm/issues/38499) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "stop" parameter will stop the reasoning_content

### Issue 正文摘录

### Your current environment the input request: { "model": "Kimi", "messages": [ { "role": "user", "content": "元曲四大家有谁" } ], "ignore_eos": false, "max_completion_tokens": 1000, "stop": "四", "temperature": 0, "stream": true, "stream_options": { "include_usage": true } } the output response: data: {"id": "1dfa1784e6b64e09ade35bedf15798ed", "object": "chat.completion.chunk", "created": 1774598361, "model": "Kimi", "choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}}], "service_tier": "default", "first_token_return_time": 1774598361.9974504, "usage": null} data: {"id": "1dfa1784e6b64e09ade35bedf15798ed", "object": "chat.completion.chunk", "created": 1774598361, "model": "Kimi", "choices": [{"index": 0, "delta": {"role": "assistant", "content": "", "reasoning_content": " 用户"}}], "service_tier": "default", "first_token_return_time": 1774598361.9976811, "usage": null} data: {"id": "1dfa1784e6b64e09ade35bedf15798ed", "object": "chat.completion.chunk", "created": 1774598361, "model": "Kimi", "choices": [{"index": 0, "delta": {"role": "assistant", "content": "", "reasoning_content": "询问"}}], "service_tier": "default", "first_token_return_time": 1774598362.0438664, "usage"...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t"? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ", "content": "元曲四大家有谁" } ], "ignore_eos": false, "max_completion_tokens": 1000, "stop": "四", "temperature": 0, "stream": true, "stream_options": { "include_usage": true } } the output response: data: {"id": "1dfa1784e6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing_content bug ### Your current environment the input request: { "model": "Kimi", "messages": [ { "role": "user", "content": "元曲四大家有谁" } ], "ignore_eos": false, "max_completion_tokens": 1000, "stop": "四", "temperature"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: l stop the reasoning_content bug ### Your current environment the input request: { "model": "Kimi", "messages": [ { "role": "user", "content": "元曲四大家有谁" } ], "ignore_eos": false, "max_completion_tokens": 1000, "stop": "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
