# vllm-project/vllm#39303: [Bug]: aiter.ops.triton.attention.pa_mqa_logits.deepgemm_fp8_paged_mqa_logits_stage1` returns random topk for `context_len > 2048` on ROCm (gfx950), breaks GLM-5.1-FP8 decode

| 字段 | 值 |
| --- | --- |
| Issue | [#39303](https://github.com/vllm-project/vllm/issues/39303) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: aiter.ops.triton.attention.pa_mqa_logits.deepgemm_fp8_paged_mqa_logits_stage1` returns random topk for `context_len > 2048` on ROCm (gfx950), breaks GLM-5.1-FP8 decode

### Issue 正文摘录

## Summary Investigations done with Claude Code on a mi355 mode. On the `rocm/vllm-dev:nightly` image bundled with vLLM `0.19.1rc1.dev83+g83d09d36b`, the aiter sparse-MLA **paged decode** kernel `deepgemm_fp8_paged_mqa_logits_stage1` produces correct top‑k indices for `context_len python repro_pa_mqa_ctx2048.py ``` ## Expected output All `topk_set_match` values near `1.0` (bf16 reference and FP8 kernel should disagree only at precision boundaries, not at entire topk sets). ## Actual output ``` ctx= 1024 topk_set_match=1.0000 ctx= 2048 topk_set_match=1.0000 ctx= 2049 topk_set_match=0.0049 ctx= 3000 topk_set_match=0.0015 ctx= 4096 topk_set_match=0.0039 ctx= 8192 topk_set_match=0.0029 ``` At `ctx >= 2049` the kernel selects essentially random positions — the 0.2–0.5 % match is just the baseline `2048 / ctx` collision rate you would get from sampling uniformly. The *absolute* values it writes are also implausible. Running the same reproducer with ```python finite = torch.isfinite(a) & torch.isfinite(r) print("max_abs_diff:", (a[finite] - r[finite]).abs().max().item()) ``` at `ctx=4096` gives `max_abs_diff ≈ 4.9e34`, i.e. the kernel is not "noisy but close", it is writing garbage float...

## 现有链接修复摘要

#39326 fix: Fallback to torch for context_len > 2048 to bypass aiter kernel bug

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: paged_mqa_logits_stage1` returns random topk for `context_len > 2048` on ROCm (gfx950), breaks GLM-5.1-FP8 decode bug;rocm ## Summary Investigations done with Claude Code on a mi355 mode. On the `rocm/vllm-dev:nightly`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: aiter.ops.triton.attention.pa_mqa_logits.deepgemm_fp8_paged_mqa_logits_stage1` returns random topk for `context_len > 2048` on ROCm (gfx950), breaks GLM-5.1-FP8 decode bug;rocm ## Summary Investigations done with...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: values near `1.0` (bf16 reference and FP8 kernel should disagree only at precision boundaries, not at entire topk sets). ## Actual output ``` ctx= 1024 topk_set_match=1.0000 ctx= 2048 topk_set_match=1.0000 ctx= 2049 top...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: aiter.ops.triton.attention.pa_mqa_logits.deepgemm_fp8_paged_mqa_logits_stage1` returns random topk for `context_len > 2048` on ROCm (gfx950), breaks GLM-5.1-FP8 decode bug;rocm ## Summary Investigations done with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: andom topk for `context_len > 2048` on ROCm (gfx950), breaks GLM-5.1-FP8 decode bug;rocm ## Summary Investigations done with Claude Code on a mi355 mode. On the `rocm/vllm-dev:nightly` image bundled with vLLM `0.19.1rc1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39326](https://github.com/vllm-project/vllm/pull/39326) | closes_keyword | 0.95 | fix: Fallback to torch for context_len > 2048 to bypass aiter kernel bug | Fixes vllm-project/vllm#39303 The aiter deepgemm_fp8_paged_mqa_logits_stage1 kernel returns random results when context_len > 2048. Added a check to use the torch fallback impleme |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
