# vllm-project/vllm#9778: [Feature]: Image-Modality Throughput Benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#9778](https://github.com/vllm-project/vllm/issues/9778) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Image-Modality Throughput Benchmark

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is a subset of #8385. This issue is intended to track the effort of enabling throughput benchmark for image-modal models. This is a reasonably large feature, and will span the work among multiple PRs. ### Alternatives Ad-hoc scripts for each model. ### Additional context see #8385 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Image-Modality Throughput Benchmark feature request ### 🚀 The feature, motivation and pitch This is a subset of #8385. This issue is intended to track the effort of enabling throughput benchmark for image-mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 85 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ded to track the effort of enabling throughput benchmark for image-modal models. This is a reasonably large feature, and will span the work among multiple PRs. ### Alternatives Ad-hoc scripts for each model. ### Additio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Image-Modality Throughput Benchmark feature request ### 🚀 The feature, motivation and pitch This is a subset of #8385. This issue is intended to track the effort of enabling throughput benchmark for image-mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
