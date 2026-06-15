# vllm-project/vllm#6577: [Bug]: SpecDecode AsyncMetricsCollector _last_metrics_collect_time is never reset

| 字段 | 值 |
| --- | --- |
| Issue | [#6577](https://github.com/vllm-project/vllm/issues/6577) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: SpecDecode AsyncMetricsCollector _last_metrics_collect_time is never reset

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug I've been looking into how the speculative decoding metrics are behaving and I noticed that in the `AsyncMetricsCollector` class we set `_last_metrics_collect_time` once in the ctor: https://github.com/vllm-project/vllm/blob/62b8aebc6f06b5c8fafa1f27893cd4f9bb11fa8b/vllm/spec_decode/metrics.py#L75 ...and then never set it again. I see that this is causing the metrics to constantly get copied from GPU, presumably leading to some unnecessary performance overhead. Don't we need to reset that variable each time we collect?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: SpecDecode AsyncMetricsCollector _last_metrics_collect_time is never reset bug ### Your current environment n/a ### 🐛 Describe the bug I've been looking into how the speculative decoding metrics are behaving and...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
