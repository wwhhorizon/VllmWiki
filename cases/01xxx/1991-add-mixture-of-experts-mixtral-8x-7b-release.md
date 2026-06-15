# vllm-project/vllm#1991: Add Mixture of Experts: Mixtral 8x 7B release

| 字段 | 值 |
| --- | --- |
| Issue | [#1991](https://github.com/vllm-project/vllm/issues/1991) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add Mixture of Experts: Mixtral 8x 7B release

### Issue 正文摘录

Mistral AI released their new model called `Mixtral` which is an MoE architecture based on MegaBlocks. It includes 8 experts with the size being 7 billion parameters each. Here is the model configuration: - dim: 4096 - n_layers: 32 - head_dim: 128 - hidden_dim: 14336 - n_heads: 32 - n_kv_heads: 8 - norm_eps: 1e-05 - vocab_size: 32000 - moe: - num_experts_per_tok: 2 - num_experts: 8 Weights: https://twitter.com/MistralAI/status/1733150512395038967 Paper: https://arxiv.org/pdf/2211.15841.pdf Code: https://github.com/stanford-futuredata/megablocks CC: @WoosukKwon @zhuohan123 for visibility.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Mixture of Experts: Mixtral 8x 7B release Mistral AI released their new model called `Mixtral` which is an MoE architecture based on MegaBlocks. It includes 8 experts with the size being 7 billion parameters each. Here...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Add Mixture of Experts: Mixtral 8x 7B release Mistral AI released their new model called `Mixtral` which is an MoE architecture based on MegaBlocks. It includes 8 experts with the size being 7 billion parameters each. H...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ase Mistral AI released their new model called `Mixtral` which is an MoE architecture based on MegaBlocks. It includes 8 experts with the size being 7 billion parameters each. Here is the model configuration: - dim: 409...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eir new model called `Mixtral` which is an MoE architecture based on MegaBlocks. It includes 8 experts with the size being 7 billion parameters each. Here is the model configuration: - dim: 4096 - n_layers: 32 - head_di...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
