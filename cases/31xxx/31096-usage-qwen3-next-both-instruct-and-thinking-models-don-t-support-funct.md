# vllm-project/vllm#31096: [Usage]: Qwen3-Next: Both Instruct and Thinking models don't support function calling

| 字段 | 值 |
| --- | --- |
| Issue | [#31096](https://github.com/vllm-project/vllm/issues/31096) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen3-Next: Both Instruct and Thinking models don't support function calling

### Issue 正文摘录

Does the Qwen3-Next model not support the function calling feature? Test results show some common error scenarios: 1. The tools should be called, but content returned something like the following: ``` { "choices": [ { "message": { "content": " \n{\"name\": \"send_email\", \"arguments\": {\"userInput\": \"ALAN的ID是123456，ALAN，中国人，英语数学很牛\"}}\n ", "tool_calls": [] }, "finish_reason": "stop" } ] } ``` ``` { "id": "chatcmpl-38af97847cce417a84577fe604d5b31e", "object": "chat.completion", "created": 1766119733, "model": "Next", "choices": [ { "index": 0, "message": { "role": "assistant", "content": " \n{\"name\": \"get_weather\", \"arguments\": {\"location\": \"San Francisco\", \"unit\": \"celsius\"}}\n ", "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning_content": null }, "logprobs": null, "finish_reason": "stop", "stop_reason": null, "token_ids": null } ], "service_tier": null, "system_fingerprint": null, "usage": { "prompt_tokens": 619, "total_tokens": 647, "completion_tokens": 28, "prompt_tokens_details": null }, "prompt_logprobs": null, "prompt_token_ids": null, "kv_transfer_params": null } ``` 2. Returning to the contents of the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen3-Next: Both Instruct and Thinking models don't support function calling usage;stale Does the Qwen3-Next model not support the function calling feature? Test results show some common error scenarios: 1. The...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tale Does the Qwen3-Next model not support the function calling feature? Test results show some common error scenarios: 1. The tools should be called, but content returned something like the following: ``` { "choices":...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: " \n{\"name\": \"get_weather\", \"arguments\": {\"location\": \"San Francisco\", \"unit\": \"celsius\"}}\n ", "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning_cont...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : Both Instruct and Thinking models don't support function calling usage;stale Does the Qwen3-Next model not support the function calling feature? Test results show some common error scenarios: 1. The tools should be ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
