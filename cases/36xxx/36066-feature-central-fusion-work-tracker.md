# vllm-project/vllm#36066: [Feature]: Central fusion work tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#36066](https://github.com/vllm-project/vllm/issues/36066) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;fp8;gemm;kernel;operator;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Central fusion work tracker

### Issue 正文摘录

## Overview This issue tracks the status and coverage of major fusion passes in vLLM across hardware and quantization configurations. Reference point: #35538 (fusion documentation work). See also: docs/design/fusions.md (from #35538). **Last updated**: March 4th, commit b1d9f53. ## Fusion pass matrix This table tracks the most performant configuration; e.g. attn+fp8 fusion is supported on sm90 for the triton attention kernel but that's not the default. Some fusions might even have multiple kernels available per-platform: e.g. RMSNorm+Quant has both custom CUDA/HIP and AITER kernels on ROCm. ### Legend / status icons - ✅ Supported **and on by default** - ⚙️ Supported **but not enabled by default** - 🚧 Work in progress - 🟧 Kernel exists, not integrated - ❌ Not supported, **kernel wanted** - ⏸️ Not applicable for platform - ❓ Status unknown --- | Fusion Pass | Variant / Quant combo | sm100 | sm90 | ROCm | Notes | |--------------------------------------------------|------------------------------------------------------------|:-----:|:----:|:----:|--------------------------------------------------------------------| | RMSNorm+Quant (`RMSNormQuantFusionPass`) | FP8 static per-tensor | ✅...

## 现有链接修复摘要

#35538 [docs][torch.compile] Add fusions.md — kernel/operator fusion reference page | #36851 [ROCm] Enable Sequence Parallelism for AMD GPUs (MI300X/MI325X/MI355X) | #37110 Fuse per-group FP8 dynamic quant onto Triton attention kernel | #39952 [Feature] Fused SiLU + Mul + per-token dynamic FP8 quantization (Triton) | #43056 [Perf][Kernel] Fused QK-RMSNorm + mRoPE CUDA kernel for Qwen3-VL

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: e status and coverage of major fusion passes in vLLM across hardware and quantization configurations. Reference point: #35538 (fusion documentation work). See also: docs/design/fusions.md (from #35538). **Last updated**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: ). See also: docs/design/fusions.md (from #35538). **Last updated**: March 4th, commit b1d9f53. ## Fusion pass matrix This table tracks the most performant configuration; e.g. attn+fp8 fusion is supported on sm90 for th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: formant configuration; e.g. attn+fp8 fusion is supported on sm90 for the triton attention kernel but that's not the default. Some fusions might even have multiple kernels available per-platform: e.g. RMSNorm+Quant has b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dd a fusion pass or expand kernel coverage, please update this table and link the PR(s). performance activation_norm;attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;quantization activat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: coverage of major fusion passes in vLLM across hardware and quantization configurations. Reference point: #35538 (fusion documentation work). See also: docs/design/fusions.md (from #35538). **Last updated**: March 4th,...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35538](https://github.com/vllm-project/vllm/pull/35538) | mentioned | 0.45 | [docs][torch.compile] Add fusions.md — kernel/operator fusion reference page | (fusion documentation work). see also: docs/design/fusions.md (from #35538). **last updated**: march 4th, commit b1d9f53. ## fusion pass matrix this table tracks the most performa… |
| [#36851](https://github.com/vllm-project/vllm/pull/36851) | mentioned | 0.6 | [ROCm] Enable Sequence Parallelism for AMD GPUs (MI300X/MI325X/MI355X) | the patterns will be universal. Related: Central fusion work tracker #36066 (Sequence Parallelism was marked ❓ for ROCm) ## Test plan * `ruff check` and `ruff format` pass on all… |
| [#37110](https://github.com/vllm-project/vllm/pull/37110) | mentioned | 0.6 | Fuse per-group FP8 dynamic quant onto Triton attention kernel | kernel Addresses the "Attention+Quant \| FP8 dynamic per-group" row in #36066. The Triton attention kernel now computes per-group dynamic FP8 scales and quantizes output directly i… |
| [#39952](https://github.com/vllm-project/vllm/pull/39952) | closes_keyword | 0.95 | [Feature] Fused SiLU + Mul + per-token dynamic FP8 quantization (Triton) | Fix the missing fusion entry in #36066. Fills the `kFp8DynamicTokenSym` gap in `fuse_act_quant`. ## Test Plan ## Test Result Test fused op: |
| [#43056](https://github.com/vllm-project/vllm/pull/43056) | closes_keyword | 0.95 | [Perf][Kernel] Fused QK-RMSNorm + mRoPE CUDA kernel for Qwen3-VL | Fixes / part of #43021. Contributes to the broader fusion work tracker #36066. For Qwen3-VL, the current attention forward pass dispatches three separate CUDA kernel launches: q_n |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
