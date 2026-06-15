# vllm-project/vllm#1734: vlllm stops generation when pending request > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#1734](https://github.com/vllm-project/vllm/issues/1734) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vlllm stops generation when pending request > 0

### Issue 正文摘录

It seems that under the AWQ , each input temporarily halts VLLM operations for a few seconds, either the generation throughput drops to zero or the prompt throughput does, indicating that the system is not simultaneously processing the prompt and generating output. In an instance with 10 requests, each containing approximately 500 prompt tokens, the system takes around 20 seconds to process the prompt before starting any generation. Even after it processed all pending requests, If a new request arrives during this time, it interrupts the ongoing generation process to handle the new prompt. ``` 11-21 00:12:08 llm_engine.py:624] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 122.2 tokens/s, Running: 20 reqs, Swapped: 0 reqs, Pending: 9 reqs, GPU KV cache usage: 24.8%, CPU KV cache usage: 0.0% INFO 11-21 00:12:13 llm_engine.py:624] Avg prompt throughput: 1032.4 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 22 reqs, Swapped: 0 reqs, Pending: 7 reqs, GPU KV cache usage: 27.1%, CPU KV cache usage: 0.0% INFO 11-21 00:12:18 llm_engine.py:624] Avg prompt throughput: 1096.2 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 24 reqs, Swapped: 0 reqs, P...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vlllm stops generation when pending request > 0 stale It seems that under the AWQ , each input temporarily halts VLLM operations for a few seconds, either the generation throughput drops to zero or the prompt throughput...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 122.2 tokens/s, Running: 20 reqs, Swapped: 0 reqs, Pending: 9 reqs, GPU KV cache usage: 24.8%, CPU KV cache usage: 0.0% INFO 11-21 00:12:13 llm_engine.py:624] Avg prompt throughput: 1032.4 tokens/s, Avg generation throu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: mporarily halts VLLM operations for a few seconds, either the generation throughput drops to zero or the prompt throughput does, indicating that the system is not simultaneously processing the prompt and generating outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
