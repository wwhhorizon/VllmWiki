# vllm-project/vllm#42515: [RFC]: External Elastic EP Scaling

| 字段 | 值 |
| --- | --- |
| Issue | [#42515](https://github.com/vllm-project/vllm/issues/42515) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: External Elastic EP Scaling

### Issue 正文摘录

### Motivation. Elastic Expert Parallelism (EEP) ([RFC #20323](https://github.com/vllm-project/vllm/issues/20323), [PR #34861](https://github.com/vllm-project/vllm/pull/34861)) already provides the worker-side mechanism for changing the EP/DP topology without restarting all workers. The current upstream implementation mainly covers the Ray-managed path, where vLLM owns the creation and removal of `EngineCore` instances during scale-up and scale-down. However, some online serving deployments use externally managed DP ranks: each rank is launched and removed by an external orchestrator, and traffic is routed through an external load balancer. In this mode, vLLM should not create Ray actors for new ranks. Instead, vLLM needs a control path that lets externally launched ranks join the existing EEP transition, while preserving the existing EEP worker-side reconfiguration flow. This RFC proposes adding external EEP scaling support by extending the client-to-engine-core orchestration path. The core EEP worker logic remains shared with the existing implementation. ### Proposed Change This proposal adds an external scaling path for `data_parallel_external_lb`: - Keep the existing EEP worke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: external orchestrator can trigger the transition on each old rank. The important distinction is: - **Existing EEP Ray path**: vLLM creates and removes `EngineCore` instances through Ray. - **External EEP path**: the ext...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: External Elastic EP Scaling RFC ### Motivation. Elastic Expert Parallelism (EEP) ([RFC #20323](https://github.com/vllm-project/vllm/issues/20323), [PR #34861](https://github.com/vllm-project/vllm/pull/34861)) already pr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: path. 7. Existing EEP worker logic transfers expert state, synchronizes KV cache capacity, switches communication groups, and runs EPLB reshuffle. 8. After reconfiguration completes, the external orchestrator can add th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: existing EEP transition, while preserving the existing EEP worker-side reconfiguration flow. This RFC proposes adding external EEP scaling support by extending the client-to-engine-core orchestration path. The core EEP...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC]: External Elastic EP Scaling RFC ### Motivation. Elastic Expert Parallelism (EEP) ([RFC #20323](https://github.com/vllm-project/vllm/issues/20323), [PR #34861](https://github.com/vllm-project/vllm/pull/34861)) alr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
