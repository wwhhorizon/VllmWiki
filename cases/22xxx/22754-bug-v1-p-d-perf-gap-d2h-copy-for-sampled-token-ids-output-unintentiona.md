# vllm-project/vllm#22754: [Bug]: [V1][P/D] Perf Gap D2H copy for sampled token ids (output) unintentionally block all other copy operations from other CUDA streams for KV transfers

| 字段 | 值 |
| --- | --- |
| Issue | [#22754](https://github.com/vllm-project/vllm/issues/22754) |
| 状态 | closed |
| 标签 | bug;performance;stale;v1 |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1][P/D] Perf Gap D2H copy for sampled token ids (output) unintentionally block all other copy operations from other CUDA streams for KV transfers

### Issue 正文摘录

## Your current environment vLLM v.0.10.0 in a disagg setup, using a vendor internal KV connector implementation. ## Issue Currently, in a P/D disagg environment, other than the normal model forward execution on the default main CUDA stream, there would be other KV saving/loading operations (mostly H2D, D2H) running in their own CUDA streams to avoid interleaving with the model forward execution. However, we observed that when the gpu model runner runs in default CUDA stream, the blocking copy operation such like `valid_sampled_token_ids = sampled_token_ids.tolist()` would block other copy operations scheduled to run in other CUDA streams even when copy engine is idle. This has caused unexpected KV injection delay, which regressed TTIT/TTFT for a disagg setup. ## Reproduce We have created a simple reproduce script to generate a similar behavior: - Main thread: run some gpu ops on the default stream and followed up by a `tolist` copy. - Second thread: run some copy operations on some other stream, in parallel with the default stream. We observed that as long as the main thread is running in the default cuda stream, it would block other copy operations from the second thread. From t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: //github.com/vllm-project/vllm/pull/22760. Replace `tolist` with an explicit non-blocking D2H for sampled token ids followed up an explicit CUDA event synchronization. cc @WoosukKwon @simon-mo @LucasWilkinson performanc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 1][P/D] Perf Gap D2H copy for sampled token ids (output) unintentionally block all other copy operations from other CUDA streams for KV transfers bug;performance;stale;v1 ## Your current environment vLLM v.0.10.0 in a d...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ed KV injection delay, which regressed TTIT/TTFT for a disagg setup. ## Reproduce We have created a simple reproduce script to generate a similar behavior: - Main thread: run some gpu ops on the default stream and follo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ids (output) unintentionally block all other copy operations from other CUDA streams for KV transfers bug;performance;stale;v1 ## Your current environment vLLM v.0.10.0 in a disagg setup, using a vendor internal KV conn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ## Issue Currently, in a P/D disagg environment, other than the normal model forward execution on the default main CUDA stream, there would be other KV saving/loading operations (mostly H2D, D2H) running in their own CU...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
