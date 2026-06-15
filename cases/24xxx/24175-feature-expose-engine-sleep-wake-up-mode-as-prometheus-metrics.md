# vllm-project/vllm#24175: [Feature]: Expose Engine Sleep & Wake_up Mode as Prometheus Metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#24175](https://github.com/vllm-project/vllm/issues/24175) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose Engine Sleep & Wake_up Mode as Prometheus Metrics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the vLLM engine exposes several Prometheus-compatible metrics via the `/metrics` endpoint. These metrics includes a set of server-level metrics that track the state and performance of the LLM engine. But the currently available server-level metrics don't provide information of the sleep mode of an engine. This information is only available today by querying `/is_sleeping` endpoint which GETs the sleep status. Hence, any metrics collection application needs to query two different endpoints to get the full picture of the performance and state of the engine, and must guarantee a similar query interval for both endpoints. Therefore, we need to expose an engine `sleep` and `wake_up` state as prometheus metrics to provide a single endpoint to query all metrics related to state and performance of an engine. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: engine. But the currently available server-level metrics don't provide information of the sleep mode of an engine. This information is only available today by querying `/is_sleeping` endpoint which GETs the sleep status...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature]: Expose Engine Sleep & Wake_up Mode as Prometheus Metrics feature request ### 🚀 The feature, motivation and pitch Currently the vLLM engine exposes several Prometheus-compatible metrics via the `/metrics` endpoin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
