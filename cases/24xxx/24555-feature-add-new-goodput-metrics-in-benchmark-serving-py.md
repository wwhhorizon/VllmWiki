# vllm-project/vllm#24555: [Feature]: Add New Goodput Metrics in benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#24555](https://github.com/vllm-project/vllm/issues/24555) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add New Goodput Metrics in benchmark_serving.py

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Suggested Content:** Currently, the output only includes **Request Goodput** (requests per second), which limits the ability to evaluate **Server-Level Objective (SLO)** performance on specific GPU systems. To enhance the granularity of performance analysis, we propose adding the following metrics: • **Output Good Throughput** – Measures the number of good tokens generated per second. • **Total Good Throughput** – Measures the total number of good tokens processed per second, regardless of request count. These additions would provide a more comprehensive view of system performance, especially for token-intensive workloads. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Feature]: Add New Goodput Metrics in benchmark_serving.py feature request;stale ### 🚀 The feature, motivation and pitch **Suggested Content:** Currently, the output only includes **Request Goodput** (requests per secon...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add New Goodput Metrics in benchmark_serving.py feature request;stale ### 🚀 The feature, motivation and pitch **Suggested Content:** Currently, the output only includes **Request Goodput** (requests per secon...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e ability to evaluate **Server-Level Objective (SLO)** performance on specific GPU systems. To enhance the granularity of performance analysis, we propose adding the following metrics: • **Output Good Throughput** – Mea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
