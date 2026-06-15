# vllm-project/vllm#27074: [Bug]: infinite empty scheduling when load kv async from external KV Cache with KVConnector

| 字段 | 值 |
| --- | --- |
| Issue | [#27074](https://github.com/vllm-project/vllm/issues/27074) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: infinite empty scheduling when load kv async from external KV Cache with KVConnector

### Issue 正文摘录

### Your current environment vllm 0.9.0 with NPU 910C ### 🐛 Describe the bug We are testing prefix cache reusing with external distributed cache storage. The system is deployed as PD Disaggregated. On the P side, the matched kv is loaded async from external caching. Our testing case is that every request prompt size is 4096, and the first 2048 tokens matched with external caching. The issue happens when the matched kv were loaded async to HBM and there is no enough space for new tokens of any request to schedule. Then infinite empty scheduling forever. Two possible ways to fix this issue: 1. At first, set the request loaded kv from remote to running status and add it to running queue. Then process the running request which contains preempt operations. 2. Before adding the request to kv async loading queue, also consider if there is enough space for new tokens after the kv loaded.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cheduling when load kv async from external KV Cache with KVConnector bug;stale ### Your current environment vllm 0.9.0 with NPU 910C ### 🐛 Describe the bug We are testing prefix cache reusing with external distributed c...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: infinite empty scheduling when load kv async from external KV Cache with KVConnector bug;stale ### Your current environment vllm 0.9.0 with NPU 910C ### 🐛 Describe the bug We are testing prefix cache reusing with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nt environment vllm 0.9.0 with NPU 910C ### 🐛 Describe the bug We are testing prefix cache reusing with external distributed cache storage. The system is deployed as PD Disaggregated. On the P side, the matched kv is lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
