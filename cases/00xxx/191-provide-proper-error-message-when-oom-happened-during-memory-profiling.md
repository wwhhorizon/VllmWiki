# vllm-project/vllm#191: Provide proper error message when OOM happened during memory profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#191](https://github.com/vllm-project/vllm/issues/191) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Provide proper error message when OOM happened during memory profiling

### Issue 正文摘录

To prevent the confusion in #184

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Provide proper error message when OOM happened during memory profiling bug To prevent the confusion in #184
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Provide proper error message when OOM happened during memory profiling bug To prevent the confusion in #184

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
