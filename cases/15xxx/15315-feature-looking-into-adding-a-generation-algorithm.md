# vllm-project/vllm#15315: [Feature]: looking into adding a generation algorithm

| 字段 | 值 |
| --- | --- |
| Issue | [#15315](https://github.com/vllm-project/vllm/issues/15315) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: looking into adding a generation algorithm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi is it possible for me to add a custom generation algorithm like sample with top-k and temperature etc? I would like to implement this paper https://arxiv.org/pdf/2403.15465 .... so that when i do greedy generation i end up doing a step of rollout with it. Is there a monkey patch like method to do this ? Perhaps i can overwrite some key function or class in the codebase...is there an example or documented process to do this? Many thanks ### Alternatives ### Additional context https://arxiv.org/pdf/2403.15465 --->this paper explains the motivation ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: looking into adding a generation algorithm feature request;stale ### 🚀 The feature, motivation and pitch Hi is it possible for me to add a custom generation algorithm like sample with top-k and temperature et...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: it possible for me to add a custom generation algorithm like sample with top-k and temperature etc? I would like to implement this paper https://arxiv.org/pdf/2403.15465 .... so that when i do greedy generation i end up...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
