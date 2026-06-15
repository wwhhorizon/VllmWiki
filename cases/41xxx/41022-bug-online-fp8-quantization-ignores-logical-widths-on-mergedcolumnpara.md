# vllm-project/vllm#41022: [Bug] Online FP8 quantization ignores logical_widths on MergedColumnParallelLinear

| 字段 | 值 |
| --- | --- |
| Issue | [#41022](https://github.com/vllm-project/vllm/issues/41022) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Online FP8 quantization ignores logical_widths on MergedColumnParallelLinear

### Issue 正文摘录

## Description `MergedColumnParallelLinear` fuses multiple projections (QKV, gate_up, GDN in_proj_qkvz) into one weight matrix. Each layer carries `logical_widths` listing the shard sizes. The INT8 CUTLASS path uses this via `convert_to_channelwise` (#6552), but the FP8 online path does not. Both `Fp8OnlineLinearMethod` and `Fp8PerTensorOnlineLinearMethod` call `ops.scaled_fp8_quant` on the entire fused weight, producing one scale for all shards. ## Impact - GDN models (Qwen3.5, Qwen3.6): the GDN recurrence amplifies the precision loss into NaN or "!!!!!!!!!!!" output. - SwiGLU models (Llama, Mistral, Qwen, Gemma, etc.): the gate shard loses resolution under the shared scale. ## Reproduction `vllm serve Qwen/Qwen3.5-35B-A3B --quantization fp8`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tire fused weight, producing one scale for all shards. ## Impact - GDN models (Qwen3.5, Qwen3.6): the GDN recurrence amplifies the precision loss into NaN or "!!!!!!!!!!!" output. - SwiGLU models (Llama, Mistral, Qwen,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug] Online FP8 quantization ignores logical_widths on MergedColumnParallelLinear ## Description `MergedColumnParallelLinear` fuses multiple projections (QKV, gate_up, GDN in_proj_qkvz) into one weight matrix. Each lay...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: x. Each layer carries `logical_widths` listing the shard sizes. The INT8 CUTLASS path uses this via `convert_to_channelwise` (#6552), but the FP8 online path does not. Both `Fp8OnlineLinearMethod` and `Fp8PerTensorOnlin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: mpact - GDN models (Qwen3.5, Qwen3.6): the GDN recurrence amplifies the precision loss into NaN or "!!!!!!!!!!!" output. - SwiGLU models (Llama, Mistral, Qwen, Gemma, etc.): the gate shard loses resolution under the sha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nearMethod` call `ops.scaled_fp8_quant` on the entire fused weight, producing one scale for all shards. ## Impact - GDN models (Qwen3.5, Qwen3.6): the GDN recurrence amplifies the precision loss into NaN or "!!!!!!!!!!!...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
