# vllm-project/vllm#41559: [Bug] DFlash speculative decoding fundamentally incompatible with all KV cache quantization (fp8, turboquant) due to non-causal attention requirement

| 字段 | 值 |
| --- | --- |
| Issue | [#41559](https://github.com/vllm-project/vllm/issues/41559) |
| 状态 | open |
| 标签 | dflash |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;fp8;quantization;triton |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] DFlash speculative decoding fundamentally incompatible with all KV cache quantization (fp8, turboquant) due to non-causal attention requirement

### Issue 正文摘录

## Summary DFlash speculative decoding (introduced in v0.20.0 via `DFlashProposer` / `DFlashQwen3ForCausalLM`) requires non-causal cross-attention for the draft model. We have empirically verified that **every** attention backend in v0.20.0 either rejects non-causal attention entirely OR rejects KV-quant dtypes when non-causal is set. This means DFlash spec decode **cannot** compose with any of `fp8_e5m2`, `fp8_e4m3`, or `turboquant_4bit_nc` — it is locked to `bfloat16` KV cache. On a 24 GiB RTX 3090 with a 27B-class target model, this halves the available KV pool (~28K → ~14K tokens), making DFlash impractical for production long-context use. ## Verified compatibility matrix on v0.20.0 | Backend | Non-causal support | `fp8_e5m2` KV + non-causal | `turboquant_4bit_nc` KV + non-causal | |---|---|---|---| | FLASH_ATTN | Yes | Rejected (`supported_kv_cache_dtypes` excludes fp8 for non-causal path) | Rejected | | FLASHINFER | **No** (rejects non-causal entirely) | N/A | N/A | | TRITON | **No** (rejects non-causal entirely) | N/A | N/A | | FLEX_ATTENTION | Yes | Rejected (no fp8 in non-causal `supported_kv_cache_dtypes`) | Rejected | | TURBOQUANT | N/A | N/A | Hardcoded `causal=True` a...

## 现有链接修复摘要

#42102 [Spec Decode] Allow DFlash drafter to coexist with quantized target KV via independent KV groups + dtype override

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: DFlash speculative decoding fundamentally incompatible with all KV cache quantization (fp8, turboquant) due to non-causal attention requirement dflash ## Summary DFlash speculative decoding (introduced in v0.20.0 via `D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `turboquant_4bit_nc` — it is locked to `bfloat16` KV cache. On a 24 GiB RTX 3090 with a 27B-class target model, this halves the available KV pool (~28K → ~14K tokens), making DFlash impractical for production long-conte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug] DFlash speculative decoding fundamentally incompatible with all KV cache quantization (fp8, turboquant) due to non-causal attention requirement dflash ## Summary DFlash speculative decoding (introduced in v0.20.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: r the draft model. We have empirically verified that **every** attention backend in v0.20.0 either rejects non-causal attention entirely OR rejects KV-quant dtypes when non-causal is set. This means DFlash spec decode *...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: harbor.focuscell.org/infra/vllm-openai:v0.20.0-tq-hybrid-v2`). **Source citations:** - `vllm/v1/spec_decode/dflash.py:192,289` — DFlash mandates `causal=False` for draft cross-attention - `vllm/v1/attention/backends/tur...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42102](https://github.com/vllm-project/vllm/pull/42102) | mentioned | 0.6 | [Spec Decode] Allow DFlash drafter to coexist with quantized target KV via independent KV groups + dtype override | roject/vllm "DFlashAttention get_kv_cache_spec"` — no results - Issue #41559 timeline — 0 cross-referenced PRs ## Testing `tests/v1/core/test_kv_cache_utils.py` (+109 lines): - DF… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
