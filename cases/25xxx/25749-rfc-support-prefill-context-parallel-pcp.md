# vllm-project/vllm#25749: [RFC]: Support Prefill Context Parallel (PCP)

| 字段 | 值 |
| --- | --- |
| Issue | [#25749](https://github.com/vllm-project/vllm/issues/25749) |
| 状态 | open |
| 标签 | RFC;keep-open;unstale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Prefill Context Parallel (PCP)

### Issue 正文摘录

### Motivation. A follow-up to add prefill context parallel(PCP) after DCP (PR [#23734](https://github.com/vllm-project/vllm/pull/23734)) to optimize TTFT. In DCP, the KV Cache is partitioned along the sequence dimension into several segments (interleave style), achieving context parallelism during the decode phase. --- --- --- Similarly, PCP will split the entire request along the sequence dimension during the prefill phase and further partitions the KVCache along the sequence dimension. ### Proposed Change. Aside from the attention module, almost all other modules do not involve contextual dependencies and can naturally adapt to context parallelism. In the attention module, we adopt the following strategy to implement PCP (chunked prefill is not considered for now), marked as **red.** First, for the KV, we perform an AllGather op along the sequence dimension within the PCP group to obtain the complete KV values. Then, the kvcache is stored according to the slot_mapping. For attention computation, since we have obtained the complete KV, we only need to carefully design the custom mask and perform normal attention. During the decode phase, modules other than attention involve redu...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ain the complete KV values. Then, the kvcache is stored according to the slot_mapping. For attention computation, since we have obtained the complete KV, we only need to carefully design the custom mask and perform norm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Support Prefill Context Parallel (PCP) RFC;keep-open;unstale ### Motivation. A follow-up to add prefill context parallel(PCP) after DCP (PR [#23734](https://github.com/vllm-project/vllm/pull/23734)) to optimize T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ion into several segments (interleave style), achieving context parallelism during the decode phase. --- --- --- Similarly, PCP will split the entire request along the sequence dimension during the prefill phase and fur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uenced and scaled by the ​​PCP size​​. - **Modification of the attention backend computation logic.** The core attention calculation requires changes to handle the distributed KV Cache across PCP groups. The specific al...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ntion module, almost all other modules do not involve contextual dependencies and can naturally adapt to context parallelism. In the attention module, we adopt the following strategy to implement PCP (chunked prefill is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
