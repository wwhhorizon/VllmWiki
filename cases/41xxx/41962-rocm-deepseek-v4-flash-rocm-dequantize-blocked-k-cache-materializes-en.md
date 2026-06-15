# vllm-project/vllm#41962: [ROCm] DeepSeek-V4-Flash: rocm_dequantize_blocked_k_cache materializes entire KV cache pool causing OOM during decode

| 字段 | 值 |
| --- | --- |
| Issue | [#41962](https://github.com/vllm-project/vllm/issues/41962) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;fp8;kernel;operator |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [ROCm] DeepSeek-V4-Flash: rocm_dequantize_blocked_k_cache materializes entire KV cache pool causing OOM during decode

### Issue 正文摘录

## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90+g7a576e2c7 (rocm/vllm-dev:nightly, 2026-05-06) - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--gpu-memory-utilization 0.95`, `--max-model-len 98304` ## Bug After loading the model (~236 GiB/GPU), only ~12.74 GiB remains free per GPU. During the decode profiling pass (and during actual inference), `rocm_forward_decode_fallback` calls `rocm_dequantize_blocked_k_cache` which materializes the **entire** SWA KV cache pool as a dense `bfloat16` tensor — regardless of the actual batch size: ``` HIP out of memory. Tried to allocate 13.54 GiB. GPU 0 has a total capacity of 255.98 GiB of which 12.74 GiB is free. ``` ## Root Cause In `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`, `rocm_forward_decode_fallback` (line ~1086): ```python blocked_swa = rocm_dequantize_blocked_k_cache( swa_k_cache, # shape: (ALL_POOL_BLOCKS, block_size, head_bytes) ... ) ``` `rocm_dequantize_blocked_k_cache` allocates `result = torch.empty((num_blocks, block_size, 1, head_dim), dtype=bfloat16)` where `num_blocks` is the full pool (~147k blocks → 13.54 GiB), even...

## 现有链接修复摘要

#40871 [New Model][ROCm] Add AMD support for DeepSeek V4 | #42248 [ROCm] Avoid full KV cache dequant in MLA decode fallback | #42576 [ROCm] Make sparse-MLA decode fallback gather CUDA-graph safe (alt to #42248)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [ROCm] DeepSeek-V4-Flash: rocm_dequantize_blocked_k_cache materializes entire KV cache pool causing OOM during decode rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [ROCm] DeepSeek-V4-Flash: rocm_dequantize_blocked_k_cache materializes entire KV cache pool causing OOM during decode rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: ] DeepSeek-V4-Flash: rocm_dequantize_blocked_k_cache materializes entire KV cache pool causing OOM during decode rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vironment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90+g7a576e2c7 (rocm/vllm-dev:nightly, 2026-05-06) - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--k...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ecode profiling pass (and during actual inference), `rocm_forward_decode_fallback` calls `rocm_dequantize_blocked_k_cache` which materializes the **entire** SWA KV cache pool as a dense `bfloat16` tensor — regardless of...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40871](https://github.com/vllm-project/vllm/pull/40871) | mentioned | 0.45 | [New Model][ROCm] Add AMD support for DeepSeek V4 | kernel path for rocm so the fallback is not needed. ## related - pr #40871 "add amd support for deepseek v4" (merged 2026-05-05) - related issue: #41961 (`mul_cuda` not implemente… |
| [#42248](https://github.com/vllm-project/vllm/pull/42248) | closes_keyword | 0.95 | [ROCm] Avoid full KV cache dequant in MLA decode fallback | Fixes #41962. ## Summary - compact the SWA and extra KV caches to only the physical blocks referenced by the current decode indices before `rocm_dequantize_blocked_k_cache` - rema |
| [#42576](https://github.com/vllm-project/vllm/pull/42576) | closes_keyword | 0.95 | [ROCm] Make sparse-MLA decode fallback gather CUDA-graph safe (alt to #42248) | resolves #41962 with a per-token gather + dequantization that is **also CUDA/HIP-graph-safe**: - New `_dequantize_referenced_tokens(quant_k_cache, indices, ...)` helper that |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
