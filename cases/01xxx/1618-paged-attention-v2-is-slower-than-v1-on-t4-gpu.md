# vllm-project/vllm#1618: Paged attention v2 is slower than v1 on T4 GPU.

| 字段 | 值 |
| --- | --- |
| Issue | [#1618](https://github.com/vllm-project/vllm/issues/1618) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Paged attention v2 is slower than v1 on T4 GPU.

### Issue 正文摘录

Running python benchmarks/kernels/benchmark_paged_attention.py --verion v1 vs python benchmarks/kernels/benchmark_paged_attention.py --verion v2 v1 output: 1531.001us v2 output: 1875.677us And i tested real model scenarios that reflects that v2 is slower than v1 when batch size up to 4(16k ctx len). @WoosukKwon Could you have T4 gpu to test these?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: d attention v2 is slower than v1 on T4 GPU. performance Running python benchmarks/kernels/benchmark_paged_attention.py --verion v1 vs python benchmarks/kernels/benchmark_paged_attention.py --verion v2 v1 output: 1531.00...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: erion v2 v1 output: 1531.001us v2 output: 1875.677us And i tested real model scenarios that reflects that v2 is slower than v1 when batch size up to 4(16k ctx len). @WoosukKwon Could you have T4 gpu to test these?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
