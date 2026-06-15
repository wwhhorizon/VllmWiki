# vllm-project/vllm#4052: [Usage]: How to do batch request on vLLM with OpenAI client

| 字段 | 值 |
| --- | --- |
| Issue | [#4052](https://github.com/vllm-project/vllm/issues/4052) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to do batch request on vLLM with OpenAI client

### Issue 正文摘录

### Your current environment I have been trying to perform the batching on the OpenAI client, which usage this api endpoint "http://localhost:8000/v1/completions", which allows to stream the tokens. ### How would you like to use vllm I want to perform a benchmark on how batch size impacts the TTFT and TPS. I have been trying to use the benchmark_serve.py script. Please share your suggestions and how should I approach this problem.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to do batch request on vLLM with OpenAI client usage;stale ### Your current environment I have been trying to perform the batching on the OpenAI client, which usage this api endpoint "http://localhost:8000/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: eam the tokens. ### How would you like to use vllm I want to perform a benchmark on how batch size impacts the TTFT and TPS. I have been trying to use the benchmark_serve.py script. Please share your suggestions and how...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
