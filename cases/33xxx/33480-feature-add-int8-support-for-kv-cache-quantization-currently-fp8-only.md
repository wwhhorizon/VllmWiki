# vllm-project/vllm#33480: [Feature]: Add INT8 Support for KV Cache Quantization (Currently FP8-Only)

| 字段 | 值 |
| --- | --- |
| Issue | [#33480](https://github.com/vllm-project/vllm/issues/33480) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cache;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add INT8 Support for KV Cache Quantization (Currently FP8-Only)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi vLLM team, First, thanks for the amazing work on vLLM—it's been a game-changer for high-performance LLM serving! I'm writing to request a feature addition that would greatly benefit users with diverse hardware setups: support for INT8 quantization in KV Cache, alongside the existing FP8 implementation. Current Behavior As of vLLM version 0.4.0 (and confirmed in latest main branch), KV Cache quantization only supports FP8 (e.g., via quantization="fp8" in LLMEngine). While FP8 offers advantages for newer hardware (like NVIDIA H100), it lacks compatibility with older or mainstream GPUs (e.g., A100, RTX 4090, or cloud instances like AWS g5), which either don't support FP8 natively or incur significant overhead when emulating it. Why INT8 Support is Needed Hardware Accessibility: FP8 requires SM9.0+ GPUs (H100+), but many production environments still use A100 (SM8.0) or consumer-grade cards. INT8 is universally supported across all modern NVIDIA GPUs (since Pascal architecture) and avoids FP8 emulation penalties. Example: On an A100, forcing FP8 for KV Cache may degrade performance by 10–20% due to software emulation, while INT8 would run nat...

## 现有链接修复摘要

#33495 [Feature] Support 'int8' in CacheConfig validation

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: LLMEngine). While FP8 offers advantages for newer hardware (like NVIDIA H100), it lacks compatibility with older or mainstream GPUs (e.g., A100, RTX 4090, or cloud instances like AWS g5), which either don't support FP8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Add INT8 Support for KV Cache Quantization (Currently FP8-Only) feature request ### 🚀 The feature, motivation and pitch Hi vLLM team, First, thanks for the amazing work on vLLM—it's been a game-changer for hi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: entation. Current Behavior As of vLLM version 0.4.0 (and confirmed in latest main branch), KV Cache quantization only supports FP8 (e.g., via quantization="fp8" in LLMEngine). While FP8 offers advantages for newer hardw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: alongside the existing FP8 implementation. Current Behavior As of vLLM version 0.4.0 (and confirmed in latest main branch), KV Cache quantization only supports FP8 (e.g., via quantization="fp8" in LLMEngine). While FP8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in frameworks like Hugging Face Transformers (quantize_kv_cache=True in model.generate()). Use Case Demand: Many users (myself included) deploy vLLM on cost-effective cloud instances (e.g., AWS p4d) where FP8 isn't viab...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33495](https://github.com/vllm-project/vllm/pull/33495) | mentioned | 0.6 | [Feature] Support 'int8' in CacheConfig validation | ig`. This is the **configuration layer support** required for Issue #33480 ([Feature]: Add INT8 Support for KV Cache Quantization). Currently, `int8` is supported by many kernels… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
