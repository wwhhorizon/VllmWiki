# vllm-project/vllm#27774: [RFC]:  Fault-Tolerant Expert Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#27774](https://github.com/vllm-project/vllm/issues/27774) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;sampling |
| 症状 | nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]:  Fault-Tolerant Expert Parallelism

### Issue 正文摘录

### Summary This RFC proposes extending vLLM's Expert Parallel Load Balancer (EPLB) with fault tolerance capabilities, enabling automatic detection and recovery from individual expert failures without service interruption. The system continues serving with degraded performance while automatically redistributing load and eventually restarting failed experts using elastic scaling mechanisms. ### Motivation Current EP implementations assume all experts remain healthy throughout deployment. In production environments serving models like DeepSeek-V3 with 256+ experts across multiple GPUs, individual expert failures are inevitable: - Hardware degradation: Specific compute units on a GPU can fail while others continue working - Memory errors: ECC errors affecting individual expert weight storage - Numerical instabilities: Specific experts producing NaN/Inf due to data patterns - Thermal throttling: Localized hotspots affecting expert execution Without fault tolerance, expert failures cause: - Request failures for tokens routed to dead experts - Cascading load imbalances as traffic shifts unpredictably - Service degradation requiring manual intervention Note: Individual expert failures na...

## 现有链接修复摘要

#28073 [Core] MoE degrade detection and graceful degradation. (Phase 0 of RFC #27774) | #28155 [Core] MoE timeout-based error detection and graceful degradation. (Phase 0 of RFC #27774) | #28281 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | #28291 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | #28296 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Fault-Tolerant Expert Parallelism RFC;stale ### Summary This RFC proposes extending vLLM's Expert Parallel Load Balancer (EPLB) with fault tolerance capabilities, enabling automatic detection and recovery from in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Fault-Tolerant Expert Parallelism RFC;stale ### Summary This RFC proposes extending vLLM's Expert Parallel Load Balancer (EPLB) with fault tolerance capabilities, enabling automatic detection and recovery from in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: - Memory errors: ECC errors affecting individual expert weight storage - Numerical instabilities: Specific experts producing NaN/Inf due to data patterns - Thermal throttling: Localized hotspots affecting expert executi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: , individual expert failures are inevitable: - Hardware degradation: Specific compute units on a GPU can fail while others continue working - Memory errors: ECC errors affecting individual expert weight storage - Numeri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: remain healthy throughout deployment. In production environments serving models like DeepSeek-V3 with 256+ experts across multiple GPUs, individual expert failures are inevitable: - Hardware degradation: Specific comput...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28073](https://github.com/vllm-project/vllm/pull/28073) | mentioned | 0.6 | [Core] MoE degrade detection and graceful degradation. (Phase 0 of RFC #27774) | lays the foundation for automatic traffic redistribution (Phase 1 RFC #27774) and expert auto-recovery (Phase 2 RFC #27908). ### What's Implemented: - Per-expert latency tracking… |
| [#28155](https://github.com/vllm-project/vllm/pull/28155) | mentioned | 0.6 | [Core] MoE timeout-based error detection and graceful degradation. (Phase 0 of RFC #27774)  | meout-based error detection and graceful degradation. (Phase 0 of RFC #27774) <!-- markdownlint-disable --> ## Purpose This PR implements a timeout-based health monitoring system… |
| [#28281](https://github.com/vllm-project/vllm/pull/28281) | mentioned | 0.6 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | ow-ups. We believe that **this implementation is compatible with RFC #27774 and #27908** to isolate fault ranks through scale_down. This implementation establishes the overall fau… |
| [#28291](https://github.com/vllm-project/vllm/pull/28291) | mentioned | 0.6 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | ow-ups. We believe that **this implementation is compatible with RFC #27774 and #27908** to isolate fault ranks through scale_down. This implementation establishes the overall fau… |
| [#28296](https://github.com/vllm-project/vllm/pull/28296) | mentioned | 0.6 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | -ups. We believe that **this implementation is compatible with RFC #27774 and #27908** to isolate fault ranks through scale_down. This implementation establishes the overall fault… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
