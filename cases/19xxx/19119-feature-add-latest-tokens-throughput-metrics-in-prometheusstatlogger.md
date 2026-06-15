# vllm-project/vllm#19119: [Feature]: Add latest tokens throughput metrics in PrometheusStatLogger

| 字段 | 值 |
| --- | --- |
| Issue | [#19119](https://github.com/vllm-project/vllm/issues/19119) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add latest tokens throughput metrics in PrometheusStatLogger

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - We can easily determine our running vLLM system's token throughputs (prompt, generation) in log of vLLM process, via `LoggingStatLogger`. - I believe these metrics are key indicator of how vLLM engines are processing prompt and generation tasks in (almost) realtime. - These two metrics are missing in current ([main](https://github.com/vllm-project/vllm/blob/main/vllm/engine/metrics.py#L469) and [v0.9.0.1](https://github.com/vllm-project/vllm/blob/5fbbfe9a4c13094ad72ed3d6b4ef208a7ddc0fd7/vllm/engine/metrics.py#L538)) `PrometheusStatLogger` implementations; - which leads difficult to measure prompt TPS in server side, and - needs to measure client-side TPS computation for generation (maybe incorrect while tool calling in recent **Reasoning** models) ### Alternatives - **Add** prompt/generation tokens throughput metrics in `PrometheusStatLogger._log_prometheus()`, just like `LoggingStatLoger.log()` do, to expose tokens throughput in `/metrics` endpoint. ### Additional context - Currently, it's difficult to get *pure* prompt throughput in vLLM engine side. - When we measure TPS with tool calling in client-side, it's difficult or incorrect to g...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Add latest tokens throughput metrics in PrometheusStatLogger feature request ### 🚀 The feature, motivation and pitch - We can easily determine our running vLLM system's token throughputs (prompt, generation)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r generation (maybe incorrect while tool calling in recent **Reasoning** models) ### Alternatives - **Add** prompt/generation tokens throughput metrics in `PrometheusStatLogger._log_prometheus()`, just like `LoggingStat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Add latest tokens throughput metrics in PrometheusStatLogger feature request ### 🚀 The feature, motivation and pitch - We can easily determine our running vLLM system's token throughputs (prompt, generation) in log...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
