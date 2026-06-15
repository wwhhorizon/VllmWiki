# vllm-project/vllm#36739: [CPU Backend] Refactor CPU FusedMoE to MK flow

| 字段 | 值 |
| --- | --- |
| Issue | [#36739](https://github.com/vllm-project/vllm/issues/36739) |
| 状态 | open |
| 标签 | cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CPU Backend] Refactor CPU FusedMoE to MK flow

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Migrate CPU FusedMoE to MK flow to reduce maintaince overhead. Ref: #36286 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CPU Backend] Refactor CPU FusedMoE to MK flow cpu ### 🚀 The feature, motivation and pitch Migrate CPU FusedMoE to MK flow to reduce maintaince overhead. Ref: #36286 ### Alternatives _No response_ ### Additional context
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CPU Backend] Refactor CPU FusedMoE to MK flow cpu ### 🚀 The feature, motivation and pitch Migrate CPU FusedMoE to MK flow to reduce maintaince overhead. Ref: #36286 ### Alternatives _No response_ ### Additional context...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
