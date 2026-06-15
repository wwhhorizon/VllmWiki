# vllm-project/vllm#43472: DSV4-Pro MTP draft: stacked attn FP8 scale loader gap + MTP forward-path mainline-vs-fork divergence

| 字段 | 值 |
| --- | --- |
| Issue | [#43472](https://github.com/vllm-project/vllm/issues/43472) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | activation;cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> DSV4-Pro MTP draft: stacked attn FP8 scale loader gap + MTP forward-path mainline-vs-fork divergence

### Issue 正文摘录

## Summary Two related findings while bringing up `canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP` against mainline vLLM. Both block end-to-end MTP serving for DSV4-Pro on the current mainline subpackage path. ## 1. Stacked attn FP8 scale loader gap (`fused_wqa_wkv.weight_scale_inv` KeyError) Repro: serve `deepseek-ai/DeepSeek-V4-Pro` (native MXFP4-FP8 with MTP) on mainline + the patches from PRs #43248, #43288, #43290, #43319, with `--speculative-config method=mtp`. ``` KeyError: 'model.layers.61.mtp_block.attn.fused_wqa_wkv.weight_scale_inv' ``` The native checkpoint has `mtp.0.attn.wq_a.scale` and `mtp.0.attn.wkv.scale` (per-key FP8 block scales). The loader at `vllm/models/deepseek_v4/nvidia/mtp.py:load_weights`: 1. Resolves `.scale` to `.weight_scale_inv` (per the candidate-list logic from PR #43319). 2. Iterates `stacked_params_mapping = [("attn.fused_wqa_wkv", "attn.wq_a", 0), ("attn.fused_wqa_wkv", "attn.wkv", 1)]`. 3. Renames `model.layers.61.mtp_block.attn.wq_a.weight_scale_inv` → `model.layers.61.mtp_block.attn.fused_wqa_wkv.weight_scale_inv`. 4. `params_dict[name]` → `KeyError` because the fused param isn't registered under that name (likely registered as `fused_wqa_wkv` (...

## 现有链接修复摘要

#43248 [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | #43288 [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | #43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43319 [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: DSV4-Pro MTP draft: stacked attn FP8 scale loader gap + MTP forward-path mainline-vs-fork divergence ## Summary Two related findings while bringing up `canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP` against mainline vLLM....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: mhc kernels split into `vllm/model_executor/kernels/mhc/{tilelang,torch,triton,aiter}.py` with CustomOp dispatch; fork inlines tilelang kernels in `layers/mhc.py`. Mathematically these should be equivalent. But the trun...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: differently. ## 2. MTP draft acceptance ~3% on mainline vs ~91% on fork docker A separately observable, large quality gap on the SAME model weights: | Build | Artifact | MTP n=1 | |---|---|---| | `vllm/vllm-openai:deeps...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: parate `hc_pre`/`hc_post` per layer. 2. Mainline integrates `ffn_norm` + router gate into `NormGatedLinear` inside `DeepseekV4MoE`. Fork keeps `self.ffn_norm = RMSNorm(...)` separate. 3. Mainline's MTP loader has 3 new...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: `canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP` against mainline vLLM. Both block end-to-end MTP serving for DSV4-Pro on the current mainline subpackage path. ## 1. Stacked attn FP8 scale loader gap (`fused_wqa_wkv.weight_...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43248](https://github.com/vllm-project/vllm/pull/43248) | mentioned | 0.45 | [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | vironment - vllm `0.21.1rc1.dev199+g30f52a895` (= `39910f2b25` + prs #43248, #43288, #43290, #43319 + the v0.3 bf16-mtp dispatch patch). - hardware: b300 sxm6 ac (compute_cap 10.3… |
| [#43288](https://github.com/vllm-project/vllm/pull/43288) | mentioned | 0.45 | [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | t - vllm `0.21.1rc1.dev199+g30f52a895` (= `39910f2b25` + prs #43248, #43288, #43290, #43319 + the v0.3 bf16-mtp dispatch patch). - hardware: b300 sxm6 ac (compute_cap 10.3), cuda… |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | m `0.21.1rc1.dev199+g30f52a895` (= `39910f2b25` + prs #43248, #43288, #43290, #43319 + the v0.3 bf16-mtp dispatch patch). - hardware: b300 sxm6 ac (compute_cap 10.3), cuda 13.0, t… |
| [#43319](https://github.com/vllm-project/vllm/pull/43319) | mentioned | 0.45 | [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | 1rc1.dev199+g30f52a895` (= `39910f2b25` + prs #43248, #43288, #43290, #43319 + the v0.3 bf16-mtp dispatch patch). - hardware: b300 sxm6 ac (compute_cap 10.3), cuda 13.0, torch 2.1… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
