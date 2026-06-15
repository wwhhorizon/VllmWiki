# vllm-project/vllm#43564: [Bug] FP8 block-quant loader rejects artifacts using 'weight_scale' rather than 'weight_scale_inv' naming

| 字段 | 值 |
| --- | --- |
| Issue | [#43564](https://github.com/vllm-project/vllm/issues/43564) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;gemm_linear;model_support;quantization |
| 子分类 | debug |
| Operator 关键词 | attention;fp8;kernel;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] FP8 block-quant loader rejects artifacts using 'weight_scale' rather than 'weight_scale_inv' naming

### Issue 正文摘录

# [Bug] FP8 block-quant loader rejects artifacts whose safetensors save `weight_scale` rather than `weight_scale_inv` ## Summary A class of compressed-tensors-quantized artifacts saves FP8 block-quant scale tensors under the attribute name `weight_scale` (no `_inv` suffix), with mathematically identical content to the `weight_scale_inv` form vLLM's FP8 block-quant loader expects. The loader crashes with: ``` AttributeError: 'MergedColumnParallelLinear' object has no attribute 'weight_scale_inv'. Did you mean: 'weight_scale'? ``` The crash site (`vllm/model_executor/kernels/linear/scaled_mm/marlin.py:73` and `marlin_utils_fp8.py:106`) accesses `layer.weight_scale_inv` directly. The DeepseekV4 weight renaming mapper (`vllm/models/deepseek_v4/nvidia/model.py:1511`) only renames `.scale` → `.weight_scale_inv`; it does not handle the case where the artifact already uses the longer name `.weight_scale`. A defensive `getattr(layer, "weight_scale_inv", layer.weight_scale)` fallback would accept both naming conventions transparently. ## Reproducer `canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` (DeepSeek-V4-Flash, W4A16 routed experts + FP8 block 128×128 attention + MTP draft head). Safeten...

## 现有链接修复摘要

#36889 [WIP][Bugfix] Fix CUDA illegal memory access for GPTQ Marlin MoE with CUDA graphs | #40923 [Kernel] Marlin MoE: include SM 12.x in default arch list | #43722 [Bugfix][Quantization] Refuse block-FP8 in MarlinFP8.can_implement

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug] FP8 block-quant loader rejects artifacts using 'weight_scale' rather than 'weight_scale_inv' naming # [Bug] FP8 block-quant loader rejects artifacts whose safetensors save `weight_scale` rather than `weight_scale_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: firmed: - `canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` (post-dequant shipping fix) - The original (pre-dequant) FP8 attention in the same artifact also exhibits this — all 33,239 FP8/W4A16 scale tensors use `weight_sc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ight_scale` instead of ` .weight_scale_inv`. ```python from safetensors import safe_open with safe_open(".../layers.0.attn.wkv.weight", framework="pt") as f: t = f.get_tensor("layers.0.attn.wkv.weight") print(t.dtype, t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug] FP8 block-quant loader rejects artifacts using 'weight_scale' rather than 'weight_scale_inv' naming # [Bug] FP8 block-quant loader rejects artifacts whose safetensors save `weight_scale` rather than `weight_scale_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: -quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` (DeepSeek-V4-Flash, W4A16 routed experts + FP8 block 128×128 attention + MTP draft head). Safetensors built by `llmcompressor`'s `model_free_ptq` path which produces keys named `...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36889](https://github.com/vllm-project/vllm/pull/36889) | mentioned | 0.45 | [WIP][Bugfix] Fix CUDA illegal memory access for GPTQ Marlin MoE with CUDA graphs | ithub.com/vllm-project/vllm/pull/40923#issuecomment-4530927937) and [`#36889 reopen comment`](https://github.com/vllm-project/vllm/pull/36889#issuecomment-4531289048) — same artif… |
| [#40923](https://github.com/vllm-project/vllm/pull/40923) | mentioned | 0.45 | [Kernel] Marlin MoE: include SM 12.x in default arch list | tches_built_artifact_blocker_2026_05_25.md - this sat alongside our [`#40923 comment`](https://github.com/vllm-project/vllm/pull/40923#issuecomment-4530927937) and [`#36889 reopen… |
| [#43722](https://github.com/vllm-project/vllm/pull/43722) | closes_keyword | 0.95 | [Bugfix][Quantization] Refuse block-FP8 in MarlinFP8.can_implement | Closes one strand of #43564 (the load-time crash on consumer Blackwell). The numerical-correctness concern documented in that issue is orthogonal to this PR and remains under inves |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
