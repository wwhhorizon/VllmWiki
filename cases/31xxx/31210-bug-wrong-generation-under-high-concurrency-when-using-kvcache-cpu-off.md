# vllm-project/vllm#31210: [Bug]: Wrong Generation Under High Concurrency When Using KVCache CPU Offload (vLLM 0.13.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#31210](https://github.com/vllm-project/vllm/issues/31210) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cache |
| 症状 | mismatch;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wrong Generation Under High Concurrency When Using KVCache CPU Offload (vLLM 0.13.0)

### Issue 正文摘录

### Your current environment **Environment** - vLLM version: 0.13.0 - Deployment mode: Standalone, single h100 GPU - Model: meta-llama/Llama-3.1-8B-Instruct - Attention backend: FlashAttention - KV offload: CPU offload via OffloadingConnector ### 🐛 Describe the bug **Description** When deploying vLLM 0.13.0 in standalone mode on a single h100 GPU, enabling the kvcache cpu offload leads to incorrect and nondeterministic generation results under high concurrency. Specifically, under load, the KV cache blocks restored from CPU memory appear to occasionally contain corrupted or incorrect data, which causes the model to generate wrong or even garbled responses. This issue is reproducible across multiple models, and I use meta-llama/Llama-3.1-8B-Instruct as a representative example. To ensure determinism and reproducibility, VLLM_BATCH_INVARIANT=1 is enabled. Despite this, when CPU offload is turned on, the same prompt eventually produces different outputs. When offload is disabled, the output is always identical and matches expectations. I am certain that this process is unrelated to preemptions. This issue may be related to #29781 @quanliu1991 ### Steps to Reproduce **1. Start vLLM wi...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: single h100 GPU, enabling the kvcache cpu offload leads to incorrect and nondeterministic generation results under high concurrency. Specifically, under load, the KV cache blocks restored from CPU memory appear to occas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: M 0.13.0) bug;stale ### Your current environment **Environment** - vLLM version: 0.13.0 - Deployment mode: Standalone, single h100 GPU - Model: meta-llama/Llama-3.1-8B-Instruct - Attention backend: FlashAttention - KV o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vironment** - vLLM version: 0.13.0 - Deployment mode: Standalone, single h100 GPU - Model: meta-llama/Llama-3.1-8B-Instruct - Attention backend: FlashAttention - KV offload: CPU offload via OffloadingConnector ### 🐛 Des...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Wrong Generation Under High Concurrency When Using KVCache CPU Offload (vLLM 0.13.0) bug;stale ### Your current environment **Environment** - vLLM version: 0.13.0 - Deployment mode: Standalone, single h100 GPU -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: - vLLM version: 0.13.0 - Deployment mode: Standalone, single h100 GPU - Model: meta-llama/Llama-3.1-8B-Instruct - Attention backend: FlashAttention - KV offload: CPU offload via OffloadingConnector ### 🐛 Describe the bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
