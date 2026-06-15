# vllm-project/vllm#38760: [RFC]: Per-iteration forward pass metrics with accurate engine-level timing

| 字段 | 值 |
| --- | --- |
| Issue | [#38760](https://github.com/vllm-project/vllm/issues/38760) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;moe |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Per-iteration forward pass metrics with accurate engine-level timing

### Issue 正文摘录

### Motivation. **Problem: orchestration systems need per-iteration scheduler telemetry, but vLLM only exposes aggregated Prometheus metrics.** Inference orchestrators (autoscalers, routers, disaggregated serving planners) need to understand the *per-iteration* cost structure of a running vLLM engine: - How many prefill vs decode requests were in each batch? - What was the KV cache depth distribution across decode requests? - How many tokens were computed vs cache-hit? - How long did the GPU forward pass actually take? - How many requests are queued and waiting? Today, vLLM exposes Prometheus gauge/histogram metrics that are **scraped asynchronously** by an external collector. This has fundamental limitations for per-iteration telemetry: 1. **Lossy**: Prometheus scraping is pull-based at a configurable interval. With iteration times of 10-100ms, the scraper can miss 90%+ of iterations. Gauge values reflect only the most recent state at scrape time, not the full distribution. Aggregated metrics inevitably lose information. 2. **Unsynchronized**: The scraper runs on a separate timer from the engine loop. Metrics from different gauges may reflect different iterations, making it impos...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: RFC ### Motivation. **Problem: orchestration systems need per-iteration scheduler telemetry, but vLLM only exposes aggregated Prometheus metrics.** Inference orchestrators (autoscalers, routers, disaggregated serving pl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: truct the sequence of batch compositions over time. An autoscaler cannot build a cost model from Prometheus data because it only sees snapshots. 4. **Latency**: Push-based Prometheus (Pushgateway) uses HTTP, adding late...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rsioned struct emitted once per forward pass: ```python class ForwardPassMetrics(msgspec.Struct, frozen=True): version: int = 1 # can include more info in later versions # Identity worker_id: str = "" # unique engine in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eration telemetry: 1. **Lossy**: Prometheus scraping is pull-based at a configurable interval. With iteration times of 10-100ms, the scraper can miss 90%+ of iterations. Gauge values reflect only the most recent state a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: aggregated Prometheus metrics.** Inference orchestrators (autoscalers, routers, disaggregated serving planners) need to understand the *per-iteration* cost structure of a running vLLM engine: - How many prefill vs decod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
