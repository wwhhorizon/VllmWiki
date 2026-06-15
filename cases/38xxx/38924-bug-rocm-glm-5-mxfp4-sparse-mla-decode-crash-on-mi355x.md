# vllm-project/vllm#38924: [Bug][ROCm] GLM-5 MXFP4 sparse MLA decode crash on MI355x

| 字段 | 值 |
| --- | --- |
| Issue | [#38924](https://github.com/vllm-project/vllm/issues/38924) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][ROCm] GLM-5 MXFP4 sparse MLA decode crash on MI355x

### Issue 正文摘录

## Summary GLM-5 (GlmMoeDsaForCausalLM) with MXFP4 quantization crashes during the **decode** phase on ROCm MI355x (gfx950) with 8 GPUs. The model loads and prefills successfully, but decode consistently fails with either `ZeroDivisionError` or `Memory access fault`. ## Root Cause GLM-5 has 64 attention heads and 32 sparse indexer heads (`index_n_heads=32`). At TP=8, the MLA decode kernel receives 8 heads per GPU, but AITER's sparse MLA kernels require `num_heads >= 16`: 1. **MLA decode kernel**: `mla_decode_stage1_asm_fwd` only supports `gqa >= 16`. With TP=8, `gqa=8` triggers `RuntimeError: get_heuristic_kernel_mla: cannot get heuristic kernel! gqa:8` 2. **FP8 paged MQA logits (indexer)**: `deepgemm_fp8_paged_mqa_logits_stage1` computes `TileQCount = heads // ChunkQ` with default `ChunkQ=64`. When `heads = 16` requirement for the MLA kernel), a `Memory access fault` persists during decode, suggesting additional issues in the sparse attention indexer's forward_hip path. ## Environment - **GPU**: 8x AMD MI355X (gfx950) - **ROCm**: 7.2.1 - **vLLM**: main branch (latest) - **Model**: GLM-5-MXFP4 (`zai-org/GLM-5-MXFP4` or equivalent Quark checkpoint) - **Config**: `num_attention_head...

## 现有链接修复摘要

#36855 [ROCm] Fix AITER sparse MLA crash for num_heads < 16 (e.g. GLM-5 TP=8)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug][ROCm] GLM-5 MXFP4 sparse MLA decode crash on MI355x rocm ## Summary GLM-5 (GlmMoeDsaForCausalLM) with MXFP4 quantization crashes during the **decode** phase on ROCm MI355x (gfx950) with 8 GPUs. The model loads and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug][ROCm] GLM-5 MXFP4 sparse MLA decode crash on MI355x rocm ## Summary GLM-5 (GlmMoeDsaForCausalLM) with MXFP4 quantization crashes during the **decode** phase on ROCm MI355x (gfx950) with 8 GPUs. The model loads and...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: GLM-5 MXFP4 sparse MLA decode crash on MI355x rocm ## Summary GLM-5 (GlmMoeDsaForCausalLM) with MXFP4 quantization crashes during the **decode** phase on ROCm MI355x (gfx950) with 8 GPUs. The model loads and prefills su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug][ROCm] GLM-5 MXFP4 sparse MLA decode crash on MI355x rocm ## Summary GLM-5 (GlmMoeDsaForCausalLM) with MXFP4 quantization crashes during the **decode** phase on ROCm MI355x (gfx950) with 8 GPUs. The model loads and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: heads=32`). At TP=8, the MLA decode kernel receives 8 heads per GPU, but AITER's sparse MLA kernels require `num_heads >= 16`: 1. **MLA decode kernel**: `mla_decode_stage1_asm_fwd` only supports `gqa >= 16`. With TP=8,...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36855](https://github.com/vllm-project/vllm/pull/36855) | mentioned | 0.45 | [ROCm] Fix AITER sparse MLA crash for num_heads < 16 (e.g. GLM-5 TP=8) | kernel**: head repeat padding from 8->16 (temporary workaround in pr #36855) until aiter supports nhead < 16 natively 2. **indexer mqa logits**: fall back to pytorch reference imp… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
