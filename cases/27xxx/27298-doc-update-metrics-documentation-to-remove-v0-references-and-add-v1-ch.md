# vllm-project/vllm#27298: [Doc]: Update metrics documentation to remove V0 references and add v1 changes.

| 字段 | 值 |
| --- | --- |
| Issue | [#27298](https://github.com/vllm-project/vllm/issues/27298) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update metrics documentation to remove V0 references and add v1 changes.

### Issue 正文摘录

## Problem The metrics documentation in `docs/design/metrics.md` still contains references to V0 metrics implementation, but V0 metrics have been removed after @njhill 's PR https://github.com/vllm-project/vllm/pull/27215 was merged. To avoid confusion, I think we should remove this and update it with the new set of v1 metrics. Was curious if we want to keep this v0 reference and add the v1 details on top of this. ### Suggest a potential alternative/fix 1. Remove all V0 references from the metrics documentation. 2. Update the introduction to focus on V1 metrics only. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
