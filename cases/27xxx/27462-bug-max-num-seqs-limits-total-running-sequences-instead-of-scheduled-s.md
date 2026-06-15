# vllm-project/vllm#27462: [Bug]: `--max-num-seqs` limits total running sequences instead of scheduled sequences, causing severe underutilization in PP

| 字段 | 值 |
| --- | --- |
| Issue | [#27462](https://github.com/vllm-project/vllm/issues/27462) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `--max-num-seqs` limits total running sequences instead of scheduled sequences, causing severe underutilization in PP

### Issue 正文摘录

### Your current environment I don't believe this information is necessary, as the `scheduler`'s code itself is clear enough to show the bug. ### 🐛 Describe the bug I have a question regarding the `--max-num-seqs` parameter and its behavior, particularly in Pipeline Parallelism (PP) scenarios. I don't know which template is more appropriate for this, so I am using the bug report template as I believe this might be a bug. Please feel free to reclassify it if necessary. ## Question on Definition The documentation describes `--max-num-seqs` as the "Maximum number of sequences per iteration." Does "iteration" here refer to a single call to `scheduler.schedule()`? If so, it seems that `max-num-seqs` should limit the number of sequences *scheduled within that single call* (i.e., the sum of `len(scheduled_new_reqs)`, `len(scheduled_resumed_reqs)`, and `len(scheduled_running_reqs)`). However, the current implementation appears to limit the total count of all currently running requests (i.e., `len(self.running)`). ## The Problem in Pipeline Parallelism (PP) This behavior is particularly problematic in PP scenarios. In PP, multiple micro-batches run concurrently. The `max-num-seqs` paramete...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: nstead of scheduled sequences, causing severe underutilization in PP bug;stale ### Your current environment I don't believe this information is necessary, as the `scheduler`'s code itself is clear enough to show the bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: that `max-num-seqs` is intended to serve two main purposes: (1) Balance latency and throughput: In an online setting, this prevents the system from waiting too long to form a large batch. (2) Limit memory usage: This pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -num-seqs` parameter and its behavior, particularly in Pipeline Parallelism (PP) scenarios. I don't know which template is more appropriate for this, so I am using the bug report template as I believe this might be a bu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r. Introduce a new parameter, such as `max-num-scheduled-seqs`, to explicitly limit the number of sequences scheduled per call. This parameter would be less than or equal to `max-num-seqs`. This is a more conservative a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: g too long to form a large batch. (2) Limit memory usage: This prevents OOM errors from too many concurrent requests. However, purpose (2) seems to be already well-covered by other parameters like `--max-num-batched-tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
