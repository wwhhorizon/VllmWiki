# vllm-project/vllm#17454: [Feature]: We propose the official development and maintenance of a VLLM integration or plugin within Dify.

| 字段 | 值 |
| --- | --- |
| Issue | [#17454](https://github.com/vllm-project/vllm/issues/17454) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: We propose the official development and maintenance of a VLLM integration or plugin within Dify.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch VLLM is a popular, high-performance library for serving large language models, known for its state-of-the-art serving throughput via techniques like PagedAttention and continuous batching. Many Dify users who deploy their own self-hosted models could significantly benefit from using VLLM for efficient and scalable serving. Currently, users might rely on custom model configurations or potentially community-maintained solutions to connect Dify with VLLM instances. Official support would provide a more stable, reliable, and seamlessly integrated option for leveraging VLLM's capabilities within the Dify ecosystem. 1. Performance: VLLM offers superior inference performance and throughput compared to many other serving frameworks, especially under load. An official integration would allow Dify users to take full advantage of this. 2. Ease of Use: An officially supported plugin would simplify the process for users to connect Dify to their VLLM-served models, reducing the need for complex custom configurations. 3. Stability & Maintenance: Official support ensures the integration is maintained and updated alongside Dify and potentially VLLM developme...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: VLLM is a popular, high-performance library for serving large language models, known for its state-of-the-art serving throughput via techniques like PagedAttention and continuous batching. Many Dify users who deploy the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ent and maintenance of a VLLM integration or plugin within Dify. feature request;stale ### 🚀 The feature, motivation and pitch VLLM is a popular, high-performance library for serving large language models, known for its...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: or serving large language models, known for its state-of-the-art serving throughput via techniques like PagedAttention and continuous batching. Many Dify users who deploy their own self-hosted models could significantly...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: We propose the official development and maintenance of a VLLM integration or plugin within Dify. feature request;stale ### 🚀 The feature, motivation and pitch VLLM is a popular, high-performance library for s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PI. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
