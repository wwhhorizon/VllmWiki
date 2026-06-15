# vllm-project/vllm#43475: [Feature]: Add SpectralQuant KV Cache Compression (builds on TurboQuant #38479)

| 字段 | 值 |
| --- | --- |
| Issue | [#43475](https://github.com/vllm-project/vllm/issues/43475) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;kernel;quantization;triton |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Add SpectralQuant KV Cache Compression (builds on TurboQuant #38479)

### Issue 正文摘录

## 🚀 The feature, motivation and pitch **SpectralQuant** is a KV cache compression method that improves on TurboQuant (merged in #38479) by exploiting a universal structural property of transformer attention: across six models in four architecture families, key vectors concentrate signal in only **3–4% of the head dimension**. By identifying these dimensions via a one-time 15-second calibration (PCA on a small sample), SpectralQuant applies error correction only where it matters and skips it on the remaining ~96% noise dimensions — achieving better quality *and* better compression simultaneously. **Paper:** "3% Is All You Need: Breaking TurboQuant's Compression Limit via Spectral Structure" — submitted to NeurIPS 2026, arXiv pending. Code: https://github.com/Dynamis-Labs/spectralquant ### Headline results (from paper, on NVIDIA B200) | Metric | SpectralQuant | TurboQuant | Delta | |---|---|---|---| | Cosine similarity (Qwen 2.5-14B) | 0.9485 | 0.9226 | +2.59 pp | | Compression ratio | 5.95× | 5.02× | +18.6% | | Latency (512 tokens) | 0.257 ms/step | 0.566 ms/step | 2.2× faster | | Perplexity (Qwen 7B) | 7.51 | 7.51 | neutral | ### Key findings 1. **Universal low-rank structure** —...

## 现有链接修复摘要

#38479 [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Add SpectralQuant KV Cache Compression (builds on TurboQuant #38479) feature request ## 🚀 The feature, motivation and pitch **SpectralQuant** is a KV cache compression method that improves on TurboQuant (merg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: structural property of transformer attention: across six models in four architecture families, key vectors concentrate signal in only **3–4% of the head dimension**. By identifying these dimensions via a one-time 15-sec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing a universal structural property of transformer attention: across six models in four architecture families, key vectors concentrate signal in only **3–4% of the head dimension**. By identifying these dimensions via a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Add SpectralQuant KV Cache Compression (builds on TurboQuant #38479) feature request ## 🚀 The feature, motivation and pitch **SpectralQuant** is a KV cache compression method that improves on TurboQuant (merg...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: k once available - [ ] Draft implementation design (calibration storage, Triton kernel approach) ## 🔧 Proposed integration SpectralQuant builds directly on the TurboQuant backend (#38479). The main design questions I'd...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38479](https://github.com/vllm-project/vllm/pull/38479) | mentioned | 0.45 | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | reference for stateless compression at serve time? ## 📎 related - #38479 — turboquant merged pr (direct dependency) - #38171 — original turboquant feature request - turboquant pape |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
