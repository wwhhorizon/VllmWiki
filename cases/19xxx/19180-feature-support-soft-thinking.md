# vllm-project/vllm#19180: [Feature]: support soft thinking

| 字段 | 值 |
| --- | --- |
| Issue | [#19180](https://github.com/vllm-project/vllm/issues/19180) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support soft thinking

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Motivation https://github.com/eric-ai-lab/Soft-Thinking/tree/main/sglang_soft_thinking_pkg/python/sglang Microsoft introduce "Soft Thinking," a training-free method enabling LLMs to reason using continuous concept representations rather than discrete tokens, achieving improved accuracy on mathematical and coding tasks while reducing token usage by up to 22.4% compared to standard Chain-of-Thought approaches. Related resources [Soft Thinking: Unlocking the Reasoning Potential of LLMs in Continuous Concept Space](https://arxiv.org/pdf/2505.15778) ### Alternatives _No response_ ### Additional context https://arxiv.org/abs/2505.15778 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support soft thinking feature request;stale ### 🚀 The feature, motivation and pitch Motivation https://github.com/eric-ai-lab/Soft-Thinking/tree/main/sglang_soft_thinking_pkg/python/sglang Microsoft introduce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: concept representations rather than discrete tokens, achieving improved accuracy on mathematical and coding tasks while reducing token usage by up to 22.4% compared to standard Chain-of-Thought approaches. Related resou...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: concept representations rather than discrete tokens, achieving improved accuracy on mathematical and coding tasks while reducing token usage by up to 22.4% compared to standard Chain-of-Thought approaches. Related resou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , achieving improved accuracy on mathematical and coding tasks while reducing token usage by up to 22.4% compared to standard Chain-of-Thought approaches. Related resources [Soft Thinking: Unlocking the Reasoning Potent...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 778 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
