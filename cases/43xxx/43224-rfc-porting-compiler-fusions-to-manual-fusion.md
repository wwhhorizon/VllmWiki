# vllm-project/vllm#43224: [RFC]: Porting compiler fusions to manual fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#43224](https://github.com/vllm-project/vllm/issues/43224) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;gemm;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Porting compiler fusions to manual fusion

### Issue 正文摘录

## Motivation. #42770 lays out the move from full-graph `torch.compile` to manual fusion expressed directly in model code. This issue tracks the concrete porting work for **section 1-1** of that RFC: enumerating the fusions currently performed by `vllm/compilation/passes/` and mapping each one to a work item to port to a manual call site in model code. To be clear this workstream is meant to touch all existing portable model definitions where compiler fusion pass would apply previously. The goal is **no performance regression** as we delete each compiler pass. Each fusion below is either: - ported to a "big fused op" callable from model code, - collapsed into another fused op, - or explicitly dropped (with rationale). ## Proposed Change. ### Changes to QuantMethod This is clearly needed for fusions where we are fusing the input quant op from a downstream Linear layer. When a linear layer ops in, by registering a `self.input_quant_key = QuantKey.XX`, the fused operation will return a new `QuantizedActivation` instead of a `torch.Tensor`. When the linear's kernel sees that the input is not a simple unquantized tensor, it will pass it through directly to the matmul without requantizi...

## 现有链接修复摘要

#43355 [Kernel] Add native CUDA fused RoPE + KV cache write op, opt-in for flash_attn | #43520 manually fuse norm and rope | #43772 Port MLA attention + quantization fusion to manual fused kernel | #43944 [Manual Fusion][ROCm] Port RMS + Group Quant Fused Op for Qwen3 on ROCm Platform | #44260 Add the QuantizedActivation linear-kernel contract

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: xplicitly dropped (with rationale). ## Proposed Change. ### Changes to QuantMethod This is clearly needed for fusions where we are fusing the input quant op from a downstream Linear layer. When a linear layer ops in, by...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: efully testing performance and accuracy for at least one model within an architecture. ### Inventory of fusion passes In rough priority order. Sub-issues will be filed per fused op to track ownership, kernel coverage, a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: Porting compiler fusions to manual fusion RFC ## Motivation. #42770 lays out the move from full-graph `torch.compile` to manual fusion expressed directly in model code. This issue tracks the concrete porting work...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e from full-graph `torch.compile` to manual fusion expressed directly in model code. This issue tracks the concrete porting work for **section 1-1** of that RFC: enumerating the fusions currently performed by `vllm/comp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rating the fusions currently performed by `vllm/compilation/passes/` and mapping each one to a work item to port to a manual call site in model code. To be clear this workstream is meant to touch all existing portable m...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | mentioned | 0.6 | [Kernel] Add native CUDA fused RoPE + KV cache write op, opt-in for flash_attn | cit `uint4` stores. - [ ] Manual call-site rewire in model code (per #43224's manual-fusion direction — Step 2 above) ## Kernel design - 1 CTA per token. Block size = `min(max(rop |
| [#43520](https://github.com/vllm-project/vllm/pull/43520) | mentioned | 0.6 | manually fuse norm and rope | manually fuse norm and rope ## Purpose #43497 #43224 Enable the `fused_qk_norm_rope kernel` across several models. A new `can_use_fused_qk_norm_rope` helper is u |
| [#43772](https://github.com/vllm-project/vllm/pull/43772) | mentioned | 0.6 | Port MLA attention + quantization fusion to manual fused kernel | unction logic for various quantization modes and edge cases Related: #43224 |
| [#43944](https://github.com/vllm-project/vllm/pull/43944) | mentioned | 0.6 | [Manual Fusion][ROCm] Port RMS + Group Quant Fused Op for Qwen3 on ROCm Platform | for Qwen3 on ROCm Platform ## Purpose Part of the effort detailed in #43224 Bench results for Qwen/Qwen3-32B-FP8 (random 1024-in / 128-out, 1000 prompts, request_rate=inf): Metric |
| [#44260](https://github.com/vllm-project/vllm/pull/44260) | mentioned | 0.6 | Add the QuantizedActivation linear-kernel contract | edActivation linear-kernel contract ## Purpose First part of #43224 for quant fusion support. Introduce `QuantizedActivation`: a pre-quantized activation that fused kernel ca |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
