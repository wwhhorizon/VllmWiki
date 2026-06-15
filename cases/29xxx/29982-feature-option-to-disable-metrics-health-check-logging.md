# vllm-project/vllm#29982: [Feature]: Option to Disable Metrics Health-Check Logging

| 字段 | 值 |
| --- | --- |
| Issue | [#29982](https://github.com/vllm-project/vllm/issues/29982) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Option to Disable Metrics Health-Check Logging

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary Add a configuration option in vLLM to disable logging for metrics health-check endpoints. ### Motivation In production environments, frequent metrics health-check requests generate repetitive log lines that do not provide actionable value. This results in: - Log clutter that makes it harder to identify real issues - Increased log storage footprint and associated operational cost - Higher noise-to-signal ratio when analyzing logs ### Proposed Solution Introduce a flag or configuration setting (e.g., --disable-metrics-healthcheck-logging or similar) that suppresses logs specifically for /health endpoints while keeping all other logging intact. ### Expected Benefits - Significant reduction in log volume in production - Cleaner and more meaningful logs - Lower storage and ingestion costs for centralized logging systems - Improved user experience when debugging issues ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: harder to identify real issues - Increased log storage footprint and associated operational cost - Higher noise-to-signal ratio when analyzing logs ### Proposed Solution Introduce a flag or configuration setting (e.g.,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ature request ### 🚀 The feature, motivation and pitch ### Summary Add a configuration option in vLLM to disable logging for metrics health-check endpoints. ### Motivation In production environments, frequent metrics hea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Option to Disable Metrics Health-Check Logging feature request ### 🚀 The feature, motivation and pitch ### Summary Add a configuration option in vLLM to disable logging for metrics health-check endpoints. ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
