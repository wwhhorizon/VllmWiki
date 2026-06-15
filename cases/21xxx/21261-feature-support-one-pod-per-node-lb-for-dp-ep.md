# vllm-project/vllm#21261: [Feature]: Support One Pod Per Node LB for DP/EP

| 字段 | 值 |
| --- | --- |
| Issue | [#21261](https://github.com/vllm-project/vllm/issues/21261) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support One Pod Per Node LB for DP/EP

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we support 2 modes for DP/EP: - internal lb --- single vllm instance, head node manages all ranks - external lb --- N vllm instances for N ranks, async llm <> engine core per rank We need a hybrid mode where we can have "one-pod-per-node". For example: - N nodes, 8 ranks per node - 1 AsyncLLM per node, 8 EngineCores per node - External LB balances between nodes WIP PR: https://github.com/vllm-project/vllm/pull/21238 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support One Pod Per Node LB for DP/EP feature request ### 🚀 The feature, motivation and pitch Currently, we support 2 modes for DP/EP: - internal lb --- single vllm instance, head node manages all ranks - ext...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
