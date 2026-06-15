# vllm-project/vllm#24394: [Performance]: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact

| 字段 | 值 |
| --- | --- |
| Issue | [#24394](https://github.com/vllm-project/vllm/issues/24394) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact

### Issue 正文摘录

### Proposal to improve performance ## Optimization Proposal: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact ### Current Background Currently, vLLM uses prefix caching for matching. The earlier a request is processed, the higher its hit rate. Therefore, when evicting and releasing blocks, they are reversed before being added to the free list, implementing eviction from the tail to improve block reuse rate. However, between multiple adjacent requests, the overall block distribution is not reversed, preventing adjacent multiple requests from utilizing this characteristic. If reverse release between multiple requests can be achieved, it will undoubtedly improve the block hit rate. ### Difficult-to-Solve Dirty Cache Problem The current design, when encountering the release of an ultra-long request, causes the cached blocks of multiple adjacent requests ahead to be prioritized for eviction, which is a typical dirty cache problem. Implementing reverse release between multiple adjacent requests could significantly alleviate the dirty cache problem. ### Solution How can we leverage this characteristic during the release of multiple requests to improve overall cache hit rate a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact performance;stale ### Proposal to improve performance ## Optimization Proposal: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact ### Current Backgro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ptimize before**： **optimize after**: ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Performance]: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact performance;stale ### Proposal to improve performance ## Optimization Proposal: Improve Prefix Cache Hit Rate and Reduce Dirty Cache Impact ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Batch Release**: During release, first temporarily store them. When a specified quantity is reached or when available blocks are insufficient, then uniformly release these requests, thereby achieving reverse release bet...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: elease**: During release, first temporarily store them. When a specified quantity is reached or when available blocks are insufficient, then uniformly release these requests, thereby achieving reverse release between mu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
