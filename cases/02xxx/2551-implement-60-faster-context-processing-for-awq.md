# vllm-project/vllm#2551: Implement 60% faster context processing for AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#2551](https://github.com/vllm-project/vllm/issues/2551) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Implement 60% faster context processing for AWQ

### Issue 正文摘录

After some experimentation, I found that dequantizing and running FP16 matmul is faster in cases where `batch_size * n_tokens >= 1024`. This should help with throughput. https://github.com/casper-hansen/AutoAWQ/pull/316

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ster context processing for AWQ After some experimentation, I found that dequantizing and running FP16 matmul is faster in cases where `batch_size * n_tokens >= 1024`. This should help with throughput. https://github.co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: er in cases where `batch_size * n_tokens >= 1024`. This should help with throughput. https://github.com/casper-hansen/AutoAWQ/pull/316

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
