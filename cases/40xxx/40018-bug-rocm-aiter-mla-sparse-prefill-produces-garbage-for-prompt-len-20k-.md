# vllm-project/vllm#40018: [Bug]: `ROCM_AITER_MLA_SPARSE` prefill produces garbage for prompt_len > ~20K tokens on gfx950 (GLM-5.1-FP8)

| 字段 | 值 |
| --- | --- |
| Issue | [#40018](https://github.com/vllm-project/vllm/issues/40018) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `ROCM_AITER_MLA_SPARSE` prefill produces garbage for prompt_len > ~20K tokens on gfx950 (GLM-5.1-FP8)

### Issue 正文摘录

## Summary The investigation and this report was generated with the help of Claude Code. The `ROCM_AITER_MLA_SPARSE` attention backend — the **only** backend available for `glm_moe_dsa` sparse-MLA models on ROCm — silently produces corrupt output when the prefill prompt exceeds approximately 20,000 tokens. This is a **distinct bug** from the decode-path regression reported in #39303 (which was fixed by PR #39509 reverting aiter to v0.1.10.post3). The new bug persists on the fixed nightly and is in the **prefill** path, not the decode path. | | #39303 (decode, FIXED) | This issue (prefill, NEW) | |---|---|---| | **Path** | Decode (paged attention) | Prefill (indexer gather + logits) | | **Kernel** | `deepgemm_fp8_paged_mqa_logits_stage1` | `rocm_fp8_mqa_logits` via `rocm_aiter_mla_sparse.py` | | **Trigger** | Running decode context > 2048 tokens | Prompt (prefill) length > ~20K tokens | | **aiter version** | v0.1.12 only (fixed in v0.1.10.post3) | v0.1.10.post3 — **still broken** | | **Symptom** | Token salad after ~2K generated tokens | Token salad from first generated token | | **Root cause** | aiter kernel regression in v0.1.12 | Missing `skip_kv_gather` + workspace reuse in ROC...

## 现有链接修复摘要

#39509 [ROCm] [AITER] Revert AITER version to v0.1.10.post3

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: `ROCM_AITER_MLA_SPARSE` prefill produces garbage for prompt_len > ~20K tokens on gfx950 (GLM-5.1-FP8) bug;rocm ## Summary The investigation and this report was generated with the help of Claude Code. The `ROCM_AI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ontext > 2048 tokens | Prompt (prefill) length > ~20K tokens | | **aiter version** | v0.1.12 only (fixed in v0.1.10.post3) | v0.1.10.post3 — **still broken** | | **Symptom** | Token salad after ~2K generated tokens | To...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: prefill produces garbage for prompt_len > ~20K tokens on gfx950 (GLM-5.1-FP8) bug;rocm ## Summary The investigation and this report was generated with the help of Claude Code. The `ROCM_AITER_MLA_SPARSE` attention backe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: `ROCM_AITER_MLA_SPARSE` prefill produces garbage for prompt_len > ~20K tokens on gfx950 (GLM-5.1-FP8) bug;rocm ## Summary The investigation and this report was generated with the help of Claude Code. The `ROCM_AI...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: _MLA_SPARSE` attention backend — the **only** backend available for `glm_moe_dsa` sparse-MLA models on ROCm — silently produces corrupt output when the prefill prompt exceeds approximately 20,000 tokens. This is a **dis...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39509](https://github.com/vllm-project/vllm/pull/39509) | mentioned | 0.45 | [ROCm] [AITER] Revert AITER version to v0.1.10.post3 | _aiter_mla_sparse` with no escape hatch. ## additional context - pr #39509 (revert aiter to v0.1.10.post3) fixed the **decode** regression from #39303. that fix is confirmed worki… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
