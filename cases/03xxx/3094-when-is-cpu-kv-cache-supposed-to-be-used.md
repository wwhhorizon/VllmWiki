# vllm-project/vllm#3094: When is cpu kv cache supposed to be used?

| 字段 | 值 |
| --- | --- |
| Issue | [#3094](https://github.com/vllm-project/vllm/issues/3094) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When is cpu kv cache supposed to be used?

### Issue 正文摘录

In my testing with many concurrent users, I see what appears to be changing of requests from `Running` to `Pending`. I've never seen `Running` change to `Swapped`, nor have I seen cpu kv cache at anything other than 0%. ``` INFO 02-28 21:48:18 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 44.9 tokens/s, Running: 2 reqs, Swapped: 0 reqs, Pending: 3 reqs, GPU KV cache usage: 82.1%, CPU KV cache usage: 0.0% ``` I have tried setting `swap_space` to a value equal to vram and that does not make a difference.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: When is cpu kv cache supposed to be used? In my testing with many concurrent users, I see what appears to be changing of requests from `Running` to `Pending`. I've never seen `Running` change to `Swapped`, nor have I se...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: When is cpu kv cache supposed to be used? In my testing with many concurrent users, I see what appears to be changing of requests from `Running` to `Pending`. I've never seen `Running` change to `Swapped`, nor have I se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: testing with many concurrent users, I see what appears to be changing of requests from `Running` to `Pending`. I've never seen `Running` change to `Swapped`, nor have I seen cpu kv cache at anything other than 0%. ``` I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
