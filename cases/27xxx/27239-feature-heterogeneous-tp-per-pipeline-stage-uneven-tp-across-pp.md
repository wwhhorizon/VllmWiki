# vllm-project/vllm#27239: [Feature]: Heterogeneous TP per Pipeline Stage (uneven TP across PP)

| 字段 | 值 |
| --- | --- |
| Issue | [#27239](https://github.com/vllm-project/vllm/issues/27239) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda |
| 症状 | build_error |
| 根因提示 | memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Heterogeneous TP per Pipeline Stage (uneven TP across PP)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Goal: Enable different tensor-parallel (TP) sizes per pipeline-parallel (PP) stage so mixed accelerators can run in one pipeline (e.g., per-stage TP = 4,1,2,1). Behavior remains unchanged unless explicitly enabled. Motivation A lot of available hardware is heterogeneous (spot pools, older nodes, new accelerators). Today vLLM assumes uniform TP across all PP stages, which limits deployment on mixed GPU fleets. Supporting per-stage TP would let users combine diverse nodes without sacrificing pipeline parallelism. Scope (initial) • Backward compatible and opt-in. • Focus on CUDA first; performance parity with homogeneous TP is not a goal for v1. • Cross-runtime hops (e.g., CUDA↔ROCm↔XLA) may start with a conservative, staged transfer. User-facing API (opt-in) • Add an optional per-stage TP setting to ParallelConfig (e.g., per_stage_tp_sizes with length = PP size). • Off by default; if not set, current uniform TP behavior is preserved. Design Overview Process groups • Build ragged TP groups per stage (stages with TP=1 get single-rank groups for API parity). • Define a PP “primary” rank per stage (TP rank 0) and form the inter-stage PP group from...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ld let users combine diverse nodes without sacrificing pipeline parallelism. Scope (initial) • Backward compatible and opt-in. • Focus on CUDA first; performance parity with homogeneous TP is not a goal for v1. • Cross-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er-facing API (opt-in) • Add an optional per-stage TP setting to ParallelConfig (e.g., per_stage_tp_sizes with length = PP size). • Off by default; if not set, current uniform TP behavior is preserved. Design Overview P...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ture]: Heterogeneous TP per Pipeline Stage (uneven TP across PP) feature request;stale ### 🚀 The feature, motivation and pitch Goal: Enable different tensor-parallel (TP) sizes per pipeline-parallel (PP) stage so mixed...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: eded, then iterate. Testing plan • Unit: group formation, rank mapping, routing logic, fallbacks. • Integration: small models with per-stage TP like [2,1] and [4,1,2,1]. • Perf sanity: document expected overhead at hete...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e (e.g., per-stage TP = 4,1,2,1). Behavior remains unchanged unless explicitly enabled. Motivation A lot of available hardware is heterogeneous (spot pools, older nodes, new accelerators). Today vLLM assumes uniform TP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
