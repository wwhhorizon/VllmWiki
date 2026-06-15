# vllm-project/vllm#35409: [RFC]: Worker Controller for warm GPU worker pooling to reduce cold-start latency

| 字段 | 值 |
| --- | --- |
| Issue | [#35409](https://github.com/vllm-project/vllm/issues/35409) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Worker Controller for warm GPU worker pooling to reduce cold-start latency

### Issue 正文摘录

### Motivation. ## Summary This RFC proposes a **Worker Controller** architecture to decouple GPU worker lifecycle from model-specific engine creation in vLLM. Instead of spawning fresh workers per model, we keep a pool of pre-warmed GPU workers (Python + CUDA initialized) and dynamically assign them to engines. Primary goal: reduce cold-start TTFT for dynamic and multi-model serving. Reference docs: https://tangkenyi2001.github.io/docs/category/vllm-worker-controller ## Motivation Today, model startup repeatedly pays for worker process initialization. In dynamic workloads (frequent model changes), this creates avoidable fixed latency and slower time-to-first-token. ## Proposal Add a Worker Controller process that: - maintains a pool of pre-warmed workers, - allocates free workers per engine request, - spawns per-engine API server processes, - supports runtime model load/unload without restarting workers, - releases workers back to the pool on engine deletion. ## Measured Results Representative benchmark (`facebook/opt-125m`, 3 sequential cold-start runs): - **Total TTFT:** `13.16s -> 10.92s` (**-2.24s**, ~17%) - **Engine creation:** `4.88s -> 2.70s` (**~45% reduction**) - **Worke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Controller** architecture to decouple GPU worker lifecycle from model-specific engine creation in vLLM. Instead of spawning fresh workers per model, we keep a pool of pre-warmed GPU workers (Python + CUDA initialized) a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: RFC]: Worker Controller for warm GPU worker pooling to reduce cold-start latency RFC ### Motivation. ## Summary This RFC proposes a **Worker Controller** architecture to decouple GPU worker lifecycle from model-specific...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: FC ### Motivation. ## Summary This RFC proposes a **Worker Controller** architecture to decouple GPU worker lifecycle from model-specific engine creation in vLLM. Instead of spawning fresh workers per model, we keep a p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ntains a pool of pre-warmed workers, - allocates free workers per engine request, - spawns per-engine API server processes, - supports runtime model load/unload without restarting workers, - releases workers back to the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: **Worker Controller** architecture to decouple GPU worker lifecycle from model-specific engine creation in vLLM. Instead of spawning fresh workers per model, we keep a pool of pre-warmed GPU workers (Python + CUDA initi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
