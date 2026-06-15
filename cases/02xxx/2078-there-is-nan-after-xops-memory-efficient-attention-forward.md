# vllm-project/vllm#2078: There is NAN After "xops.memory_efficient_attention_forward"

| 字段 | 值 |
| --- | --- |
| Issue | [#2078](https://github.com/vllm-project/vllm/issues/2078) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> There is NAN After "xops.memory_efficient_attention_forward"

### Issue 正文摘录

core dumped in Warm up: ```python out = xops.memory_efficient_attention_forward( query, key, value, attn_bias=input_metadata.attn_bias, p=0.0, scale=self.scale, op=xops.fmha.MemoryEfficientAttentionFlashAttentionOp[0] if (is_hip()) else None, ) ``` I check the query, key, value, no NAN，But there is NAN in out model: llama 70B AWQ

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: key, value, attn_bias=input_metadata.attn_bias, p=0.0, scale=self.scale, op=xops.fmha.MemoryEfficientAttentionFlashAttentionOp[0] if (is_hip()) else None, ) ``` I check the
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ) ``` I check the query, key, value, no NAN，But there is NAN in out model: llama 70B AWQ
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: scale=self.scale, op=xops.fmha.MemoryEfficientAttentionFlashAttentionOp[0] if (is_hip()) else None, ) ``` I check the query, key, value, no NAN，But there is NAN in out model: llama 70B AWQ
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: There is NAN After "xops.memory_efficient_attention_forward" core dumped in Warm up: ```python out = xops.memory_efficient_attention_forward( query, key, value, attn_bias=input_met
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tn_bias=input_metadata.attn_bias, p=0.0, scale=self.scale, op=xops.fmha.MemoryEfficientAttentionFlashAttentionOp[0] if (is_hip()) else None, ) ``` I check the query, key, value, no NAN，But there is NAN in out model:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
