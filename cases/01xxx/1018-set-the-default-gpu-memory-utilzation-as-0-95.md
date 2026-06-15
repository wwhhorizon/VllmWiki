# vllm-project/vllm#1018: Set the default `gpu-memory-utilzation` as 0.95

| 字段 | 值 |
| --- | --- |
| Issue | [#1018](https://github.com/vllm-project/vllm/issues/1018) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Set the default `gpu-memory-utilzation` as 0.95

### Issue 正文摘录

The `gpu-memory-utilization` argument was originally set to 0.95 by default but changed to 0.9, mainly because the memory profiling at the initialization time can be inaccurate. However, oftentimes the wasted 5% of GPU memory considerably affects the performance; For 13B LLMs, this leads to 20% difference (10GB vs. 12GB) in the KV cache size. For the best performance, we should make the memory profiling more accurate and set `gpu-memory-utilization` back to 0.95.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: tialization time can be inaccurate. However, oftentimes the wasted 5% of GPU memory considerably affects the performance; For 13B LLMs, this leads to 20% difference (10GB vs. 12GB) in the KV cache size. For the best per...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lly set to 0.95 by default but changed to 0.9, mainly because the memory profiling at the initialization time can be inaccurate. However, oftentimes the wasted 5% of GPU memory considerably affects the performance; For...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
