# vllm-project/vllm#35577: [Feature] TRITON_MLA: support FP8 KV cache (needed for SM12.0 / Blackwell)

| 字段 | 值 |
| --- | --- |
| Issue | [#35577](https://github.com/vllm-project/vllm/issues/35577) |
| 状态 | open |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature] TRITON_MLA: support FP8 KV cache (needed for SM12.0 / Blackwell)

### Issue 正文摘录

## Problem The TRITON_MLA backend raises `NotImplementedError` when FP8 KV cache is requested: ```python # triton_mla.py, __init__ if is_quantized_kv_cache(self.kv_cache_dtype): raise NotImplementedError("TritonMLA V1 with FP8 KV cache not yet supported") # triton_mla.py, forward_mqa if self.kv_cache_dtype.startswith("fp8"): raise NotImplementedError("FP8 Triton MLA not yet supported") ``` On SM12.0 (Blackwell — RTX 5080/5090, B100/B200), **TRITON_MLA is the only available MLA backend**: - `FLASHINFER_MLA` requires `qk_nope_head_dim=128`, but models like GLM-4.7-Flash-REAP have `qk_nope_head_dim=192` - `CUTLASS_MLA` requires SM10.x This means FP8 KV cache is completely blocked on Blackwell for these models, even though the base class `MLACommonImpl` already handles FP8 cache writes via `concat_and_cache_mla` (with `_k_scale` quantization in the CUDA kernel) and FlashMLA supports FP8 on other architectures. ## Impact For VRAM-constrained GPUs (e.g. RTX 5080 with 16 GB), FP8 KV cache would **double the usable context length**. Tested with GLM-4.7-Flash-REAP-23B-A3B NVFP4: - BF16 KV cache: ~4,928 tokens max context - FP8 KV cache: ~11,728 tokens max context (2.38×) ## Workaround (not...

## 现有链接修复摘要

#35833 [Bugfix] Fix TRITON_MLA FP8 KV cache decode on Blackwell GPUs

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 11: [Feature] TRITON_MLA: support FP8 KV cache (needed for SM12.0 / Blackwell) stale ## Problem The TRITON_MLA backend raises `NotImplementedError` when FP8 KV cache is requested: ```python # triton_mla.py, __init__ if is_q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Feature] TRITON_MLA: support FP8 KV cache (needed for SM12.0 / Blackwell) stale ## Problem The TRITON_MLA backend raises `NotImplementedError` when FP8 KV cache is requested: ```python # triton_mla.py, __init__ if is_q...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Feature] TRITON_MLA: support FP8 KV cache (needed for SM12.0 / Blackwell) stale ## Problem The TRITON_MLA backend raises `NotImplementedError` when FP8 KV cache is requested: ```python # triton_mla.py, __init__ if is_q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: eature] TRITON_MLA: support FP8 KV cache (needed for SM12.0 / Blackwell) stale ## Problem The TRITON_MLA backend raises `NotImplementedError` when FP8 KV cache is requested: ```python # triton_mla.py, __init__ if is_qua...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n is fragile** — uses `element_size() == 1` heuristic instead of an explicit contract ## Suggested proper implementation The ideal fix would be to handle FP8 inside the Triton decode kernel (`decode_attention_fwd`), sim...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35833](https://github.com/vllm-project/vllm/pull/35833) | closes_keyword | 0.95 | [Bugfix] Fix TRITON_MLA FP8 KV cache decode on Blackwell GPUs | Fixes #35577 ## Test plan - Verified on NVIDIA GB10 (SM 12.1) with GLM-4.7-Flash-NVFP4, `--kv-cache-dtype fp8`, generation throughput ~32–80 tok/s - FP8 vs bfloat16 kernel outpu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
