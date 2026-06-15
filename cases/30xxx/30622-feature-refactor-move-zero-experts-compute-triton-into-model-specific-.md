# vllm-project/vllm#30622: [Feature]: [Refactor] Move `zero_experts_compute_triton` into model specific file

| 字段 | 值 |
| --- | --- |
| Issue | [#30622](https://github.com/vllm-project/vllm/issues/30622) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [Refactor] Move `zero_experts_compute_triton` into model specific file

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, [`zero_expert_result`](https://github.com/vllm-project/vllm/blob/7c16f3fbcc45e95491b90811fe9af1e6dfe297bc/vllm/model_executor/layers/fused_moe/layer.py#L1649-L1664) is only used for the [LongCat-Flash model](https://github.com/vllm-project/vllm/pull/23991). While it introduces three additional parameters for `FusedMoE` and returns a third parameter, which is only used for longcat model. For a clean routing interface, we should only keep `topk_weights` and `topk_ids` from the `FusedMoE.select_experts`. Move the related function to the longcat model file and keep the routing interface clean. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Feature]: [Refactor] Move `zero_experts_compute_triton` into model specific file feature request ### 🚀 The feature, motivation and pitch Currently, [`zero_expert_result`](https://github.com/vllm-project/vllm/blob/7c16f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: [Refactor] Move `zero_experts_compute_triton` into model specific file feature request ### 🚀 The feature, motivation and pitch Currently, [`zero_expert_result`](https://github.com/vllm-project/vllm/blob/7c16f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: [Refactor] Move `zero_experts_compute_triton` into model specific file feature request ### 🚀 The feature, motivation and pitch Currently, [`zero_expert_result`](https://github.com/vllm-project/vllm/blob/7c16f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: [Refactor] Move `zero_experts_compute_triton` into model specific file feature request ### 🚀 The feature, motivation and pitch Currently, [`zero_expert_result`](https://github.com/vllm-project/vllm/blob/7c16f...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
