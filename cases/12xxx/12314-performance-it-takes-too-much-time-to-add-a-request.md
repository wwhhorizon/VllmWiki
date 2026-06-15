# vllm-project/vllm#12314: [Performance]: It takes too much time to Add a request.

| 字段 | 值 |
| --- | --- |
| Issue | [#12314](https://github.com/vllm-project/vllm/issues/12314) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: It takes too much time to Add a request.

### Issue 正文摘录

### Proposal to improve performance the log likes: INFO 01-22 18:25:07 engine.py:267] Added request chatcmpl-b5a928b306044e3e882031ea6ec83d54. INFO 01-22 18:25:09 metrics.py:449] Avg prompt throughput: 605.5 tokens/s, Avg generation throughput: 61.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 7.4%, CPU KV cache usage: 0.0%. INFO 01-22 18:25:14 metrics.py:449] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 82.5 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 7.5%, CPU KV cache usage: 0.0%. INFO 01-22 18:25:19 metrics.py:449] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 81.2 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 7.6%, CPU KV cache usage: 0.0%. INFO 01-22 18:25:24 metrics.py:449] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 81.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 7.6%, CPU KV cache usage: 0.0%. INFO 01-22 18:25:29 metrics.py:449] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 81.3 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usa...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 06044e3e882031ea6ec83d54. INFO 01-22 18:25:09 metrics.py:449] Avg prompt throughput: 605.5 tokens/s, Avg generation throughput: 61.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 7.4%,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: It takes too much time to Add a request. performance;stale ### Proposal to improve performance the log likes: INFO 01-22 18:25:07 engine.py:267] Added request chatcmpl-b5a928b306044e3e882031ea6ec83d54. IN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t: 61.0 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 7.4%, CPU KV cache usage: 0.0%. INFO 01-22 18:25:14 metrics.py:449] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
