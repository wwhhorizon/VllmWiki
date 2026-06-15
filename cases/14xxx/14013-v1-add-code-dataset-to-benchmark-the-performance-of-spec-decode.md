# vllm-project/vllm#14013: [V1] Add code dataset to benchmark the performance of spec decode

| 字段 | 值 |
| --- | --- |
| Issue | [#14013](https://github.com/vllm-project/vllm/issues/14013) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1] Add code dataset to benchmark the performance of spec decode

### Issue 正文摘录

Current we don't have a code-related dataset in the benchmark. It will be nice to have a code editing dataset to demonstrate the major use case and benefits of ngram speculative decoding.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [V1] Add code dataset to benchmark the performance of spec decode feature request Current we don't have a code-related dataset in the benchmark. It will be nice to have a code editing dataset to demonstrate the major us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [V1] Add code dataset to benchmark the performance of spec decode feature request Current we don't have a code-related dataset in the benchmark. It will be nice to have a code editing dataset to demonstrate the major us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
