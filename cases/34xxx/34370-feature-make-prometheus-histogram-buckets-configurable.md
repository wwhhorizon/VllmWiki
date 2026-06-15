# vllm-project/vllm#34370: [Feature]: Make Prometheus histogram buckets configurable

| 字段 | 值 |
| --- | --- |
| Issue | [#34370](https://github.com/vllm-project/vllm/issues/34370) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make Prometheus histogram buckets configurable

### Issue 正文摘录

### Feature Request Allow configuring Prometheus histogram buckets for vLLM metrics (e.g., `vllm:e2e_request_latency_seconds`) via CLI flag or environment variable. --- ### 🎯 Motivation Currently, histogram buckets for metrics are statically defined in the source code. In production environments, especially in high-throughput and low-latency deployments, operators may require: - Finer granularity at sub-300ms ranges - Custom bucket distributions depending on workload profile - Alignment with existing SLO definitions - Consistent bucket definitions across services Without configurable buckets, users must patch and rebuild vLLM to adjust histogram resolution. --- ### Solution Introduce a way to configure histogram buckets via: - CLI flag - Environment variable - Or configuration file option ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: g Prometheus histogram buckets for vLLM metrics (e.g., `vllm:e2e_request_latency_seconds`) via CLI flag or environment variable. --- ### 🎯 Motivation Currently, histogram buckets for metrics are statically defined in th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: statically defined in the source code. In production environments, especially in high-throughput and low-latency deployments, operators may require: - Finer granularity at sub-300ms ranges - Custom bucket distributions...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Make Prometheus histogram buckets configurable feature request;stale ### Feature Request Allow configuring Prometheus histogram buckets for vLLM metrics (e.g., `vllm:e2e_request_latency_seconds`) via CLI flag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Make Prometheus histogram buckets configurable feature request;stale ### Feature Request Allow configuring Prometheus histogram buckets for vLLM metrics (e.g., `vllm:e2e_request_latency_seconds`) via CLI flag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
