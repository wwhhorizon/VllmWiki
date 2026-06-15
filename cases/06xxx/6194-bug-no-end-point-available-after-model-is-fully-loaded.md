# vllm-project/vllm#6194: [Bug]: No end point available after model is fully loaded

| 字段 | 值 |
| --- | --- |
| Issue | [#6194](https://github.com/vllm-project/vllm/issues/6194) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: No end point available after model is fully loaded

### Issue 正文摘录

### Your current environment ```text vllm==0.5.0.post1 vllm-flash-attn==2.5.9 Python 3.10.11 ``` ### 🐛 Describe the bug Hey Guys, I loaded a Llama-3-70B with vllm, once the model is loaded, I get the following message, which I assume means it is ready to take the requests, ``` INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) ``` However, no end point is available, I tried both / and /generate, both giving me 404 error, here is the log printed by vllm: ``` INFO: 127.0.0.1:55504 - "GET / HTTP/1.1" 404 Not Found INFO 07-07 20:12:44 metrics.py:295] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO: 127.0.0.1:59820 - "GET /generate HTTP/1.1" 404 Not Found INFO 07-07 20:12:54 metrics.py:295] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO: 127.0.0.1:53798 - "POST /generate HTTP/1.1" 404 Not Found ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: No end point available after model is fully loaded bug ### Your current environment ```text vllm==0.5.0.post1 vllm-flash-attn==2.5.9 Python 3.10.11 ``` ### 🐛 Describe the bug Hey Guys, I loaded a Llama-3-70B with...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO: 127.0.0.1:59820 - "GET /generate HTTP/1.1" 404 Not Found INFO 07-07 20:12:54 metrics.py:295]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: get the following message, which I assume means it is ready to take the requests, ``` INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) ``` However, no end point is available, I tried both / and /gener...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: / HTTP/1.1" 404 Not Found INFO 07-07 20:12:44 metrics.py:295] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
