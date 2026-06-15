# vllm-project/vllm#43765: [Feature]: Support PD disaggregation / KV transfer for hybrid SSM/GDN models such as Qwen3.5-397B-A17B-W8A8

| 字段 | 值 |
| --- | --- |
| Issue | [#43765](https://github.com/vllm-project/vllm/issues/43765) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support PD disaggregation / KV transfer for hybrid SSM/GDN models such as Qwen3.5-397B-A17B-W8A8

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Feature request I would like to ask whether vLLM plans to support PD disaggregation / KV transfer for hybrid SSM/GDN models, such as Qwen3.5-397B-A17B-W8A8, and whether there is an expected release version or roadmap for this support. ## Background Qwen3.5-397B-A17B-W8A8 is a hybrid attention model. Its `text_config.layer_types` contains both `linear_attention` and `full_attention` layers. The layer pattern is roughly: ```text linear_attention linear_attention linear_attention full_attention ... In my environment, the KV cache groups are split as follows: group[0]: MambaSpec, mamba_type='gdn_attention', linear_attn layers 0,4,8,... group[1]: MambaSpec, mamba_type='gdn_attention', linear_attn layers 1,5,9,... group[2]: MambaSpec, mamba_type='gdn_attention', linear_attn layers 2,6,10,... group[3]: FullAttentionSpec, self_attn/full_attention layers 3,7,11,... So this model contains both: MambaSpec / GDN / linear_attention state cache FullAttentionSpec / full_attention KV cache Issue with MooncakeConnector When using MooncakeConnector for PD disaggregation, Mooncake currently obtains the attention backend from the first layer: backend = get_c...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: attention linear_attention full_attention ... In my environment, the KV cache groups are split as follows: group[0]: MambaSpec, mamba_type='gdn_attention', linear_attn layers 0,4,8,... group[1]: MambaSpec, mamba_type='g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support PD disaggregation / KV transfer for hybrid SSM/GDN models such as Qwen3.5-397B-A17B-W8A8 feature request ### 🚀 The feature, motivation and pitch ## Feature request I would like to ask whether vLLM pla...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ar_attention linear_attention full_attention ... In my environment, the KV cache groups are split as follows: group[0]: MambaSpec, mamba_type='gdn_attention', linear_attn layers 0,4,8,... group[1]: MambaSpec, mamba_type...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: onnector for PD disaggregation, Mooncake currently obtains the attention backend from the first layer: backend = get_current_attn_backend(vllm_config) Since the first layer of Qwen3.5-397B-A17B-W8A8 is linear_attention,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: such as Qwen3.5-397B-A17B-W8A8, and whether there is an expected release version or roadmap for this support. ## Background Qwen3.5-397B-A17B-W8A8 is a hybrid attention model. Its `text_config.layer_types` contains both...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
