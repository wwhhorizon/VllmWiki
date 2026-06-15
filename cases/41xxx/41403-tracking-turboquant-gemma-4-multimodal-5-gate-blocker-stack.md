# vllm-project/vllm#41403: [Tracking] TurboQuant + Gemma 4 multimodal: 5-gate blocker stack

| 字段 | 值 |
| --- | --- |
| Issue | [#41403](https://github.com/vllm-project/vllm/issues/41403) |
| 状态 | open |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Tracking] TurboQuant + Gemma 4 multimodal: 5-gate blocker stack

### Issue 正文摘录

# [Tracking] TurboQuant KV cache + Gemma 4 31B (multimodal) — full blocker stack ## Summary Trying to enable TurboQuant KV cache compression (`turboquant_4bit_nc`) on Gemma 4 31B FP8 (the multimodal `Gemma4ForConditionalGeneration` variant) on consumer Blackwell hardware (4× RTX 5060 Ti, sm_120, TP=4). Walking through the failure modes systematically, there are **5 distinct gates** that block this configuration today on `main`. Filing this as a tracking/discussion issue because the gates compose: fixing #1 reveals #2, fixing #2 reveals #3, etc. Hopefully useful as a roadmap item for anyone working on TurboQuant + multimodal hybrid models. **TL;DR motivation:** on 4× 16 GB consumer Blackwell at TP=4, native 262,144 context with `fp8_per_token_head` doesn't fit (~3.04 GiB needed per GPU vs ~2.15 GiB available at gpu-util 0.97; estimated max 170,560). TurboQuant 4-bit KV would give ~4× compression and unlock native context. So the value proposition is real, not hypothetical. ## Environment - vLLM `0.20.1rc1.dev119+gc74e90b9e.cu132` = `origin/main` @ `39a7f4f` (2026-04-29) + #40391 (lisp19's rework HEAD `c74e90b9`) - 4× RTX 5060 Ti (Blackwell consumer, sm_120), CUDA 13.2, Ubuntu 25.10...

## 现有链接修复摘要

#38479 [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | #39931 [Feature] TurboQuant: support hybrid models and uniform quantization | #40391 Fix Gemma4 KV cache page-size alignment for per-token-head quantization | #40534 [Model] Gemma4: add bidirectional vision attention for sliding layers with window guard | #43577 fix(turboquant): use SDPA prefill fallback on pre-Ampere GPUs

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 7: [Tracking] TurboQuant + Gemma 4 multimodal: 5-gate blocker stack # [Tracking] TurboQuant KV cache + Gemma 4 31B (multimodal) — full blocker stack ## Summary Trying to enable TurboQuant KV cache compression (`turboquant_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Tracking] TurboQuant + Gemma 4 multimodal: 5-gate blocker stack # [Tracking] TurboQuant KV cache + Gemma 4 31B (multimodal) — full blocker stack ## Summary Trying to enable TurboQuant KV cache compression (`turboquant_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: P8 (the multimodal `Gemma4ForConditionalGeneration` variant) on consumer Blackwell hardware (4× RTX 5060 Ti, sm_120, TP=4). Walking through the failure modes systematically, there are **5 distinct gates** that block thi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Tracking] TurboQuant + Gemma 4 multimodal: 5-gate blocker stack # [Tracking] TurboQuant KV cache + Gemma 4 31B (multimodal) — full blocker stack ## Summary Trying to enable TurboQuant KV cache compression (`turboquant_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: t_nc` (chose `_4bit_nc` over `_k8v4` because sm_86 lacks FP8 hardware in Triton — same caveat applies as a guard for users on Ampere) ## The 5 gates (encountered in order) ### Gate 1 — `partial multimodal token full att...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38479](https://github.com/vllm-project/vllm/pull/38479) | mentioned | 0.45 | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | h the current in-tree turboquant api (signature drifted post-merge of #38479). **workaround:** `pip uninstall -y turboquant-vllm`. easy if you know about it; surprising if you don… |
| [#39931](https://github.com/vllm-project/vllm/pull/39931) | mentioned | 0.45 | [Feature] TurboQuant: support hybrid models and uniform quantization | without #39931) ``` ## tagging cc @lisp19 (#40391 author), @jartx (#39931 author), @lucianommartins (#40534/gemma 4 vision-bidi), @mgoin, @woosukkwon — happy to provide any additi… |
| [#40391](https://github.com/vllm-project/vllm/pull/40391) | mentioned | 0.45 | Fix Gemma4 KV cache page-size alignment for per-token-head quantization | no workaround for gate 5 without #39931) ``` ## tagging cc @lisp19 (#40391 author), @jartx (#39931 author), @lucianommartins (#40534/gemma 4 vision-bidi), @mgoin, @woosukkwon — ha… |
| [#40534](https://github.com/vllm-project/vllm/pull/40534) | mentioned | 0.45 | [Model] Gemma4: add bidirectional vision attention for sliding layers with window guard | cc @lisp19 (#40391 author), @jartx (#39931 author), @lucianommartins (#40534/gemma 4 vision-bidi), @mgoin, @woosukkwon — happy to provide any additional diagnostic data. |
| [#43577](https://github.com/vllm-project/vllm/pull/43577) | mentioned | 0.6 | fix(turboquant): use SDPA prefill fallback on pre-Ampere GPUs | fires on SM < 8.0 ## Related issues - Partially addresses Gate 6 of #41403 (TQ + Gemma 4 blocker stack) — the SDPA fallback handles any head_dim, unlike FA2's 256 cap - Related to… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
