# vllm-project/vllm#40130: [Feature]: Support n_positions config field for nomic_bert models to enable inference beyond max_position_embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#40130](https://github.com/vllm-project/vllm/issues/40130) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support n_positions config field for nomic_bert models to enable inference beyond max_position_embeddings

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Support n_positions config field for nomic_bert like models to enable inference beyond max_position_embeddings nomic-embed-text-v1.5 publishes n_positions: 8192 in its config.json to signal that RoPE frequencies are precomputed to 8192 tokens, enabling inference beyond the training length of 2048. vLLM currently has no awareness of this field and always derives max context from max_position_embeddings, capping at 2048. This RFE requests that vLLM recognise n_positions for nomic_bert model types and use it as the effective max context length. Config.json https://huggingface.co/nomic-ai/nomic-embed-text-v1.5/blob/main/config.json ``` "n_positions": 8192, /← TRUE max positions (8192, not 2048!) "max_position_embeddings": 2048, ← what vLLM reads by default (misleading) "max_trained_positions": 2048, ← trained up to 2048 "rope_parameters": { "rope_theta": 1000.0, ← RoPE base frequency "rope_type": "default" ← standard RoPE (no dynamic scaling) }, "rotary_emb_base": 1000, ← confirms RoPE is active "rotary_emb_fraction": 1.0, ← RoPE applied to 100% of head dims "rotary_emb_interleaved": false, "rotary_emb_scale_base": null, ← no trained scaling fac...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support n_positions config field for nomic_bert models to enable inference beyond max_position_embeddings feature request ### 🚀 The feature, motivation and pitch Support n_positions config field for nomic_ber...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ublishes n_positions: 8192 in its config.json to signal that RoPE frequencies are precomputed to 8192 tokens, enabling inference beyond the training length of 2048. vLLM currently has no awareness of this field and alwa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: pplied to 100% of head dims "rotary_emb_interleaved": false, "rotary_emb_scale_base": null, ← no trained scaling factor set "rotary_scaling_factor": null, ← no scaling factor set ``` 1.When model_type == "nomic_bert" an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , ← RoPE applied to 100% of head dims "rotary_emb_interleaved": false, "rotary_emb_scale_base": null, ← no trained scaling factor set "rotary_scaling_factor": null, ← no scaling factor set ``` 1.When model_type == "nomi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
