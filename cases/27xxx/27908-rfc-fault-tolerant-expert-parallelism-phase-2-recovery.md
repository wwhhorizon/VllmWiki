# vllm-project/vllm#27908: [RFC]: Fault-Tolerant Expert parallelism phase 2 (recovery)

| 字段 | 值 |
| --- | --- |
| Issue | [#27908](https://github.com/vllm-project/vllm/issues/27908) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe |
| 症状 | slowdown |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Fault-Tolerant Expert parallelism phase 2 (recovery)

### Issue 正文摘录

### Summary Phase 2 enables automatic recovery from persistent rank failures by integrating Phase 0-1's health monitoring with vLLM's existing scale_elastic_ep() API. When failures persist beyond a threshold, the system automatically triggers scale-down (remove failed ranks) followed by scale-up (restore capacity) to achieve self-healing without manual `intervention.` ### Motivation Problem: Phase 0-1 Leaves System in Degraded State Phase 0-1 (#27774) successfully provides graceful degradation: - Detects failures via per-expert latency monitoring within some number of forward passes - Applies weight penalty to unhealthy experts during EPLB rebalancing - Continues serving with reduced capacity However, critical limitations remain in production: 1. Incomplete traffic blocking. The weight penalty is probabilistic rather than absolute, so failed experts continue to receive traffic. 2. No capacity is restored. Phases 0–1 never recover capacity, so failed ranks remain in the cluster indefinitely. Redundant experts are compensating for these failures. 3. Manual intervention is required to restore full capacity. ### Proposed Change. ### Solution: Automatic Recovery via Elastic Scaling Pha...

## 现有链接修复摘要

#28073 [Core] MoE degrade detection and graceful degradation. (Phase 0 of RFC #27774) | #28281 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | #28291 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | #28296 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [RFC]: Fault-Tolerant Expert parallelism phase 2 (recovery) RFC;stale ### Summary Phase 2 enables automatic recovery from persistent rank failures by integrating Phase 0-1's health monitoring with vLLM's existing scale_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ─┘ ``` #### Track the failed state of each rank ``` @dataclass class EPLBConfig: # ... existing EPLB fields ... # Phase 0-1 (from #27774) health_check_enabled: bool = True health_latency_threshold: float = 3.0 # 3x medi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Fault-Tolerant Expert parallelism phase 2 (recovery) RFC;stale ### Summary Phase 2 enables automatic recovery from persistent rank failures by integrating Phase 0-1's health monitoring with vLLM's existing scale_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: sfully provides graceful degradation: - Detects failures via per-expert latency monitoring within some number of forward passes - Applies weight penalty to unhealthy experts during EPLB rebalancing - Continues serving w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ggers scale-down (remove failed ranks) followed by scale-up (restore capacity) to achieve self-healing without manual `intervention.` ### Motivation Problem: Phase 0-1 Leaves System in Degraded State Phase 0-1 (#27774)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28073](https://github.com/vllm-project/vllm/pull/28073) | mentioned | 0.6 | [Core] MoE degrade detection and graceful degradation. (Phase 0 of RFC #27774) | stribution (Phase 1 RFC #27774) and expert auto-recovery (Phase 2 RFC #27908). ### What's Implemented: - Per-expert latency tracking in EPLB sliding window - Health detection algo… |
| [#28281](https://github.com/vllm-project/vllm/pull/28281) | mentioned | 0.6 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | believe that **this implementation is compatible with RFC #27774 and #27908** to isolate fault ranks through scale_down. This implementation establishes the overall fault toleranc… |
| [#28291](https://github.com/vllm-project/vllm/pull/28291) | mentioned | 0.6 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | believe that **this implementation is compatible with RFC #27774 and #27908** to isolate fault ranks through scale_down. This implementation establishes the overall fault toleranc… |
| [#28296](https://github.com/vllm-project/vllm/pull/28296) | mentioned | 0.6 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | believe that **this implementation is compatible with RFC #27774 and #27908** to isolate fault ranks through scale_down. This implementation establishes the overall fault toleranc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
