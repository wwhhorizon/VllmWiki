# vllm-project/vllm#45: Turn shareGPT data into a standard benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#45](https://github.com/vllm-project/vllm/issues/45) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Turn shareGPT data into a standard benchmark

### Issue 正文摘录

1. Extract out the lengths of the conversation rounds, and maybe have that data directly available from github. 2. The current L-shape evaluation with binary search for throughput is hard to run and not scalable. We should find an easier way to benchmark the performance.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Turn shareGPT data into a standard benchmark 1. Extract out the lengths of the conversation rounds, and maybe have that data directly available from github. 2. The current L-shape evaluation with binary search for throu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y available from github. 2. The current L-shape evaluation with binary search for throughput is hard to run and not scalable. We should find an easier way to benchmark the performance.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
