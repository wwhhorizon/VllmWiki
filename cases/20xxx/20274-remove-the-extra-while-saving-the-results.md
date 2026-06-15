# vllm-project/vllm#20274: remove the extra ":" while saving the results

| 字段 | 值 |
| --- | --- |
| Issue | [#20274](https://github.com/vllm-project/vllm/issues/20274) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> remove the extra ":" while saving the results

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/3015d5634e74d59704e2b39bab0dbe2e6f86a38a/benchmarks/benchmark_serving.py#L426 Please remove the extra ":" from `"request_goodput:":`, so that we can keep the post processing script simple :)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: benchmarks/benchmark_serving.py#L426 Please remove the extra ":" from `"request_goodput:":`, so that we can keep the post processing script simple :)
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: thub.com/vllm-project/vllm/blob/3015d5634e74d59704e2b39bab0dbe2e6f86a38a/benchmarks/benchmark_serving.py#L426 Please remove the extra ":" from `"request_goodput:":`, so that we can keep the post processing script simple...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
