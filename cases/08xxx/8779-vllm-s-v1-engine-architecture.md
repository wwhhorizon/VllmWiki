# vllm-project/vllm#8779: vLLM's V1 Engine Architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#8779](https://github.com/vllm-project/vllm/issues/8779) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;kernel;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM's V1 Engine Architecture

### Issue 正文摘录

This issues describes the high level directions that "create LLM Engine V1". We want the design to be as transparent as possible and created this issue to track progress and solicit feedback. Goal: * The new engine will be simple and performant. We found the first iteration of the engine to be simple, the multistep engine to be performant, but we want best of the both worlds. For it to be performat, we want to **minimize GPU idle time**. * The new architecture will be extensible and modular. We found the current codebase becoming difficult to extend and add new features (both production and experimental features) due to the hard tangling of different features. In the new design, features should be compatible with each other. * Tech debts will be cleaned up. We will remove optimizations that compromise code readability. We will also redo ad-hoc implementations to support certain features/models. Non-goals, the following are important but orthogonal: * Optimize GPU time/kernels * Add new features/optimizations * Performance in rare cases The scope is exclusively in the scheduler, memory manager, distributed architecture. We will not touch APIs, models, kernels, and most parts of the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: transparent as possible and created this issue to track progress and solicit feedback. Goal: * The new engine will be simple and performant. We found the first iteration of the engine to be simple, the multistep engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM's V1 Engine Architecture RFC;keep-open This issues describes the high level directions that "create LLM Engine V1". We want the design to be as transparent as possible and created this issue to track progress and s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: will only send the “diffs” * New request: input token IDs & block tables & sampling params, etc. * In-flight request: scheduled request IDs, new block IDs (no token IDs, sampling params, etc.) * Clean up data structures...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: will only send the “diffs” * New request: input token IDs & block tables & sampling params, etc. * In-flight request: scheduled request IDs, new block IDs (no token IDs, sampling params, etc.) * Clean up data structures...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: timizations * Performance in rare cases The scope is exclusively in the scheduler, memory manager, distributed architecture. We will not touch APIs, models, kernels, and most parts of the model runner. Highlights of the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
