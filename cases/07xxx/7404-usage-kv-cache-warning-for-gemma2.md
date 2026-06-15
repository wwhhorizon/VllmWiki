# vllm-project/vllm#7404: [Usage]: KV Cache Warning for `gemma2`

| 字段 | 值 |
| --- | --- |
| Issue | [#7404](https://github.com/vllm-project/vllm/issues/7404) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: KV Cache Warning for `gemma2`

### Issue 正文摘录

### Your current environment I get the following warning running a quantized version of `gemma2`, when I have not quantized the kv cache: ```bash WARNING 08-11 22:31:50 gemma2.py:399] Some weights are not initialized from checkpoints: {'model.layers.2.self_attn.attn.v_scale', 'model.layers.13.self_attn.attn.v_scale', 'model.layers.14.self_attn.attn.v_scale', 'model.layers.16.self_attn.attn.k_scale', 'model.layers.16.self_attn.attn.v_scale', 'model.layers.19.self_attn.attn.v_scale', 'model.layers.21.self_attn.attn.v_scale', 'model.layers.2.self_attn.attn.k_scale', 'model.layers.3.self_attn.attn.k_scale', 'model.layers.20.self_attn.attn.v_scale', 'model.layers.24.self_attn.attn.k_scale', 'model.layers.6.self_attn.attn.k_scale', 'model.layers.6.self_attn.attn.v_scale', 'model.layers.12.self_attn.attn.k_scale', 'model.layers.15.self_attn.attn.v_scale', 'model.layers.18.self_attn.attn.k_scale', 'model.layers.14.self_attn.attn.k_scale', 'model.layers.9.self_attn.attn.k_scale', 'model.layers.11.self_attn.attn.v_scale', 'model.layers.11.self_attn.attn.k_scale', 'model.layers.24.self_attn.attn.v_scale', 'model.layers.7.self_attn.attn.v_scale', 'model.layers.1.self_attn.attn.v_scale', 'mode...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: tale ### Your current environment I get the following warning running a quantized version of `gemma2`, when I have not quantized the kv cache: ```bash WARNING 08-11 22:31:50 gemma2.py:399] Some weights are not initializ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: KV Cache Warning for `gemma2` usage;stale ### Your current environment I get the following warning running a quantized version of `gemma2`, when I have not quantized the kv cache: ```bash WARNING 08-11 22:31:50...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: our current environment I get the following warning running a quantized version of `gemma2`, when I have not quantized the kv cache: ```bash WARNING 08-11 22:31:50 gemma2.py:399] Some weights are not initialized from ch...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: KV Cache Warning for `gemma2` usage;stale ### Your current environment I get the following warning running a quantized version of `gemma2`, when I have not quantized the kv cache: ```bash WARNING 08-11 22:31:50...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: KV Cache Warning for `gemma2` usage;stale ### Your current environment I get the following warning running a quantized version of `gemma2`, when I have not quantized the kv cache: ```bash WARNING 08-11 22:31:50...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
