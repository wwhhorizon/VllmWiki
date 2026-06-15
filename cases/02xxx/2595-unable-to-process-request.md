# vllm-project/vllm#2595: Unable to process request 

| 字段 | 值 |
| --- | --- |
| Issue | [#2595](https://github.com/vllm-project/vllm/issues/2595) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unable to process request 

### Issue 正文摘录

I am getting this on terminal _AsyncLLMEngine pid=1974) INFO 01-25 11:26:53 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% (_AsyncLLMEngine pid=1974) INFO 01-25 11:26:58 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 77.3 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0% (_AsyncLLMEngine pid=1974) INFO 01-25 11:27:03 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 77.3 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.3%, CPU KV cache usage: 0.0% (_AsyncLLMEngine pid=1974) INFO 01-25 11:27:08 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 76.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.4%, CPU KV cache usage: 0.0% (_AsyncLLMEngine pid=1974) INFO 01-25 11:27:13 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 76.4 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pend...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% (_AsyncLLMEngine pid=1974) INFO 01-25 11:26:58 llm_engine.py:706] Avg prompt throughput: 0.0 tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Unable to process request I am getting this on terminal _AsyncLLMEngine pid=1974) INFO 01-25 11:26:53 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: yncLLMEngine pid=1974) INFO 01-25 11:26:53 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
