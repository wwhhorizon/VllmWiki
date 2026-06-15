# vllm-project/vllm#20962: [RFC][FEATURE]: TTFT Routing

| 字段 | 值 |
| --- | --- |
| Issue | [#20962](https://github.com/vllm-project/vllm/issues/20962) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][FEATURE]: TTFT Routing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Motivation The current PrefixAwareRouter and KvawareRouter (in production-stack) route user request purely base of the length the cached prefix. However, it may not be optimal due to the selected instance may have a long pending request queue. A more efficient way is estimating TTFT of the incoming request for each instance, select the one with the least estimated TTFT. ### TTFT Estimation ttft = queue_time + cache_transfer_time + (num_uncached_blk * blk_compute_time) **queue_time:** estimated time of the instance finish all the pending requests **cache_transfer_time:** estimated time of transferring matched block cache from other instances to the subject instance, by the number of cached remote block and it's size & device type **num_uncached_blk:** number of blocks that is not uncached in the prompt **blk_compute_time:** estimated time of the instance process each block for inferencing @youkaichao @DarkLight1337 is that estimation reasonable ? ### TODO **vllm:** Add http API for retrieving the queue_time and blk_compute_time, an internal profiler may be added for these 2 estimations **production-stack:** Add TtftRouter **lmcache:** Add...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC][FEATURE]: TTFT Routing feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation The current PrefixAwareRouter and KvawareRouter (in production-stack) route user request purely base of the lengt...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC][FEATURE]: TTFT Routing feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation The current PrefixAwareRouter and KvawareRouter (in production-stack) route user request purely base of the lengt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: http API for retrieving the queue_time and blk_compute_time, an internal profiler may be added for these 2 estimations **production-stack:** Add TtftRouter **lmcache:** Add API for retrieving matched cache info of all i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC][FEATURE]: TTFT Routing feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation The current PrefixAwareRouter and KvawareRouter (in production-stack) route user request purely base of the lengt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the selected instance may have a long pending request queue. A more efficient way is estimating TTFT of the incoming request for each instance, select the one with the least estimated TTFT. ### TTFT Estimation ttft = qu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
