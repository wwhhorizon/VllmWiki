# vllm-project/vllm#32658: [Feature]: batch invariance for A100

| 字段 | 值 |
| --- | --- |
| Issue | [#32658](https://github.com/vllm-project/vllm/issues/32658) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: batch invariance for A100

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/features/batch_invariance/#motivation Batch invariance currently requires NVIDIA GPUs with compute capability 9.0 or higher: H-series: H100, H200 B-series: B100, B200 Is there any plan to support batch invariance for A100? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Feature]: batch invariance for A100 feature request ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/features/batch_invariance/#motivation Batch invariance currently requires NVIDIA GPUs with comp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Feature]: batch invariance for A100 feature request ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/features/batch_invariance/#motivation Batch invariance currently requires NVIDIA GPUs with comp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: batch invariance for A100 feature request ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/features/batch_invariance/#motivation Batch invariance currently requires NVIDIA GPUs with comp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: quest ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/features/batch_invariance/#motivation Batch invariance currently requires NVIDIA GPUs with compute capability 9.0 or higher: H-series: H100, H...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
