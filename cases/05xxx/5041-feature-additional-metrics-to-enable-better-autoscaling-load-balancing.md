# vllm-project/vllm#5041: [Feature]: Additional metrics to enable better autoscaling / load balancing of vLLM servers in Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#5041](https://github.com/vllm-project/vllm/issues/5041) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Additional metrics to enable better autoscaling / load balancing of vLLM servers in Kubernetes

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM provides some metrics on model performance and load today which are very useful. There are a few metrics that are missing today which if added can make it easier for any orchestrators like Kubernetes to provide better support for autoscaling vLLM servers or distribute load between multiple vLLM servers more efficiently. We have a proposal in the Kubernetes Serving WG to add these additional metrics to popular model servers. We want to add these to vLLM as well. Google doc link to the proposal which has the set of metrics we want to add and the reasoning behind it - https://docs.google.com/document/d/1SpSp1E6moa4HSrJnS4x3NpLuj88sMXr2tbofKlzTZpk/edit?usp=sharing&resourcekey=0-ob5dR-AJxLQ5SvPlA4rdsg. (Please request access if you are not able to view it) Listing the metrics that we've identified to include in vLLM: Metric Name | Type | Unit -- | -- | -- model_load_time | Counter | Seconds time_per_output_token_per_batch_size | Histogram | Milliseconds request_wait_time (total time - time spent on inference) | Histogram | Milliseconds request_queue_time | Histogram | Milliseconds max_token_capacity | Counter | Tokens time_per_prefill_token...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: etter autoscaling / load balancing of vLLM servers in Kubernetes feature request;stale ### 🚀 The feature, motivation and pitch vLLM provides some metrics on model performance and load today which are very useful. There...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Additional metrics to enable better autoscaling / load balancing of vLLM servers in Kubernetes feature request;stale ### 🚀 The feature, motivation and pitch vLLM provides some metrics on model performance and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hind it - https://docs.google.com/document/d/1SpSp1E6moa4HSrJnS4x3NpLuj88sMXr2tbofKlzTZpk/edit?usp=sharing&resourcekey=0-ob5dR-AJxLQ5SvPlA4rdsg. (Please request access if you are not able to view it) Listing the metrics...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e ### 🚀 The feature, motivation and pitch vLLM provides some metrics on model performance and load today which are very useful. There are a few metrics that are missing today which if added can make it easier for any or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
