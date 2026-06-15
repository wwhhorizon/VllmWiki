# vllm-project/vllm#38256: [RFC]: Incremental MoE Expert Offloading — GPU Cache + Async Pipeline

| 字段 | 值 |
| --- | --- |
| Issue | [#38256](https://github.com/vllm-project/vllm/issues/38256) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;quantization;sampling |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Incremental MoE Expert Offloading — GPU Cache + Async Pipeline

### Issue 正文摘录

## Summary Dynamic MoE expert weight offloading for vLLM. Expert weights live in CPU pinned memory; a fixed-size GPU cache holds the hottest experts; LFRU eviction and cross-layer prediction minimize cache misses. Models that exceed GPU VRAM can run on smaller hardware. **PR 1 is open:** [#37190](https://github.com/vllm-project/vllm/pull/37190) (~980 LOC Python, passing CI). This RFC covers the full 3-PR architecture and provides production data from [tinyserve](https://github.com/e1n00r/tinyserve), an independent implementation of the same techniques (30 tok/s decode on 8 GB GPU, 550+ tests). ## Motivation Large MoE models (DeepSeek-V3 671B, Qwen3.5-122B) don't fit in a single GPU. Only a small subset of experts activates per token (e.g., 8 of 256), so most expert weights sit idle. Moving cold experts to CPU and caching hot ones on GPU lets these models run on hardware that would otherwise OOM. ### Prior art in vLLM | PR | What it does | Limitation this RFC addresses | |---|---|---| | [#34535](https://github.com/vllm-project/vllm/pull/34535) (merged) | Static CPU weight offload | No runtime migration — offloaded weights stay on CPU permanently | | [#29941](https://github.com/vllm...

## 现有链接修复摘要

#29941 [offloader] v2: Hide weight onloading latency via prefetching | #31938 moe-offload-fixed | #34535 [Feature][Perf] Support Selective CPU Weight Offloading | #37190 [MoE][Offload] Run MoE models exceeding VRAM via expert CPU offloading with GPU cache (--moe-expert-cache-size)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 8: t weights live in CPU pinned memory; a fixed-size GPU cache holds the hottest experts; LFRU eviction and cross-layer prediction minimize cache misses. Models that exceed GPU VRAM can run on smaller hardware. **PR 1 is o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: ipeline. ## Production data (tinyserve) RTX PRO 2000 8 GB, GPT-OSS-20B MXFP4, 238 cache slots, single-stream decode: | Metric | Result | |---|---| | Decode throughput | 30 tok/s (stable across context lengths) | | vs HF...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: experts; LFRU eviction and cross-layer prediction minimize cache misses. Models that exceed GPU VRAM can run on smaller hardware. **PR 1 is open:** [#37190](https://github.com/vllm-project/vllm/pull/37190) (~980 LOC Pyt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: prediction minimize cache misses. Models that exceed GPU VRAM can run on smaller hardware. **PR 1 is open:** [#37190](https://github.com/vllm-project/vllm/pull/37190) (~980 LOC Python, passing CI). This RFC covers the f...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 6: [RFC]: Incremental MoE Expert Offloading — GPU Cache + Async Pipeline ## Summary Dynamic MoE expert weight offloading for vLLM. Expert weights live in CPU pinned memory; a fixed-size GPU cache holds the hottest experts;...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29941](https://github.com/vllm-project/vllm/pull/29941) | mentioned | 0.45 | [offloader] v2: Hide weight onloading latency via prefetching | oject/vllm/pull/34535) — selective cpu offload (merged, static) - [pr #29941](https://github.com/vllm-project/vllm/pull/29941) — async prefetch handler (merged, pattern for pr 2)… |
| [#31938](https://github.com/vllm-project/vllm/pull/31938) | mentioned | 0.45 | moe-offload-fixed | \| [rfc #33869](https://github.com/vllm-project/vllm/issues/33869) / [#31938](https://github.com/vllm-project/vllm/pull/31938) \| monolithic moe offload (cache + cpu kernels + dbo +… |
| [#34535](https://github.com/vllm-project/vllm/pull/34535) | mentioned | 0.45 | [Feature][Perf] Support Selective CPU Weight Offloading | .com/vllm-project/vllm/pull/37190) — pr 1 implementation (open) - [pr #34535](https://github.com/vllm-project/vllm/pull/34535) — selective cpu offload (merged, static) - [pr #2994… |
| [#37190](https://github.com/vllm-project/vllm/pull/37190) | mentioned | 0.6 | [MoE][Offload] Run MoE models exceeding VRAM via expert CPU offloading with GPU cache (--moe-expert-cache-size) | king, and shared expert overlap work unchanged. **References:** [RFC #38256](https://github.com/vllm-project/vllm/issues/38256) \| [tinyserve](https://github.com/e1n00r/tinyserve)… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
