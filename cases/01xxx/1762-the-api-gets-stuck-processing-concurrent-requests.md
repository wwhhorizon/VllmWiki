# vllm-project/vllm#1762: The API gets stuck (processing concurrent requests)

| 字段 | 值 |
| --- | --- |
| Issue | [#1762](https://github.com/vllm-project/vllm/issues/1762) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The API gets stuck (processing concurrent requests)

### Issue 正文摘录

Sometimes the API gets stuck after spamming it with concurrent requests. It proceeds processing the requests after waiting for +/- 1 minute. I'm using the OpenAI API and with streaming. In spite of the API having received many requests this is the latest update the terminal gives me: `INFO 11-23 19:12:45 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.4%, CPU KV cache usage: 0.0% ` As you can see, it records just 1 request and 0 pending. Might or might not be related to: https://github.com/vllm-project/vllm/issues/1712 https://github.com/vllm-project/vllm/issues/1707

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: The API gets stuck (processing concurrent requests) Sometimes the API gets stuck after spamming it with concurrent requests. It proceeds processing the requests after waiting for +/- 1 minute. I'm using the OpenAI API a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: eaming. In spite of the API having received many requests this is the latest update the terminal gives me: `INFO 11-23 19:12:45 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 toke...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.4%, CPU KV cache usage: 0.0% ` As you can see, it records just 1 request and 0 pending. Might or might not be related to: https:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
