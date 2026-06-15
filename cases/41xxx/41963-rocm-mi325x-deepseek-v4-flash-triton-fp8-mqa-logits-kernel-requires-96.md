# vllm-project/vllm#41963: [ROCm/MI325X] DeepSeek-V4-Flash: Triton fp8_mqa_logits kernel requires 96KB shared memory, MI325X limit is 64KB

| 字段 | 值 |
| --- | --- |
| Issue | [#41963](https://github.com/vllm-project/vllm/issues/41963) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;fp8;kernel;operator;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [ROCm/MI325X] DeepSeek-V4-Flash: Triton fp8_mqa_logits kernel requires 96KB shared memory, MI325X limit is 64KB

### Issue 正文摘录

## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90+g7a576e2c7 (rocm/vllm-dev:nightly, 2026-05-06) - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--enforce-eager` ## Bug At inference time, the first request fails with a Triton shared memory OOM: ``` triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 98304, Hardware limit: 65536. Reducing block sizes or `num_stages` may help. ``` Call stack: ``` rocm_aiter_mla_sparse.py:538 → rocm_fp8_mqa_logits aiter/ops/triton/attention/fp8_mqa_logits.py:53 → _fp8_mqa_logits_kernel ``` ## Root Cause The Triton kernel `_fp8_mqa_logits_kernel` in `aiter/ops/triton/attention/fp8_mqa_logits.py` is configured with block sizes that require **96 KB** of LDS (Local Data Share / shared memory). The AMD MI325X GPU supports a maximum of **64 KB** per workgroup. The PR #40871 was developed and tested exclusively on **MI355X**, which appears to support the larger shared memory configuration required by this kernel. ## Impact DeepSeek-V4-Flash is completely non-functional for inference on MI325X. The model loads correctly but crashes...

## 现有链接修复摘要

#40871 [New Model][ROCm] Add AMD support for DeepSeek V4

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [ROCm/MI325X] DeepSeek-V4-Flash: Triton fp8_mqa_logits kernel requires 96KB shared memory, MI325X limit is 64KB rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev9...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [ROCm/MI325X] DeepSeek-V4-Flash: Triton fp8_mqa_logits kernel requires 96KB shared memory, MI325X limit is 64KB rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [ROCm/MI325X] DeepSeek-V4-Flash: Triton fp8_mqa_logits kernel requires 96KB shared memory, MI325X limit is 64KB rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev9...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vironment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90+g7a576e2c7 (rocm/vllm-dev:nightly, 2026-05-06) - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--k...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--enforce-eager` ## Bug At inference time, the first request fails with a Triton shared memory OOM: ``` triton.runtime.errors...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40871](https://github.com/vllm-project/vllm/pull/40871) | mentioned | 0.45 | [New Model][ROCm] Add AMD support for DeepSeek V4 | e in `aiter` (the aiter library used by vllm rocm). ## related - pr #40871 "add amd support for deepseek v4" (merged 2026-05-05) — tested on mi355x only - issue #41961: `mul_cuda`… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
