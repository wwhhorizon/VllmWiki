# vllm-project/vllm#14044: [Feature]: Speculative decoding and Pipeline Paralelism

| 字段 | 值 |
| --- | --- |
| Issue | [#14044](https://github.com/vllm-project/vllm/issues/14044) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Speculative decoding and Pipeline Paralelism

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, Deepseek cannot be deployed with TP=32 because the block_size cannot be evenly divided by 32. In the case of 32 GPUs with 48GB memory each, it's necessary to enable PP (Pipeline Parallelism) for full parameter v3 deployment. However, once PP is enabled, speculative decoding is no longer supported. ![Image](https://github.com/user-attachments/assets/63b70635-9577-4f38-9e8b-10af2474b335) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Speculative decoding and Pipeline Paralelism feature request;stale ### 🚀 The feature, motivation and pitch Currently, Deepseek cannot be deployed with TP=32 because the block_size cannot be evenly divided by...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Speculative decoding and Pipeline Paralelism feature request;stale ### 🚀 The feature, motivation and pitch Currently, Deepseek cannot be deployed with TP=32 because the block_size cannot be evenly divided by...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: and pitch Currently, Deepseek cannot be deployed with TP=32 because the block_size cannot be evenly divided by 32. In the case of 32 GPUs with 48GB memory each, it's necessary to enable PP (Pipeline Parallelism) for ful...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
