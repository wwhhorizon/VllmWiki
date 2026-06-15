# vllm-project/vllm#21596: [Usage]: How do you use benchmark_serving on VLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#21596](https://github.com/vllm-project/vllm/issues/21596) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How do you use benchmark_serving on VLM?

### Issue 正文摘录

I used random datasets on LLM to test the performance, but VLM requires images or videos as input and I can no longer use random datasets. I was wondering what is a good way to test the performance of VLM. Do you recommend using real datasets? If so, which one is better?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: How do you use benchmark_serving on VLM? usage;stale I used random datasets on LLM to test the performance, but VLM requires images or videos as input and I can no longer use random datasets. I was wondering wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How do you use benchmark_serving on VLM? usage;stale I used random datasets on LLM to test the performance, but VLM requires images or videos as input and I can no longer use random datasets. I was wondering wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How do you use benchmark_serving on VLM? usage;stale I used random datasets on LLM to test the performance, but VLM requires images or videos as input and I can no longer use random datasets. I was wondering wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
