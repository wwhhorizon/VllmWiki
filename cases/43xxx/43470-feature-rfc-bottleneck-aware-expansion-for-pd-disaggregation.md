# vllm-project/vllm#43470: [Feature]: [RFC] Bottleneck-aware expansion for PD disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#43470](https://github.com/vllm-project/vllm/issues/43470) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [RFC] Bottleneck-aware expansion for PD disaggregation

### Issue 正文摘录

This is an RFC-style feature request for discussion. I have been reading through the recent PD, KV transfer, and offloading work, and it feels like the next missing step is not replacing PD, but making PD deployments more adaptive when one side becomes the dominant bottleneck. ## Summary This proposal does **not** replace PD disaggregation. Instead, it builds on the current PD model and asks whether vLLM should identify the dominant bottleneck at runtime and expand the most effective side first. Concretely, the idea is: - keep the current PD architecture - detect whether runtime pressure is mainly on `prefill`, `decode`, or `decode-side KV capacity` - expand the easiest and most effective side first - reduce user-facing contention before relying on stronger competition inside a fixed topology ## Motivation PD already gives an important separation between prefill and decode pools, and KV transfer / request migration / offloading are all moving in the right direction. But even with PD, deployments still seem mostly statically provisioned. That means it is still easy to end up in situations like: - `prefill` is saturated while `decode` is relatively idle - `decode` is saturated while...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: and offloading work, and it feels like the next missing step is not replacing PD, but making PD deployments more adaptive when one side becomes the dominant bottleneck. ## Summary This proposal does **not** replace PD d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Feature]: [RFC] Bottleneck-aware expansion for PD disaggregation feature request This is an RFC-style feature request for discussion. I have been reading through the recent PD, KV transfer, and offloading work, and it f...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: discussion. I have been reading through the recent PD, KV transfer, and offloading work, and it feels like the next missing step is not replacing PD, but making PD deployments more adaptive when one side becomes the dom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t effective side first. Concretely, the idea is: - keep the current PD architecture - detect whether runtime pressure is mainly on `prefill`, `decode`, or `decode-side KV capacity` - expand the easiest and most effectiv...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y understanding is that those efforts already provide the right building blocks. What seems missing is a policy/runtime layer that decides which side should be expanded first when pressure emerges inside an already disa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
