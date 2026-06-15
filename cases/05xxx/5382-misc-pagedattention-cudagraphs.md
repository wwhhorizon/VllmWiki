# vllm-project/vllm#5382: [Misc]: PagedAttention + cudagraphs 

| 字段 | 值 |
| --- | --- |
| Issue | [#5382](https://github.com/vllm-project/vllm/issues/5382) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: PagedAttention + cudagraphs 

### Issue 正文摘录

### Anything you want to discuss about vllm. Please excuse the naive question, but was wondering how `PagedAttention` can be used with `Cuda Graphs` given that KV cache is dynamically allocated with `PagedAttention`?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Misc]: PagedAttention + cudagraphs ### Anything you want to discuss about vllm. Please excuse the naive question, but was wondering how `PagedAttention` can be used with `Cuda Graphs` given that KV cache is dynamically...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: wondering how `PagedAttention` can be used with `Cuda Graphs` given that KV cache is dynamically allocated with `PagedAttention`?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
