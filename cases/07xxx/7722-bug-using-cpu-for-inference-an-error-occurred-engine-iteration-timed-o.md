# vllm-project/vllm#7722: [Bug]: Using CPU for inference, an error occurred. [Engine iteration timed out. This should never happen! ]

| 字段 | 值 |
| --- | --- |
| Issue | [#7722](https://github.com/vllm-project/vllm/issues/7722) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using CPU for inference, an error occurred. [Engine iteration timed out. This should never happen! ]

### Issue 正文摘录

### I compiled the vllm0.5.4 using the CPU, which does not support AVX512. After compiling, I entered the container and executed the command to start the llama3-8b model. ### 🐛 Describe the bug 3, 112471, 128001, 198, 72803, 5232], lora_request: None, prompt_adapter_request: None. INFO: 127.0.0.1:48252 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 08-21 07:31:22 async_llm_engine.py:174] Added request chat-0eefb9c0183b4a2197d1408cd47717ce. INFO 08-21 07:31:28 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 08-21 07:31:38 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 08-21 07:31:48 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 08-21 07:31:58 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ne 491, in _wait ERROR 08-21 07:32:22 async_llm_engine.py:57] await waiter ERROR 08-21 07:32:22 async_llm_engine.py:57] asyncio.exceptions.CancelledError ERROR 08-21 07:32:22 async_llm_engine.py:57] ERROR 08-21 07:32:22...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ngine iteration timed out. This should never happen! ] bug;stale ### I compiled the vllm0.5.4 using the CPU, which does not support AVX512. After compiling, I entered the container and executed the command to start the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: compiling, I entered the container and executed the command to start the llama3-8b model. ### 🐛 Describe the bug 3, 112471, 128001, 198, 72803, 5232], lora_request: None, prompt_adapter_request: None. INFO: 127.0.0.1:48...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r occurred. [Engine iteration timed out. This should never happen! ] bug;stale ### I compiled the vllm0.5.4 using the CPU, which does not support AVX512. After compiling, I entered the container and executed the command...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 08-21 07:31:38 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
