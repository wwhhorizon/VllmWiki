# vllm-project/vllm#35402: [Bug]: GPT-2 scale_attn_weights config flag is ignored in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#35402](https://github.com/vllm-project/vllm/issues/35402) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT-2 scale_attn_weights config flag is ignored in vLLM

### Issue 正文摘录

### Your current environment Environment-independent issue. This is a configuration compliance issue discovered by code inspection. ### 🐛 Describe the bug In the vLLM GPT-2 implementation, the attention scaling factor is always set to: ``` self.scale = self.head_dim**-0.5 ``` which differs from the Transformers implementation: ``` # transformers/models/gpt2/modeling_gpt2.py if module.scale_attn_weights: attn_weights = attn_weights / torch.full( [], value.size(-1) ** 0.5, dtype=attn_weights.dtype, device=attn_weights.device ) ``` When scale_attn_weights=False, Transformers does not apply scaling, while vLLM always uses head_dim**-0.5. In the vLLM GPT-2 code, I noticed that several configuration options are explicitly restricted: ``` assert not config.add_cross_attention assert not config.scale_attn_by_inverse_layer_idx assert not config.reorder_and_upcast_attn ``` Since vLLM already enforces configuration invariants using assertions, a consistent approach might be to explicitly require: ``` assert config.scale_attn_weights ``` This would make the assumption explicit and avoid silent behavioral differences from the Transformers implementation, without requiring additional changes. #...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: GPT-2 scale_attn_weights config flag is ignored in vLLM bug;stale ### Your current environment Environment-independent issue. This is a configuration compliance issue discovered by code inspection. ### 🐛 Describe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: GPT-2 scale_attn_weights config flag is ignored in vLLM bug;stale ### Your current environment Environment-independent issue. This is a configuration compliance issue discovered by code inspection. ### 🐛 Describe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e vLLM GPT-2 code, I noticed that several configuration options are explicitly restricted: ``` assert not config.add_cross_attention assert not config.scale_attn_by_inverse_layer_idx assert not config.reorder_and_upcast...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: device=attn_weights.device ) ``` When scale_attn_weights=False, Transformers does not apply scaling, while vLLM always uses head_dim**-0.5. In the vLLM GPT-2 code, I noticed that several configuration options are explic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
