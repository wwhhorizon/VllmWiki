# vllm-project/vllm#40999: [Feature][FP8] Opt-in `ParallelLMHead` quantization in legacy `Fp8Config` (parity with AWQ-Marlin / GPTQ-Marlin / cpu_wna16)

| 字段 | 值 |
| --- | --- |
| Issue | [#40999](https://github.com/vllm-project/vllm/issues/40999) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;fp8;gemm;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature][FP8] Opt-in `ParallelLMHead` quantization in legacy `Fp8Config` (parity with AWQ-Marlin / GPTQ-Marlin / cpu_wna16)

### Issue 正文摘录

## Summary vLLM's legacy `Fp8Config` cannot quantize `lm_head` (the `ParallelLMHead` projection used by the sampler), even when the on-disk checkpoint stores `lm_head` in block-FP8 format. Several other quantization backends in the codebase already support this via an opt-in `lm_head_quantized` flag — this issue proposes bringing `Fp8Config` to parity, plus the loader-level plumbing that's needed to make it actually work end-to-end. We have a public, reproducible checkpoint and minimal patches for the first two of three required layers, and we're happy to take this through to a PR if there's maintainer interest in scope review first. ## Motivation For a 27B-parameter Qwen3.5-family checkpoint already FP8-quantized with DeepSeek-style block FP8 (`weight_block_size: [128, 128]`, `activation_scheme: dynamic`), `lm_head` remains in BF16. On a 32 GB Blackwell GPU (RTX 5090) this leaves only ~1 GiB of free GPU memory after weight load, which is not enough headroom for: - Triton autotuner scratch for the GDN linear-attention `solve_tril` kernels (the model is a Mamba/GDN hybrid) - Subsequent KV cache block reservation by vLLM Result: engine OOMs at warmup or fails with `No available memo...

## 现有链接修复摘要

#35694 [Core] Support FP8 weight storage in unquantized linear and embedding layers | #41000 [FP8] Add opt-in ParallelLMHead dispatch to Fp8Config | #41365 Add opt-in FP8 vocab embedding support

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Feature][FP8] Opt-in `ParallelLMHead` quantization in legacy `Fp8Config` (parity with AWQ-Marlin / GPTQ-Marlin / cpu_wna16) ## Summary vLLM's legacy `Fp8Config` cannot quantize `lm_head` (the `ParallelLMHead` projectio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature][FP8] Opt-in `ParallelLMHead` quantization in legacy `Fp8Config` (parity with AWQ-Marlin / GPTQ-Marlin / cpu_wna16) ## Summary vLLM's legacy `Fp8Config` cannot quantize `lm_head` (the `ParallelLMHead` projectio...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: F16. On a 32 GB Blackwell GPU (RTX 5090) this leaves only ~1 GiB of free GPU memory after weight load, which is not enough headroom for: - Triton autotuner scratch for the GDN linear-attention `solve_tril` kernels (the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ckpoint stores `lm_head` in block-FP8 format. Several other quantization backends in the codebase already support this via an opt-in `lm_head_quantized` flag — this issue proposes bringing `Fp8Config` to parity, plus th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ]`, `activation_scheme: dynamic`), `lm_head` remains in BF16. On a 32 GB Blackwell GPU (RTX 5090) this leaves only ~1 GiB of free GPU memory after weight load, which is not enough headroom for: - Triton autotuner scratc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35694](https://github.com/vllm-project/vllm/pull/35694) | mentioned | 0.45 | [Core] Support FP8 weight storage in unquantized linear and embedding layers | `mistral.py` - gated on env var `vllm_fp8_lm_head=1` - depends on pr #35694 (`unquantizedlinearmethod.apply()` fp8 support) - doesn't touch `fp8config.get_quant_method` @robertgsh… |
| [#41000](https://github.com/vllm-project/vllm/pull/41000) | mentioned | 0.6 | [FP8] Add opt-in ParallelLMHead dispatch to Fp8Config | [ ] Docs update (`docs/features/quantization/fp8.md`) --- Refs: #40999, #35696 |
| [#41365](https://github.com/vllm-project/vllm/pull/41365) | mentioned | 0.6 | Add opt-in FP8 vocab embedding support | embedding gather kernel (separate PR) --- Refs: #41000, #39931, #40999 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
