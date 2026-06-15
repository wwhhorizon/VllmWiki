# vllm-project/vllm#42803: [Bug] MiMoV2 load_weights: fused qkv_proj path uses naive chunk(tp,dim=0)[rank], misplaces Q values into K/V slots

| 字段 | 值 |
| --- | --- |
| Issue | [#42803](https://github.com/vllm-project/vllm/issues/42803) |
| 状态 | open |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] MiMoV2 load_weights: fused qkv_proj path uses naive chunk(tp,dim=0)[rank], misplaces Q values into K/V slots

### Issue 正文摘录

## Summary `vllm/model_executor/models/mimo_v2.py:load_weights` has a code path for fused-`qkv_proj` checkpoints (MiMo-V2 Pro variants) that does ```python if "qkv_proj" in name: if name in params_dict: param = params_dict[name] loaded_weight = loaded_weight.chunk(tp_size, dim=0)[tp_rank] default_weight_loader(param, loaded_weight) continue ``` For a checkpoint where the fused tensor is laid out `[Q | K | V]` along dim 0 — which is the case for at least `festr2/MiMo-V2.5-Pro-NVFP4-MXFP8-attn-TP8` — a naive `chunk(tp_size, dim=0)[tp_rank]` gives 7 of 8 ranks (at TP=8) rows that fall entirely inside the Q region. Those ranks' `QKVParallelLinear` parameter slots for K and V end up filled with Q values; only the last rank gets any real K/V data. Attention is therefore severely broken on 7 of 8 ranks. The proper loader (`QKVParallelLinear.weight_loader` with `shard_id="q"/"k"/"v"`) handles the TP split per-section correctly. It's already used by the `stacked_params_mapping` path for checkpoints that store Q/K/V as separate tensors; the fused path just doesn't reach it. ## Repro Model: `festr2/MiMo-V2.5-Pro-NVFP4-MXFP8-attn-TP8` (the only Pro-format quant I'm aware of that hits the fuse...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: | V]` along dim 0 — which is the case for at least `festr2/MiMo-V2.5-Pro-NVFP4-MXFP8-attn-TP8` — a naive `chunk(tp_size, dim=0)[tp_rank]` gives 7 of 8 ranks (at TP=8) rows that fall entirely inside the Q region. Those r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: 121), TP=8, Ray distributed executor. With other patches in place (MXFP8 dispatch wired into `modelopt_mixed`, `weight_scale_inv` -> `weight_scale` rename for the modelopt MXFP8 scale parameter), the model reaches Appli...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: _proj path uses naive chunk(tp,dim=0)[rank], misplaces Q values into K/V slots ## Summary `vllm/model_executor/models/mimo_v2.py:load_weights` has a code path for fused-`qkv_proj` checkpoints (MiMo-V2 Pro variants) that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: unk(tp,dim=0)[rank], misplaces Q values into K/V slots ## Summary `vllm/model_executor/models/mimo_v2.py:load_weights` has a code path for fused-`qkv_proj` checkpoints (MiMo-V2 Pro variants) that does ```python if "qkv_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: h. Proposed patch against `vllm/model_executor/models/mimo_v2.py` (replacing the `if "qkv_proj" in name:` block): ```python if "qkv_proj" in name: if name in params_dict: param = params_dict[name] try: _li = int(name.sp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
