# vllm-project/vllm#28071: [RFC]: Pin all dependencies

| 字段 | 值 |
| --- | --- |
| Issue | [#28071](https://github.com/vllm-project/vllm/issues/28071) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Pin all dependencies

### Issue 正文摘录

### Motivation. Our builds should be as deterministic as possible. Building an image from the same commit should yield the same result. Otherwise we are in the wild west and things can break arbitrarily when things change underneath us, turning our main branch red. ### Proposed Change. - We pin all dependencies to precise versions - Have a way of annotating them as "hard pinned" or not - We have an automated job that: - Compares all deps with latest available versions - If there are any with new minor versions, opens a new PR updating the requirements.txt files with them. "hard pinned" dependencies are excluded. - The PR text can also include notification of any new major versions - This job runs automatically at some regular interval (suggest 1-2 times per week), but can also be run manually ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC]: Pin all dependencies RFC ### Motivation. Our builds should be as deterministic as possible. Building an image from the same commit should yield the same result. Otherwise we are in the wild west and things can br...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC]: Pin all dependencies RFC ### Motivation. Our builds should be as deterministic as possible. Building an image from the same commit should yield the same result. Otherwise we are in the wild west and things can br...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [RFC]: Pin all dependencies RFC ### Motivation. Our builds should be as deterministic as possible. Building an image from the same commit should yield the same result. Otherwise we are in the wild west and things can br...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
