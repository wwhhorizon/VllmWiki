# vllm-project/vllm#435: Why do not you calculate the real output token for throughput?

| 字段 | 值 |
| --- | --- |
| Issue | [#435](https://github.com/vllm-project/vllm/issues/435) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why do not you calculate the real output token for throughput?

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/c894836108732d0cbb6fce15aeda8de1218a380d/benchmarks/benchmark_throughput.py#L177-L180 You can see that you just use the tokens' length of request in the dataset , not the real output length for the model to eval.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Why do not you calculate the real output token for throughput? https://github.com/vllm-project/vllm/blob/c894836108732d0cbb6fce15aeda8de1218a380d/benchmarks/benchmark_throughput.py#L177-L180 You can see that you just us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s' length of request in the dataset , not the real output length for the model to eval.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ughput.py#L177-L180 You can see that you just use the tokens' length of request in the dataset , not the real output length for the model to eval.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
