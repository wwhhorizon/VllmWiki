# vllm-project/vllm#2060: Can we avoid request.is_disconnected in api_server?

| 字段 | 值 |
| --- | --- |
| Issue | [#2060](https://github.com/vllm-project/vllm/issues/2060) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can we avoid request.is_disconnected in api_server?

### Issue 正文摘录

When using benchmark_serving without assigning request-rate (want to test the underlying degree of concurrency), the more num-prompts selected, the more likely following **ClientOSError: reset connection by peer** received from the client side. So is there any workaround to avoid the above overloaded situation, like defining try-except sentence instead of throwing out errors to keep the client side continue sending requests to the scheduler? And I also want to know the bottleneck is due to the FastAPI or vLLM itself?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Can we avoid request.is_disconnected in api_server? When using benchmark_serving without assigning request-rate (want to test the underlying degree of concurrency), the more num-prompts selected, the more likely followi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Can we avoid request.is_disconnected in api_server? When using benchmark_serving without assigning request-rate (want to test the underlying degree of concurrency), the more num-prompts selected, the more likely followi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
