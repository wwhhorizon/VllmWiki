# vllm-project/vllm#28137: [Feature]: Refactor `aiter_shared_expert_fusion`

| 字段 | 值 |
| --- | --- |
| Issue | [#28137](https://github.com/vllm-project/vllm/issues/28137) |
| 状态 | closed |
| 标签 | help wanted;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Refactor `aiter_shared_expert_fusion`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have a special case in `FusedMoE` layer for `aiter_shared_expert_fusion` which creates various if branches spattered across the layer We should factor this out ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Refactor `aiter_shared_expert_fusion` help wanted;stale ### 🚀 The feature, motivation and pitch We have a special case in `FusedMoE` layer for `aiter_shared_expert_fusion` which creates various if branches sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Refactor `aiter_shared_expert_fusion` help wanted;stale ### 🚀 The feature, motivation and pitch We have a special case in `FusedMoE` layer for `aiter_shared_expert_fusion` which creates various if branches sp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: help wanted;stale ### 🚀 The feature, motivation and pitch We have a special case in `FusedMoE` layer for `aiter_shared_expert_fusion` which creates various if branches spattered across the layer We should factor this ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Refactor `aiter_shared_expert_fusion` help wanted;stale ### 🚀 The feature, motivation and pitch We have a special case in `FusedMoE` layer for `aiter_shared_expert_fusion` which creates various if branches sp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
