# vllm-project/vllm#41563: [Bug]: /wake_up fails with "'list' object has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives

| 字段 | 值 |
| --- | --- |
| Issue | [#41563](https://github.com/vllm-project/vllm/issues/41563) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;fp8;kernel;moe;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: /wake_up fails with "'list' object has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives

### Issue 正文摘录

**TL;DR:** On RTX PRO 6000 Blackwell (SM120) with `vllm/vllm-openai:cu129-nightly`, `/sleep` succeeds for every model we tested, but `/wake_up` fails with `AttributeError: 'list' object has no attribute 'zero_'` on every architecture except Gemma-4 (interleaved-SWA). The same bug reproduces on hybrid-SWA (Qwen3.6), hybrid-SWA MoE (Qwen3.6 A3B), DeltaNet+SWA (Qwen3-Coder-Next), and Mamba+attention (Nemotron-Omni). Because Gemma-4 wakes cleanly on the same hardware, image, and quantization scheme, the failure is in the engine pause/resume tensor-restore path — not in any arch-specific kernel. Filing because no upstream issue currently tracks this. --- ### Your current environment **Hardware / image summary:** - GPUs: 4× NVIDIA RTX PRO 6000 Blackwell Server Edition (SM 12.0) - OS: Ubuntu 24.04 - NVIDIA driver: 580 - Container images tested (both reproduce): - `vllm/vllm-openai:cu129-nightly` @ digest `8b49cf3a37eb` (older) - `vllm/vllm-openai:cu129-nightly` @ digest `a749a33d8d05` (newer) - Quantization: `compressed-tensors` (NVFP4) for all five models --- ### 🐛 Describe the bug #### Summary `/wake_up` consistently fails with `AttributeError: 'list' object has no attribute 'zero_'` a...

## 现有链接修复摘要

#40897 [Core] Added Sleep 3 -- Keep weights on GPU, discard KV cache and everything else

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: as no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives **TL;DR:** On RTX PRO 6000 Blackwell (SM120) with `vllm/vllm-openai:cu129-nightly`, `/sleep` succee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: bject has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives **TL;DR:** On RTX PRO 6000 Blackwell (SM120) with `vllm/vllm-openai:cu129-nightly`, `/sleep`...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: at least `model_weights × 2 + working_set`. We initially saw a confusing OOM-kill on Qwen3.6-27B (`memory_max=20 GB`, model ≈ 14 GB) that masked the actual wake-up bug — the container died at sleep time before we could...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 'list' object has no attribute 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives **TL;DR:** On RTX PRO 6000 Blackwell (SM120) with `vllm/vllm-openai:cu129-nightly`,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: e 'zero_'" on hybrid-SWA / Mamba / DeltaNet models (SM120, NVFP4) — only Gemma-4 interleaved-SWA survives **TL;DR:** On RTX PRO 6000 Blackwell (SM120) with `vllm/vllm-openai:cu129-nightly`, `/sleep` succeeds for every m...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40897](https://github.com/vllm-project/vllm/pull/40897) | mentioned | 0.45 | [Core] Added Sleep 3 -- Keep weights on GPU, discard KV cache and everything else | models; flagged as a potentially still-relevant mitigation path. - **#40897** — sleep level 3 pr. tangential — appears to address weight retention, not the `/wake_up` tensor-resto… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
