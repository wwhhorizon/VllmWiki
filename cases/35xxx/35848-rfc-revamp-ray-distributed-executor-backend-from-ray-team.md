# vllm-project/vllm#35848: [RFC]: Revamp Ray Distributed Executor Backend (from Ray team)

| 字段 | 值 |
| --- | --- |
| Issue | [#35848](https://github.com/vllm-project/vllm/issues/35848) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | crash;oom;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Revamp Ray Distributed Executor Backend (from Ray team)

### Issue 正文摘录

## Summary Replace the current `RayExecutor` distributed executor backend which uses Compiled Graph with a new `RayExecutorV2` that launches workers as plain Ray remote actors and follows the `MultiprocExecutor` communication model: ZMQ/SHM-backed MessageQueue for the control plane and NCCL collective communication for the data plane. ## Motivation ### 1. Compiled Graph’s optimizations are no longer the primary bottleneck The Compiled Graph backend was introduced to minimize scheduling overhead by compiling the execution DAG in advance and to provide NCCL abstractions for Ray actor communication. Since then, two developments have removed the need for both: - Async scheduling (v0.15.0) overlaps control plane scheduling with GPU execution, eliminating the per-step scheduling latency that Compiled Graph was designed to hide. - `torch.distributed` already provides NCCL collectives natively. vLLM's `MultiprocExecutor` uses these directly for worker-to-worker communication. Compiled Graph does offer additional optimizations, notably overlapping communication with computation, that are not yet implemented in vLLM. However, these can be achieved independently through `torch.distributed` A...

## 现有链接修复摘要

#41218 fix: convert LogprobsLists to lists for cross node Ray transport (#38602)

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ort bundles: Driver node gets the lowest rank, and same node bundles get contiguous ranks. 3. Compute global and per-node local rank. 4. Classify local vs. remote for MessageQueue creation (more details in the following...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: these can be achieved independently through `torch.distributed` APIs and CUDA stream pipelining without requiring compiled graph. The remaining benefits of Compiled Graph do not justify the stability and maintenance cos...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eplace the current `RayExecutor` distributed executor backend which uses Compiled Graph with a new `RayExecutorV2` that launches workers as plain Ray remote actors and follows the `MultiprocExecutor` communication model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: plane scheduling with GPU execution, eliminating the per-step scheduling latency that Compiled Graph was designed to hide. - `torch.distributed` already provides NCCL collectives natively. vLLM's `MultiprocExecutor` use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lain Ray remote actors and follows the `MultiprocExecutor` communication model: ZMQ/SHM-backed MessageQueue for the control plane and NCCL collective communication for the data plane. ## Motivation ### 1. Compiled Graph...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41218](https://github.com/vllm-project/vllm/pull/41218) | closes_keyword | 0.95 | fix: convert LogprobsLists to lists for cross node Ray transport (#38602) | fix is the RayExecutorV2 migration tracked in #35848 (cc @kouroshHakha @jeffreywang-anyscale). I cannot use V2 on my model class today because of a separate `deepseek_v2.py` loader |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
