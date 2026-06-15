# vllm-project/vllm#3395: Specify the max batch size with continous batching

| 字段 | 值 |
| --- | --- |
| Issue | [#3395](https://github.com/vllm-project/vllm/issues/3395) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Specify the max batch size with continous batching

### Issue 正文摘录

I want to process multiple inference requests and evaluate the the average request latency. Because increasing the batch size will add extra latency to the request, I want to find the optimal maximun batch size to minimize the average average request latency. So instead of letting vllm decide batch size at each iteration, is there a way to specify the max batch size (e.g., 40 requests inference at one iteration at most) with continous batching?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ith continous batching I want to process multiple inference requests and evaluate the the average request latency. Because increasing the batch size will add extra latency to the request, I want to find the optimal maxi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Specify the max batch size with continous batching I want to process multiple inference requests and evaluate the the average request latency. Because increasing the batch size will add extra latency to the request, I w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: batch size with continous batching I want to process multiple inference requests and evaluate the the average request latency. Because increasing the batch size will add extra latency to the request, I want to find the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
