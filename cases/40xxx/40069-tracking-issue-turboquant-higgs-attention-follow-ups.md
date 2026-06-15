# vllm-project/vllm#40069: [Tracking issue]: TurboQuant/HIGGS Attention follow-ups

| 字段 | 值 |
| --- | --- |
| Issue | [#40069](https://github.com/vllm-project/vllm/issues/40069) |
| 状态 | open |
| 标签 | quantization |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization;triton |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Tracking issue]: TurboQuant/HIGGS Attention follow-ups

### Issue 正文摘录

Tracking follow-up work on the TurboQuant/HIGGS KV cache attention backend initially landed in #38479. ### Backend coverage - [x] Expand `flash_attn_varlen_func` to FA3/4, not just FA2 - [ ] Hybrid attention models (e.g. Qwen3.5, mamba+attention, interleaved SWA?) - [ ] MLA support (through a new attention backend?) ### Accuracy - [x] Long-context evals across presets (k8v4, t4nc, k3v4nc, t3nc): RULER, NIAH at 32K–1M, LongBench - [ ] Per-layer sensitivity sweep to inform `--kv-cache-dtype-skip-layers` defaults - [ ] Publish recommended config table (quality vs. compression vs. throughput) based on eval results - [ ] Add new presets as the sweeps suggest (e.g. mixed-bit, per-layer schedules) ### Feature compatibility Things currently disabled or unverified with the TurboQuant backend; enable and test: - [ ] Speculative decoding / Eagle - [ ] KV connector / disaggregated serving (NIXL, LMCache, Mooncake) ### Performance - [ ] CUDA/cutedsl kernels to replace the triton kernels - [ ] Validate AMD performance - [ ] Revisit stream-overlap gating under CUDAGraph - [ ] FP8 decode path parity on Hopper cc @vibhavagarwal5

## 现有链接修复摘要

#38479 [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | #41414 [Bugfix][Attention][TurboQuant] Pad head_dim to power-of-2 for WHT | #41418 [Attention][TurboQuant] Pre-bake Lloyd-Max centroids for common (d, bits) shapes | #41422 [Attention][TurboQuant] Sparse V tile-skip (opt-in) | #41803 [Attention][MLA] Add Triton-fused TurboQuant decode backend | #43577 fix(turboquant): use SDPA prefill fallback on pre-Ampere GPUs | #43747 [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ation Tracking follow-up work on the TurboQuant/HIGGS KV cache attention backend initially landed in #38479. ### Backend coverage - [x] Expand `flash_attn_varlen_func` to FA3/4, not just FA2 - [ ] Hybrid attention model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: erleaved SWA?) - [ ] MLA support (through a new attention backend?) ### Accuracy - [x] Long-context evals across presets (k8v4, t4nc, k3v4nc, t3nc): RULER, NIAH at 32K–1M, LongBench - [ ] Per-layer sensitivity sweep to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Tracking issue]: TurboQuant/HIGGS Attention follow-ups quantization Tracking follow-up work on the TurboQuant/HIGGS KV cache attention backend initially landed in #38479. ### Backend coverage - [x] Expand `flash_attn_v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: / disaggregated serving (NIXL, LMCache, Mooncake) ### Performance - [ ] CUDA/cutedsl kernels to replace the triton kernels - [ ] Validate AMD performance - [ ] Revisit stream-overlap gating under CUDAGraph - [ ] FP8 dec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d `flash_attn_varlen_func` to FA3/4, not just FA2 - [ ] Hybrid attention models (e.g. Qwen3.5, mamba+attention, interleaved SWA?) - [ ] MLA support (through a new attention backend?) ### Accuracy - [x] Long-context eval...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38479](https://github.com/vllm-project/vllm/pull/38479) | mentioned | 0.45 | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | n the turboquant/higgs kv cache attention backend initially landed in #38479. ### backend coverage - [x] expand `flash_attn_varlen_func` to fa3/4, not just fa2 - [ ] hybrid attent… |
| [#41414](https://github.com/vllm-project/vllm/pull/41414) | mentioned | 0.6 | [Bugfix][Attention][TurboQuant] Pad head_dim to power-of-2 for WHT | before opening this PR. The closest references are: - Tracking issue #40069 (TurboQuant follow-ups) — does not list `head_dim` padding. - PR #39890 (erhan1209) adds new "official"… |
| [#41418](https://github.com/vllm-project/vllm/pull/41418) | closes_keyword | 0.95 | [Attention][TurboQuant] Pre-bake Lloyd-Max centroids for common (d, bits) shapes | closed PRs / issues with combinations of `turboquant`, `centroid`, `lloyd-max`, `pre-bake`, `startup`. No existing PR proposes this. Tracking issue #40069 (TurboQuant follow-ups) d |
| [#41422](https://github.com/vllm-project/vllm/pull/41422) | mentioned | 0.6 | [Attention][TurboQuant] Sparse V tile-skip (opt-in) | -skip, attention sparsity, softmax skip} — no matches. Tracking issue #40069 (TurboQuant follow-ups) does not list a sparse-V item. Adjacent perf work: - [#40792](https://github.c… |
| [#41803](https://github.com/vllm-project/vllm/pull/41803) | mentioned | 0.6 | [Attention][MLA] Add Triton-fused TurboQuant decode backend | n-MLA) attention path only. - **Addresses the MLA support item** from #40069 (tracking issue for TurboQuant/HIGGS follow-ups). - **Complementary to #39931** (hybrid model support)… |
| [#43577](https://github.com/vllm-project/vllm/pull/43577) | mentioned | 0.6 | fix(turboquant): use SDPA prefill fallback on pre-Ampere GPUs | SDPA fallback handles any head_dim, unlike FA2's 256 cap - Related to #40069 (TQ tracking issue) - Builds on #39931 (hybrid model support, merged) --- Formatted-by: GitHub Copilot |
| [#43747](https://github.com/vllm-project/vllm/pull/43747) | closes_keyword | 0.95 | [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807) | closed) - #42544 — workspace allocation assertion (open, addressed by #42551) - #41726 — large chunked continuation prefill crash (open) - #40069 — TurboQuant/HIGGS tracking issue |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
