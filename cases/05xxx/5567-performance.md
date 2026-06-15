# vllm-project/vllm#5567: [Performance]: 

| 字段 | 值 |
| --- | --- |
| Issue | [#5567](https://github.com/vllm-project/vllm/issues/5567) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: 

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance i dont konw when this happen when batch increasae generation throughput: didnot increase when I use VLLM batch 1 Avg generation throughput: 55.2 tokens/s batch 3 Avg generation throughput: 98.2 tokens/s, batch 5 Avg generation throughput: 134.4 tokens/s batch 30 Avg generation throughput: 249.2 tokens/s batch 256 Avg generation throughput: 1275.0 tokens/s ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance i dont konw when this happen when batch increasae generation throughput: didnot increase...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance i dont konw when this happen when batch increasae...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
