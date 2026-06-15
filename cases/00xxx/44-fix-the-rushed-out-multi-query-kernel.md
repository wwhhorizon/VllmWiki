# vllm-project/vllm#44: Fix the rushed out multi-query kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#44](https://github.com/vllm-project/vllm/issues/44) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Fix the rushed out multi-query kernel

### Issue 正文摘录

1. Fix the correctness issue in the current FlashAttention-copy-based kernel. Make sure we call the FlashAttention kernel correctly. Evaluate the performance of this kernel. 2. Reduce the memory usage of the current kernel by limiting the buffer size and calling the kernel multiple times.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ushed out multi-query kernel 1. Fix the correctness issue in the current FlashAttention-copy-based kernel. Make sure we call the FlashAttention kernel correctly. Evaluate the performance of this kernel. 2. Reduce the me...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: opy-based kernel. Make sure we call the FlashAttention kernel correctly. Evaluate the performance of this kernel. 2. Reduce the memory usage of the current kernel by limiting the buffer size and calling the kernel multi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
