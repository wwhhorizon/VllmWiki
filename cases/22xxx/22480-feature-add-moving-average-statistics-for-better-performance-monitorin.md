# vllm-project/vllm#22480: [Feature]: Add Moving Average Statistics for Better Performance Monitoring

| 字段 | 值 |
| --- | --- |
| Issue | [#22480](https://github.com/vllm-project/vllm/issues/22480) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Moving Average Statistics for Better Performance Monitoring

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM's Prometheus metrics, such as **IterationStats** and **RequestStateStats**, provide real-time or event-based data. While useful for immediate monitoring, it is challenging to get a clear, stable view of the long-term or recent average performance of the vLLM server without implementing an external data processing and aggregation layer. ### **WHY:** **IterationStats**: Emitted per scheduling step (not per request), too frequent for request-level tracking **RequestStateStats**: Only captures request start events, lacks completion data **FinishedRequestStats**: Records completed requests but doesn't maintain historical aggregates **LoRAStats**: Unrelated to performance tracking (handles Low-Rank Adaptation metrics) ### Gap: No sliding-window aggregation for request performance metrics exists For example, a user wants to monitor the average latency or throughput of the last 100 finished requests to understand the server's typical performance, rather than just the real-time fluctuations of each iteration or individual request. Existing metrics are not designed to provide this kind of rolling average. I propose adding a new metrics...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: y, vLLM's Prometheus metrics, such as **IterationStats** and **RequestStateStats**, provide real-time or event-based data. While useful for immediate monitoring, it is challenging to get a clear, stable view of the long...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Add Moving Average Statistics for Better Performance Monitoring feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM's Prometheus metrics, such as **IterationStats** and **RequestStateStats**, p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d allow users to directly monitor the server's performance trends with a smoother, more representative metric. This new class could track metrics such as: **Average Latency:** The average time from request start to fini...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rst token is generated for the last N requests. The value of N could be configurable to allow users to adjust the window size for the moving average. ### Suggested Solution Implement a sliding-window metric tracker that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ime-series model lacking request ordering guarantees Absence of stateful circular buffer semantics Inability to evict specific old data points when new ones arrive ### Additional context This feature would significantly...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
