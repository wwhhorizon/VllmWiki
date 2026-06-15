# vllm-project/vllm#41838: [Bug]: Eagle 2/3 acceptance length regression over time

| 字段 | 值 |
| --- | --- |
| Issue | [#41838](https://github.com/vllm-project/vllm/issues/41838) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | activation;cache;fp8 |
| 症状 |  |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Eagle 2/3 acceptance length regression over time

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Problem Speculative decoding acceptance length (AL) smoothly and monotonically regresses over time when serving models with Eagle/Eagle3 draft models in vLLM 0.17.1. AL never recovers — only a full service restart resets it to the initial high value. The degradation correlates with traffic volume per prompt type — only high-volume prompt types are affected. # Setup * vLLM 0.17.1, v1 engine, async scheduling enabled * 4x H200 GPUs (564GB total), gpu_memory_utilization=0.9 (all models executed with TP=4) * Model ~250GB, leaving ~257GB for KV cache (~5M tokens capacity, ~312K blocks at block_size=16) * KV cache dtype: GPT OSS 120B - BF16 (auto), ~50KB per token, other models uses FP8 * Block size: 16 * Prefix caching enabled * Traffic: ~10-20 RPS * ~60 different prompt types, average ~30K tokens each * Per type: ~27K tokens cacheable (unique to that type), ~3K tokens unique per request * First 4K tokens shared across all types, remaining 23K unique per type * Traffic distribution: 5 types occupy ~50% of traffic, other 55 types share the rest * Average OSL: 40 tokens # Observations 1. Model A (BF16 weights and KV, Eagle2, 4 draft t...

## 现有链接修复摘要

#14464 [Bugfix] EAGLE output norm bug | #14990 [Feature] Enhance EAGLE Architecture with Proper RMS Norms | #42359 Fix/full attention ghost block race

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: bug ### Your current environment ### 🐛 Describe the bug # Problem Speculative decoding acceptance length (AL) smoothly and monotonically regresses over time when serving models with Eagle/Eagle3 draft models in vLLM 0.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: KV cache (~5M tokens capacity, ~312K blocks at block_size=16) * KV cache dtype: GPT OSS 120B - BF16 (auto), ~50KB per token, other models uses FP8 * Block size: 16 * Prefix caching enabled * Traffic: ~10-20 RPS * ~60 di...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: n=0.9 (all models executed with TP=4) * Model ~250GB, leaving ~257GB for KV cache (~5M tokens capacity, ~312K blocks at block_size=16) * KV cache dtype: GPT OSS 120B - BF16 (auto), ~50KB per token, other models uses FP8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: * Model ~250GB, leaving ~257GB for KV cache (~5M tokens capacity, ~312K blocks at block_size=16) * KV cache dtype: GPT OSS 120B - BF16 (auto), ~50KB per token, other models uses FP8 * Block size: 16 * Prefix caching ena...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Eagle 2/3 acceptance length regression over time bug ### Your current environment ### 🐛 Describe the bug # Problem Speculative decoding acceptance length (AL) smoothly and monotonically regresses over time when s...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14464](https://github.com/vllm-project/vllm/pull/14464) | mentioned | 0.45 | [Bugfix] EAGLE output norm bug | ine benchmarks (2.43 vs 2.48 for 5 spec tokens on llama 3.1 8b). * pr #14464: "eagle output norm bug" — merged, fixes return x + residual, none vs return x, residual in eagle mode… |
| [#14990](https://github.com/vllm-project/vllm/pull/14990) | mentioned | 0.45 | [Feature] Enhance EAGLE Architecture with Proper RMS Norms | first pass mechanism largely addresses it (small residual gap). * pr #14990: "enhance eagle architecture with proper rms norms" — merged mar 2025, adds proper norm handling to eag… |
| [#42359](https://github.com/vllm-project/vllm/pull/42359) | closes_keyword | 0.95 | Fix/full attention ghost block race | fix to #41838. ## Test Plan Serve GPT-OSS-120B on 2xH200 [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) and [nvidia/gpt-oss-120b-Eagle3-v3](https://hugging |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
