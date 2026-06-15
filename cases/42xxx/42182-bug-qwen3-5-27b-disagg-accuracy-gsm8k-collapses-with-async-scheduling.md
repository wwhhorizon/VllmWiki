# vllm-project/vllm#42182: [Bug]: Qwen3.5-27B Disagg accuracy gsm8k collapses with async scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#42182](https://github.com/vllm-project/vllm/issues/42182) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-27B Disagg accuracy gsm8k collapses with async scheduling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be applied: - #41628: Support GDN conv-state splits for NIXL - #41869: PD disagg with NIXL Connector: GDN support (Qwen3.5) - #41644: [Feature] Keep HMA enabled for supported KV connectors Without these patches, Qwen3.5 Disagg serving fails earlier because the GDN conv-state transfer path for NIXL is not fully implemented, so the FP8 KV cache correctness issue cannot be reached. ## Summary Qwen/Qwen3.5-27B disagg serving has a severe correctness regression when `--async-scheduling` is enabled. This is **not** the FP8 KV cache issue. The repro uses `--kv-cache-dtype bfloat16`. The issue appears **only** under a larger GSM8K evaluation load. A small 32-question GSM8K sanity run is healthy, but the full 1319-question GSM8K run collapses in accuracy and produces many invalid responses under the same server configuration. ## Setup - Model: `Qwen/Qwen3.5-27B` - Hardware: GB200 - Disagg setup: - Prefill: 1 node, 4 GPUs, TP=1 - Decode: 1 node, 4 GPUs, TP=1 - KV connector: `NixlConnector` - KV cache dtype: `bfloat16` - Prefix caching: disabled - Async...

## 现有链接修复摘要

#41628 Support GDN conv-state splits for NIXL | #41644 [Feature] Keep HMA enabled for supported KV connectors | #41869 PD disagg with NIXL Connector: GDN support (Qwen3.5)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: e GDN conv-state transfer path for NIXL is not fully implemented, so the FP8 KV cache correctness issue cannot be reached. ## Summary Qwen/Qwen3.5-27B disagg serving has a severe correctness regression when `--async-sch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Qwen3.5-27B Disagg accuracy gsm8k collapses with async scheduling bug ### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: heduling bug ### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be applied: - #41628: Support GDN conv-state splits for NIXL - #41...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Qwen3.5-27B Disagg accuracy gsm8k collapses with async scheduling bug ### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Setup - Model: `Qwen/Qwen3.5-27B` - Hardware: GB200 - Disagg setup: - Prefill: 1 node, 4 GPUs, TP=1 - Decode: 1 node, 4 GPUs, TP=1 - KV connector: `NixlConnector` - KV cache dtype: `bfloat16` - Prefix caching: disabled...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41628](https://github.com/vllm-project/vllm/pull/41628) | mentioned | 0.45 | Support GDN conv-state splits for NIXL | g this issue, qwen3.5/gdn nixl disagg support needs to be applied: - #41628: support gdn conv-state splits for nixl - #41869: pd disagg with nixl connector: gdn support (qwen3.5)… |
| [#41644](https://github.com/vllm-project/vllm/pull/41644) | mentioned | 0.45 | [Feature] Keep HMA enabled for supported KV connectors | nixl - #41869: pd disagg with nixl connector: gdn support (qwen3.5) - #41644: [feature] keep hma enabled for supported kv connectors without these patches, qwen3.5 disagg serving… |
| [#41869](https://github.com/vllm-project/vllm/pull/41869) | mentioned | 0.45 | PD disagg with NIXL Connector: GDN support (Qwen3.5) | ds to be applied: - #41628: support gdn conv-state splits for nixl - #41869: pd disagg with nixl connector: gdn support (qwen3.5) - #41644: [feature] keep hma enabled for supporte… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
