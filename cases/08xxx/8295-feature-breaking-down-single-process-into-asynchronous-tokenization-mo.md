# vllm-project/vllm#8295: [Feature]: Breaking Down Single Process into Asynchronous Tokenization, Model Inference, and Detokenization for Enhanced GPU Utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#8295](https://github.com/vllm-project/vllm/issues/8295) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Breaking Down Single Process into Asynchronous Tokenization, Model Inference, and Detokenization for Enhanced GPU Utilization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Feature Proposal: I would like to request an optimization feature where tokenization, model inference, and detokenization are performed asynchronously in separate processes, leading to a significant improvement in GPU utilization. This setup would enable parallel execution of these tasks, minimizing idle GPU time between the phases of the pipeline and increasing overall throughput. Motivation: Currently, these three stages (tokenization, inference, detokenization) are typically handled sequentially, which results in underutilization of the GPU during the tokenization and detokenization phases. By separating these stages into asynchronous, tri-process collaboration, the GPU could be used more efficiently, especially for large models where tokenization and detokenization overhead becomes non-negligible. Pitch: Implementing this feature could greatly enhance the performance of vLLM for high-throughput applications, leading to faster inference times and better resource utilization. I believe this would be beneficial for any workload where latency and throughput are critical. ### Alternatives One alternative solution would be to look into other f...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: idle GPU time between the phases of the pipeline and increasing overall throughput. Motivation: Currently, these three stages (tokenization, inference, detokenization) are typically handled sequentially, which results i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: asynchronous, tri-process collaboration, the GPU could be used more efficiently, especially for large models where tokenization and detokenization overhead becomes non-negligible. Pitch: Implementing this feature could...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Breaking Down Single Process into Asynchronous Tokenization, Model Inference, and Detokenization for Enhanced GPU Utilization feature request ### 🚀 The feature, motivation and pitch Feature Proposal: I would...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Model Inference, and Detokenization for Enhanced GPU Utilization feature request ### 🚀 The feature, motivation and pitch Feature Proposal: I would like to request an optimization feature where tokenization, model infere...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
