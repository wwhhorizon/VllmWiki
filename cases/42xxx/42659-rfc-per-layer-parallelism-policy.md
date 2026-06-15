# vllm-project/vllm#42659: [RFC]: Per-Layer Parallelism Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#42659](https://github.com/vllm-project/vllm/issues/42659) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Per-Layer Parallelism Policy

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## 1. Motivation PR #36287 introduced TPA (tensor-parallel-size-attention) to vLLM, and review feedback from Lucas Wilkinson — *"the design shouldn't be attention-specific"* — pointed to a more general need: a per-layer parallelism policy that lets layers declare what they are and have the framework resolve their plan. ## 2. The idea A single function, owned by the framework, that turns a layer's identity into its parallelism plan: ``` ┌─────────────────────────────┐ (layer instance, prefix) ──▶ │ framework-owned resolver │──▶ plan │ (consults config + layer) │ └─────────────────────────────┘ ``` Layers consult the resolver in `__init__` instead of reading global TP accessors. A *plan* is whatever the layer needs to make local decisions — its TP width, its rank within that group, its communication backend, etc. The plan schema is open-ended; the call shape stays the same as new fields are added. The plan being a function of the layer is what makes the design non-attention-specific. The resolver doesn't know it's an attention layer — it knows it's *this* layer at *this* prefix and consults config to decide. New strategies (Q-replication, hybr...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: decisions — its TP width, its rank within that group, its communication backend, etc. The plan schema is open-ended; the call shape stays the same as new fields are added. The plan being a function of the layer is what...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: owned resolver │──▶ plan │ (consults config + layer) │ └─────────────────────────────┘ ``` Layers consult the resolver in `__init__` instead of reading global TP accessors. A *plan* is whatever the layer needs to make l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Per-Layer Parallelism Policy feature request ### 🚀 The feature, motivation and pitch ## 1. Motivation PR #36287 introduced TPA (tensor-parallel-size-attention) to vLLM, and review feedback from Lucas Wilkinson —...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: plan: { tp_size: tp } ``` One attention rule, one MLP rule. Every block matches the same two rules. Every derivative (Mistral, Phi3, NemotronNAS, TeleChat2, GLM) reuses this verbatim. ### 3.2 Nemotron-H, Jamba — hybrid...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: geneity signal already exists in the model config. ### 3.3 DSV4 — MLA + MoE + sparse indexer ```yaml parallelism_rules: axes: tp: 16 attn_tp: 1 # MLA has 1 effective KV head → TPA collapses to DCP-only dcp: 16 ep: 8 # e...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
