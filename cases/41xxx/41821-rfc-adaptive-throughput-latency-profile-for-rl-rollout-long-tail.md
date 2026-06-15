# vllm-project/vllm#41821: [RFC]: Adaptive throughput/latency profile for RL rollout long-tail

| 字段 | 值 |
| --- | --- |
| Issue | [#41821](https://github.com/vllm-project/vllm/issues/41821) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory;speculative_decoding |
| 子分类 | edge_case |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Adaptive throughput/latency profile for RL rollout long-tail

### Issue 正文摘录

# [RFC]: Adaptive throughput/latency profile for RL rollout long-tail ## Motivation. RL rollouts have two clearly distinguishable phases on the same engine: - **Front phase (throughput-bound)**: trainer submits 256–1024 requests at once; batch is large, compute is saturated. MTP / spec decode is **negative-ROI** here — extra `propose() + verify()` FLOPs cost wall time without paying back. - **Tail phase (latency-bound)**: 1–10 long-tail decodes remain; batch is tiny, memory bandwidth is idle. **This is exactly when spec decode pays off** — but today's vLLM forces a single static profile for the whole rollout. The closest existing work: - **#32374** [V1][Spec Decode] Add Dynamic SD — varies `K` (number of draft tokens) per *batch* based on offline-profiled goodput. Fits Full-CG and async scheduling. Already directionally endorsed by maintainers. - **#36657** [RFC]: Dynamic Speculation Length with Confidence-Threshold Early Exit — adapts length per-step via drafter confidence; complementary technique. - **#39359 / #40662** Synthetic Acceptance Rate — measurement infrastructure that lets dynamic-SD policies be evaluated without retraining drafters. - **#25112** [Bug]: Spec decoding i...

## 现有链接修复摘要

#32374 [V1][Spec Decode] Add Dynamic SD | #39359 [Feat] Synthetic Acceptance Rate for Benchmarking

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: engine: - **Front phase (throughput-bound)**: trainer submits 256–1024 requests at once; batch is large, compute is saturated. MTP / spec decode is **negative-ROI** here — extra `propose() + verify()` FLOPs cost wall ti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [RFC]: Adaptive throughput/latency profile for RL rollout long-tail # [RFC]: Adaptive throughput/latency profile for RL rollout long-tail ## Motivation. RL rollouts have two clearly distinguishable phases on the same en...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ic Acceptance Rate — measurement infrastructure that lets dynamic-SD policies be evaluated without retraining drafters. - **#25112** [Bug]: Spec decoding is not disabled at/after configured batch size — same problem sta...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ide scheduler stats already available on every step. 3. **Reuse #32374's dispatch path** when it lands. The toggle proposed here is the `K=0` end of that spectrum; both should converge on the same `BatchDescriptor`-keye...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: speculator.propose()` entirely) instead of just shrinking K. Same mechanism, same constraints, cleaner semantics for the `K=0` edge. ## Proposed Change. ### Scope (intentionally narrow) 1. **Batch-level only**, not per-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32374](https://github.com/vllm-project/vllm/pull/32374) | mentioned | 0.45 | [V1][Spec Decode] Add Dynamic SD | e this rfc is positioned as a boundary case of the dynamic-sd work in #32374 / #36657 / #39359 / #40662, and async-scheduling preservation is an explicit hard constraint shaped by… |
| [#39359](https://github.com/vllm-project/vllm/pull/39359) | mentioned | 0.45 | [Feat] Synthetic Acceptance Rate for Benchmarking | tioned as a boundary case of the dynamic-sd work in #32374 / #36657 / #39359 / #40662, and async-scheduling preservation is an explicit hard constraint shaped by your prior discus… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
