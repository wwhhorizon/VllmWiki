# vllm-project/vllm#1658: benchmark_latency.py will hang  when --batchsize=1 and --n=2

| 字段 | 值 |
| --- | --- |
| Issue | [#1658](https://github.com/vllm-project/vllm/issues/1658) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> benchmark_latency.py will hang  when --batchsize=1 and --n=2

### Issue 正文摘录

benchmark_latency.py will hang if setting --batchsize=1 and --n=2or4or8. should max_num_seqs been set as args.batch_size * args.n ？ https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py#L23

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: benchmark_latency.py will hang when --batchsize=1 and --n=2 benchmark_latency.py will hang if setting --batchsize=1 and --n=2or4or8. should max_num_seqs been set as args.batch_size * args.n ？ https://github.com/vllm-pro

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
