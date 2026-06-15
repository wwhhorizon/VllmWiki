# vllm-project/vllm#481: when will cpu kv cache block be used?

| 字段 | 值 |
| --- | --- |
| Issue | [#481](https://github.com/vllm-project/vllm/issues/481) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> when will cpu kv cache block be used?

### Issue 正文摘录

I ran the benchmark scripts and found that the cpu block usage is always 0%, I wonder in what workload will the cpu block been used?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: when will cpu kv cache block be used? I ran the benchmark scripts and found that the cpu block usage is always 0%, I wonder in what workload will the cpu block been used?
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: when will cpu kv cache block be used? I ran the benchmark scripts and found that the cpu block usage is always 0%, I wonder in what workload will the cpu block been used?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: when will cpu kv cache block be used? I ran the benchmark scripts and found that the cpu block usage is always 0%, I wonder in what workload will the cpu block been used?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
