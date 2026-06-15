# vllm-project/vllm#16014: [Bug]: Null response for Mistral3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#16014](https://github.com/vllm-project/vllm/issues/16014) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Null response for Mistral3.1

### Issue 正文摘录

### Your current environment vllm version `0.8.1` ### 🐛 Describe the bug serving Mistral3.1 on A100, and I have null response as the following, what could be the issue here? - command ``` VLLM_USE_V1=0 vllm serve mistralai/Mistral-Small-3.1-24B-Base-2503 --tensor-parallel-size 1 --max-model-len 32000 --gpu-memory-utilization 0.90 --distributed-executor-backend mp --served-model-name mistral --tokenizer-mode mistral --config-format mistral --load_format mistral ``` - response ``` { "id": "chatcmpl-string", "object": "chat.completion", "created": 1743686242, "model": "mistral", "choices": [ { "index": 0, "message": { "role": "assistant", "reasoning_content": null, "content": "", "tool_calls": [] }, "logprobs": null, "finish_reason": "stop", "stop_reason": null } ], "usage": { "prompt_tokens": 1011, "total_tokens": 1012, "completion_tokens": 1, "prompt_tokens_details": null }, "prompt_logprobs": null } ``` - request ``` { "model": "mistral", "messages": [ { "role": "user", "content": "summarize the following story:\n\"My aunt will be down presently, Mr. Nuttel,\" said a very self-possessed young lady of fifteen; \"in the meantime you must try and put up with me.\"\n\nFramton Nuttel e...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ent vllm version `0.8.1` ### 🐛 Describe the bug serving Mistral3.1 on A100, and I have null response as the following, what could be the issue here? - command ``` VLLM_USE_V1=0 vllm serve mistralai/Mistral-Small-3.1-24B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stralai/Mistral-Small-3.1-24B-Base-2503 --tensor-parallel-size 1 --max-model-len 32000 --gpu-memory-utilization 0.90 --distributed-executor-backend mp --served-model-name mistral --tokenizer-mode mistral --config-format...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ull response for Mistral3.1 bug;stale ### Your current environment vllm version `0.8.1` ### 🐛 Describe the bug serving Mistral3.1 on A100, and I have null response as the following, what could be the issue here? - comma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Null response for Mistral3.1 bug;stale ### Your current environment vllm version `0.8.1` ### 🐛 Describe the bug serving Mistral3.1 on A100, and I have null response as the following, what could be the issue here?...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: x-model-len 32000 --gpu-memory-utilization 0.90 --distributed-executor-backend mp --served-model-name mistral --tokenizer-mode mistral --config-format mistral --load_format mistral ``` - response ``` { "id": "chatcmpl-s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
