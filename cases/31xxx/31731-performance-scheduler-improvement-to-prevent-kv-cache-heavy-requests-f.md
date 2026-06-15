# vllm-project/vllm#31731: [Performance]: scheduler improvement to prevent KV-cache heavy requests from blocking others

| 字段 | 值 |
| --- | --- |
| Issue | [#31731](https://github.com/vllm-project/vllm/issues/31731) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: scheduler improvement to prevent KV-cache heavy requests from blocking others

### Issue 正文摘录

### Proposal to improve performance Dear vLLM community members and scheduler.py contributors (@woosuk, @KuntaiDu, @zhuohan123, @hmellor), This PR opens a discussion about a minimal scheduling-policy adjustment to improve resources utilization and efficiency. ### Motivation The current v1 scheduler can let a single “KV-cache hungry” request reduce hardware utilization and effiency by preventing other eligible work from running in a decoding step. ### Problem Current scheduler policy preempt all subsequent running requests and skip waiting requests for a decoding step in case of appearance a kv-cache heavy request. The net effect is head-of-line blocking: one request that can’t grow its KV footprint can stall progress for other requests that could have run, causing resource underutilization. ### Current behavior (high-level) For each decoding step, the scheduler roughly follows: 1. [Iterate](https://github.com/vllm-project/vllm/blob/d5503ca7f93ee756604c8dac0adeec9526c40802/vllm/v1/core/sched/scheduler.py#L259C13-L259C46) RUNNING requests. 2. For each request, [try to allocate KV slots](https://github.com/vllm-project/vllm/blob/d5503ca7f93ee756604c8dac0adeec9526c40802/vllm/v1/core/s...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: mpact - Better hardware-utilization during KV-cache contention. - Higher throughput and reduced latency where one request has large KV growth. - Reduced unnecessary preemption ### Next steps If the direction sounds good...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: scheduler improvement to prevent KV-cache heavy requests from blocking others performance;stale ### Proposal to improve performance Dear vLLM community members and scheduler.py contributors (@woosuk, @Kun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : token budget, max running, KV cache correctness, and preemption mechanisms remain unchanged – only the control flow around a failed allocation is adjusted. ### Expected impact - Better hardware-utilization during KV-c...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: scheduler improvement to prevent KV-cache heavy requests from blocking others performance;stale ### Proposal to improve performance Dear vLLM community members and scheduler.py contributors (@woosuk, @Kun...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: formance]: scheduler improvement to prevent KV-cache heavy requests from blocking others performance;stale ### Proposal to improve performance Dear vLLM community members and scheduler.py contributors (@woosuk, @KuntaiD...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
