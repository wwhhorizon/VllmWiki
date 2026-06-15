# vllm-project/vllm#39389: [Bug]: V1 engine prefix caching was causing non-deterministic outputs during greedy decoding T=0

| 字段 | 值 |
| --- | --- |
| Issue | [#39389](https://github.com/vllm-project/vllm/issues/39389) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 engine prefix caching was causing non-deterministic outputs during greedy decoding T=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: V1 engine prefix caching was causing non-deterministic outputs during greedy decoding T=0 bug ### Your current environment ### 🐛 Describe the bug NA ### Before submitting a new issue... - [x] Make sure you alread...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: V1 engine prefix caching was causing non-deterministic outputs during greedy decoding T=0 bug ### Your current environment ### 🐛 Describe the bug NA ### Before submitting a new issue... - [x] Make sure you alread...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
