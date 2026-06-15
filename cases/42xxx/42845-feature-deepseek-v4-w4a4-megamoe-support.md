# vllm-project/vllm#42845: [Feature]: DeepSeek V4 w4a4 MegaMoE support

| 字段 | 值 |
| --- | --- |
| Issue | [#42845](https://github.com/vllm-project/vllm/issues/42845) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: DeepSeek V4 w4a4 MegaMoE support

### Issue 正文摘录

## Problem DeepSeek V4 uses a MoE architecture where expert weights are already quantized to FP4 (w4), but activations in the MegaMoE pre-dispatch stage are still packed into the symmetric buffer as FP8 (E4M3) — one byte per activation value. On Blackwell (SM100), DeepGEMM already supports FP4 activations. The mismatch is wasteful in two ways: 1. **Buffer footprint**: FP8 packing uses 2× the memory that FP4 would require. 2. **Mainloop efficiency**: FP8 activations force the `kind::mxf8f6f4` mainloop (K=32 with padding). FP4 activations unlock the `kind::mxf4` mainloop (K=64 dense), doubling compute density. The goal of this issue is to support packing activations as FP4 (E2M1) in the MegaMoE pre-dispatch stage, turning w4a8 into true w4a4. --- ## Root Cause Analysis ### Current data flow In `_run_mega_moe()`, the current path is: 1. A Triton kernel (`_stage_deepseek_v4_mega_moe_inputs`) quantizes `hidden_states` to FP8 and packs them into the `x` slot of the symmetric buffer, along with `topk_idx` and `topk_weights`. 2. `fp8_fp4_mega_moe` runs the actual MoE computation. The Triton kernel only outputs FP8 — this is a hard constraint. Changing the kernel to output FP4 E2M1 is non-...

## 现有链接修复摘要

#42844 [Model][Experimental] DeepSeek V4 w4a4 MegaMoE support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: FP8 packing uses 2× the memory that FP4 would require. 2. **Mainloop efficiency**: FP8 activations force the `kind::mxf8f6f4` mainloop (K=32 with padding). FP4 activations unlock the `kind::mxf4` mainloop (K=64 dense),...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: e. On Blackwell (SM100), DeepGEMM already supports FP4 activations. The mismatch is wasteful in two ways: 1. **Buffer footprint**: FP8 packing uses 2× the memory that FP4 would require. 2. **Mainloop efficiency**: FP8 a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: em DeepSeek V4 uses a MoE architecture where expert weights are already quantized to FP4 (w4), but activations in the MegaMoE pre-dispatch stage are still packed into the symmetric buffer as FP8 (E4M3) — one byte per ac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: w4a4 MegaMoE support feature request ## Problem DeepSeek V4 uses a MoE architecture where expert weights are already quantized to FP4 (w4), but activations in the MegaMoE pre-dispatch stage are still packed into the sym...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Feature]: DeepSeek V4 w4a4 MegaMoE support feature request ## Problem DeepSeek V4 uses a MoE architecture where expert weights are already quantized to FP4 (w4), but activations in the MegaMoE pre-dispatch stage are st...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42844](https://github.com/vllm-project/vllm/pull/42844) | mentioned | 0.6 | [Model][Experimental] DeepSeek V4 w4a4 MegaMoE support | [Model][Experimental] DeepSeek V4 w4a4 MegaMoE support seealso: #42845 https://github.com/deepseek-ai/DeepGEMM/issues/338 ## Purpose MegaMoE currently packs activations as FP8 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
