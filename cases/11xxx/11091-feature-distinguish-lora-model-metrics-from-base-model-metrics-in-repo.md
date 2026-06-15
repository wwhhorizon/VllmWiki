# vllm-project/vllm#11091: [Feature]: Distinguish LoRA Model Metrics from Base Model Metrics in Reporting

| 字段 | 值 |
| --- | --- |
| Issue | [#11091](https://github.com/vllm-project/vllm/issues/11091) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Distinguish LoRA Model Metrics from Base Model Metrics in Reporting

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When submitting requests to a LoRA model and subsequently checking the associated metrics, I've noticed that all metrics are aggregated under the base model's metrics. This means that requests made to the LoRA model are being counted as requests to the base model. Given that LoRA models logically represent a distinct model layer on top of the base, it is crucial for accurate monitoring and analysis that we separate these metrics. part of https://github.com/vllm-project/vllm/issues/6275 ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "sql-lora", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": 0 }' ``` ![image](https://github.com/user-attachments/assets/cf7706d3-e4f2-4f92-985b-517a90b1e3c6) ### Expected Behavior Metrics for LoRA models should be distinctly reported, separate from the base model metrics, to accurately reflect their usage and performance. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tinguish LoRA Model Metrics from Base Model Metrics in Reporting feature request;stale ### 🚀 The feature, motivation and pitch When submitting requests to a LoRA model and subsequently checking the associated metrics, I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: en submitting requests to a LoRA model and subsequently checking the associated metrics, I've noticed that all metrics are aggregated under the base model's metrics. This means that requests made to the LoRA model are b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Distinguish LoRA Model Metrics from Base Model Metrics in Reporting feature request;stale ### 🚀 The feature, motivation and pitch When submitting requests to a LoRA model and subsequently checking the associa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
