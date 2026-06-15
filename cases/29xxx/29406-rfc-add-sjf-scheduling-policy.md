# vllm-project/vllm#29406: [RFC]: Add SJF Scheduling Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#29406](https://github.com/vllm-project/vllm/issues/29406) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add SJF Scheduling Policy

### Issue 正文摘录

--- authors: - Chen Jie @HiC4Sh1e - Jiahong Zhang @JiahongZhang-Work - Weichen Zhu @Pr0Wh1teGivee - Zhexu Liu @henryxuxu0716 --- ### Motivation. ### Limitations of Current vLLM Scheduling Strategies vLLM primarily employs **First-Come-First-Served (FCFS)** or **priority-based scheduling** (e.g., token-budget or deadline-aware strategies). While simple to implement, these approaches exhibit critical limitations in production inference workloads: | Problem | Impact | |--------------------------|------------------------------------------------------------------------------------------------------| | **High Tail Latency** | Large requests (e.g., 32K-token documents) monopolize resources, causing severe head-of-line blocking. Small requests (e.g., 100-token chat responses) experience order-of-magnitude latency spikes despite their inherent speed potential. | | **Throughput-Latency Imbalance** | FCFS's strict arrival-order fairness forces small requests to wait behind decoding phases of large requests. This wastes compute resources that could otherwise process multiple short jobs concurrently, degrading system-wide throughput by 30-50% in mixed-workload benchmarks. | | **SLO Violations*...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Add SJF Scheduling Policy RFC;stale --- authors: - Chen Jie @HiC4Sh1e - Jiahong Zhang @JiahongZhang-Work - Weichen Zhu @Pr0Wh1teGivee - Zhexu Liu @henryxuxu0716 --- ### Motivation. ### Limitations of Current vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ---------------------------------------------------------| | **High Tail Latency** | Large requests (e.g., 32K-token documents) monopolize resources, causing severe head-of-line blocking. Small requests (e.g., 100-token...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: * - Accepts multi-dimensional parameters (e.g., length, wait time) with configurable weights - Computes final weighted score: `Score = weight₁ * score₁ + weight₂ * score₂ + ⋯ + weightₙ * scoreₙ` (1) - Each parameter's c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n documents) monopolize resources, causing severe head-of-line blocking. Small requests (e.g., 100-token chat responses) experience order-of-magnitude latency spikes despite their inherent speed potential. | | **Through...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: orporating **queue waiting time** alongside job length into scheduling decisions. ## 2. Implementation Requirements As a queue sorting strategy, SJF must dynamically order requests during insertion and extraction based...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
