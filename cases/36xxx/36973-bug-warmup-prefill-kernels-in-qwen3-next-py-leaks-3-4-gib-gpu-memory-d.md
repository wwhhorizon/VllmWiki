# vllm-project/vllm#36973: [Bug] _warmup_prefill_kernels in qwen3_next.py leaks ~3.4 GiB GPU memory despite empty_cache()

| 字段 | 值 |
| --- | --- |
| Issue | [#36973](https://github.com/vllm-project/vllm/issues/36973) |
| 状态 | open |
| 标签 |  |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;fp8;kernel;quantization;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] _warmup_prefill_kernels in qwen3_next.py leaks ~3.4 GiB GPU memory despite empty_cache()

### Issue 正文摘录

## Bug Description First, I want to thank the contributors for their efforts. PR #36599 added `_warmup_prefill_kernels()` to warm up Triton autotuned GDN kernels during V1 profiling. The warmup correctly calls `torch.accelerator.empty_cache()` afterward, but ~3.4 GiB of GPU memory is not recovered, dramatically reducing available KV cache. ## Environment - GPU: NVIDIA GeForce RTX 5090 (32 GiB, sm_120) - vLLM: v0.17.1rc1.dev126+gbc2c0c86e (cu130-nightly, 2026-03-13) - Model: Qwen/Qwen3.5-35B-A3B-GPTQ-Int4 (21.05 GiB) - Config: `--quantization gptq_marlin --dtype bfloat16 --kv-cache-dtype fp8 --gpu-memory-utilization 0.90 --enable-prefix-caching` ## Reproduction **Without warmup fix (v0.17.1rc1.dev88, same model, same config):** ``` Available KV cache memory: 5.18 GiB GPU KV cache size: 134,144 tokens ``` **With warmup fix (v0.17.1rc1.dev126, same model, same config):** ``` Available KV cache memory: 1.76 GiB GPU KV cache size: 44,016 tokens ``` The only difference between the two runs is the vLLM version. The warmup fix reduces available KV cache memory by 3.42 GiB (66%), cutting max context from 134K to 44K tokens. ## Root Cause Hypothesis `_warmup_prefill_kernels()` runs `chunk_g...

## 现有链接修复摘要

#36599 [Bugfix] Warm up Triton autotuner for GDN layers during V1 profiling | #37088 [Bugfix] Add FLA_USE_TMA env var to disable TMA in FLA ops (#36973)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: bc2c0c86e (cu130-nightly, 2026-03-13) - Model: Qwen/Qwen3.5-35B-A3B-GPTQ-Int4 (21.05 GiB) - Config: `--quantization gptq_marlin --dtype bfloat16 --kv-cache-dtype fp8 --gpu-memory-utilization 0.90 --enable-prefix-caching...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: afterward, but ~3.4 GiB of GPU memory is not recovered, dramatically reducing available KV cache. ## Environment - GPU: NVIDIA GeForce RTX 5090 (32 GiB, sm_120) - vLLM: v0.17.1rc1.dev126+gbc2c0c86e (cu130-nightly, 2026-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug] _warmup_prefill_kernels in qwen3_next.py leaks ~3.4 GiB GPU memory despite empty_cache() ## Bug Description First, I want to thank the contributors for their efforts. PR #36599 added `_warmup_prefill_kernels()` to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ally reducing available KV cache. ## Environment - GPU: NVIDIA GeForce RTX 5090 (32 GiB, sm_120) - vLLM: v0.17.1rc1.dev126+gbc2c0c86e (cu130-nightly, 2026-03-13) - Model: Qwen/Qwen3.5-35B-A3B-GPTQ-Int4 (21.05 GiB) - Con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] _warmup_prefill_kernels in qwen3_next.py leaks ~3.4 GiB GPU memory despite empty_cache() ## Bug Description First, I want to thank the contributors for their efforts. PR #36599 added `_warmup_prefill_kernels()` to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36599](https://github.com/vllm-project/vllm/pull/36599) | mentioned | 0.45 | [Bugfix] Warm up Triton autotuner for GDN layers during V1 profiling | ption first, i want to thank the contributors for their efforts. pr #36599 added `_warmup_prefill_kernels()` to warm up triton autotuned gdn kernels during v1 profiling. the warmu… |
| [#37088](https://github.com/vllm-project/vllm/pull/37088) | closes_keyword | 0.95 | [Bugfix] Add FLA_USE_TMA env var to disable TMA in FLA ops (#36973) | Fixes #36973 which reports that `_warmup_prefill_kernels()` during V1 profiling leaks ~3.4 GiB GPU memory on RTX 5090, reducing KV cache from ~134K to ~44K tokens. ### Root Caus |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
