# vllm-project/vllm#37563: mm_fp4 trtllm backend leaks padding scales into real rows (use_8x4_sf_layout=True)

| 字段 | 值 |
| --- | --- |
| Issue | [#37563](https://github.com/vllm-project/vllm/issues/37563) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | gemm_linear;hardware_porting;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;moe;quantization |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> mm_fp4 trtllm backend leaks padding scales into real rows (use_8x4_sf_layout=True)

### Issue 正文摘录

## Bug: TRT-LLM mm_fp4 with `use_8x4_sf_layout=True` reads padding rows' scales and applies them to real rows ### Summary When `mm_fp4` is called with `backend="trtllm"` and `use_8x4_sf_layout=True` (triggered when `m 32 (use_8x4_sf_layout=False)**: clean — bug is specific to 8×4 SF layout path - The bug persists even when scales are produced by the correct `flashinfer_quant_nvfp4_8x4_sf_layout` quantization function (passing `backend="trtllm"` to `scaled_fp4_quant`) ### Workaround Setting padding scales to **zero** (0x00 in float8_e4m3fn) neutralizes the bug: even though the kernel still reads the wrong scales, `0 * data = 0` contributes nothing to real rows' output. This is the same principle behind the `torch.zeros` fix in `create_fp4_scale_tensor` for the CUTLASS MoE path. ### Production impact In R1 NVFP4 decode, production traces show all `mm_fp4` GEMMs use the CUTLASS backend (which is unaffected). The TRT-LLM backend is only used for `cvt_fp16_to_fp4_expert` (quantization, not GEMM). So this bug does not currently affect R1 production, but it would affect any deployment that routes through `flashinfer_scaled_fp4_mm` with `backend="trtllm"` and small batch sizes (m ≤ 32). #...

## 现有链接修复摘要

#37564 [Bugfix] Zero-init NVFP4 padding scales to prevent NaN contamination

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: mm_fp4 trtllm backend leaks padding scales into real rows (use_8x4_sf_layout=True) ## Bug: TRT-LLM mm_fp4 with `use_8x4_sf_layout=True` reads padding rows' scales and applies them to real rows ### Summary When `mm_fp4`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: at routes through `flashinfer_scaled_fp4_mm` with `backend="trtllm"` and small batch sizes (m ≤ 32). ### Relevant code - `use_8x4_sf_layout` gate: [`vllm/_custom_ops.py:1732`](https://github.com/vllm-project/vllm/blob/1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: mm_fp4 trtllm backend leaks padding scales into real rows (use_8x4_sf_layout=True) ## Bug: TRT-LLM mm_fp4 with `use_8x4_sf_layout=True` reads padding rows' scales and applies them to real rows ### Summary When `mm_fp4`...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ehind the `torch.zeros` fix in `create_fp4_scale_tensor` for the CUTLASS MoE path. ### Production impact In R1 NVFP4 decode, production traces show all `mm_fp4` GEMMs use the CUTLASS backend (which is unaffected). The T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ` (triggered when `m 32 (use_8x4_sf_layout=False)**: clean — bug is specific to 8×4 SF layout path - The bug persists even when scales are produced by the correct `flashinfer_quant_nvfp4_8x4_sf_layout` quantization func...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37564](https://github.com/vllm-project/vllm/pull/37564) | closes_keyword | 0.95 | [Bugfix] Zero-init NVFP4 padding scales to prevent NaN contamination | Closes #37563 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
