# vllm-project/vllm#38171: [Feature]: Add TurboQuant Support for KV Cache Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#38171](https://github.com/vllm-project/vllm/issues/38171) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add TurboQuant Support for KV Cache Quantization

### Issue 正文摘录

# [Feature]: Add TurboQuant Support for KV Cache Quantization ## 🚀 The feature, motivation and pitch **TurboQuant** is a novel online vector quantization method that achieves near-optimal distortion rates for both MSE and inner product preservation, specifically designed for KV cache compression in LLMs. As described in the paper [TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://arxiv.org/pdf/2504.19874), this method provides: - **Provably optimal distortion bounds** within a factor of ~2.7 of information-theoretic limits - **Unbiased inner product estimation** - critical for attention mechanisms - **Online application** - no data-dependent preprocessing required - **Accelerator-friendly design** - suitable for real-time AI workloads - **Significant memory savings** - 4-5× compression while maintaining model performance The paper demonstrates TurboQuant achieving perfect recall on Needle-in-a-Haystack tests at 4× compression and competitive performance on LongBench with just 2.5-3.5 bits per dimension. This would be a valuable addition to vLLM's quantization portfolio, complementing existing scalar methods (FP8, INT4, etc.) with a vector quantizati...

## 现有链接修复摘要

#39008 [Quant] Add TurboQuant 4-bit (tq4) KV cache quantization

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Feature]: Add TurboQuant Support for KV Cache Quantization feature request # [Feature]: Add TurboQuant Support for KV Cache Quantization ## 🚀 The feature, motivation and pitch **TurboQuant** is a novel online vector qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: - **Unbiased inner product estimation** - critical for attention mechanisms - **Online application** - no data-dependent preprocessing required - **Accelerator-friendly design** - suitable for real-time AI workloads - *...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : - **Provably optimal distortion bounds** within a factor of ~2.7 of information-theoretic limits - **Unbiased inner product estimation** - critical for attention mechanisms - **Online application** - no data-dependent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Add TurboQuant Support for KV Cache Quantization feature request # [Feature]: Add TurboQuant Support for KV Cache Quantization ## 🚀 The feature, motivation and pitch **TurboQuant** is a novel online vector qu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: to recognize TurboQuant as a quantized format. #### 5. Implement CUDA/Triton Kernels Develop two key operations: - **Encode kernel**: Quantize K/V tensors to codebook indices for cache storage - **Decode kernel**: Recon...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39008](https://github.com/vllm-project/vllm/pull/39008) | mentioned | 0.6 | [Quant] Add TurboQuant 4-bit (tq4) KV cache quantization | quality/compression tradeoffs ### Related - Consolidates ideas from #38171, #38662, #38280, #38479 (competing TQ PRs, none merged) - Extends #38378 (per-token-head framework) - Pa… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
