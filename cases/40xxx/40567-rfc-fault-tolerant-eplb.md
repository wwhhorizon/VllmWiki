# vllm-project/vllm#40567: [RFC]: Fault tolerant EPLB

| 字段 | 值 |
| --- | --- |
| Issue | [#40567](https://github.com/vllm-project/vllm/issues/40567) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Fault tolerant EPLB

### Issue 正文摘录

> **Note:** A related RFC exists: [[External RFC] Fault-Tolerant EP Collectives and Fault-Aware EPLB by Jeffrey Wang](https://docs.google.com/document/d/1SHoh70ld4imhtOVkGDKbzlygyqAdDjSWfZWW5eqHfEg/edit?tab=t.0#heading=h.vibtx8lu5x5u). This issue proposes a different approach for the NIXL EP path that requires no new dependencies. See the [Comparison with Prior RFC](#comparison-with-prior-rfc) section. --- ## Motivation vLLM's EPLB control plane uses three PyTorch distributed collectives on the EP process groups: | Call site | Collective | Group | |-----------|-----------|-------| | `_allreduce_list` ([eplb_state.py#L843](https://github.com/vllm-project/vllm/blob/3461c8b0277f2d1df6c7ea1ec789881c1d01650b/vllm/distributed/eplb/eplb_state.py#L843)) | `torch.distributed.all_reduce` | NCCL `device_group` | | `_all_ranks_result_ready` ([eplb_state.py#L822](https://github.com/vllm-project/vllm/blob/3461c8b0277f2d1df6c7ea1ec789881c1d01650b/vllm/distributed/eplb/eplb_state.py#L822)) | `torch.distributed.all_reduce` | Gloo `cpu_group` | | `NixlEplbCommunicator.execute` ([eplb_communicator.py#L506](https://github.com/vllm-project/vllm/blob/3461c8b0277f2d1df6c7ea1ec789881c1d01650b/vllm/distri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s a different approach for the NIXL EP path that requires no new dependencies. See the [Comparison with Prior RFC](#comparison-with-prior-rfc) section. --- ## Motivation vLLM's EPLB control plane uses three PyTorch dist...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: andled by the existing elastic EP recovery path) - Extending to non-NIXL backends in this PR (DeepEP, Mooncake EP can follow once they provide a fault-tolerant weight-transfer communicator and dispatch kernel) ## Compar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ess. If rank 0 dies, the store disappears and the fault-tolerance mechanism stops working. We host the TCPStore on `DPCoordinator` ([`v1/engine/coordinator.py`](https://github.com/vllm-project/vllm/blob/3461c8b0277f2d1d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: When any EP rank dies while one of these is in flight, the collective **blocks indefinitely** and the process group is **permanently poisoned**. All surviving ranks stall. With NIXL EP the data plane (NIXL RDMA P2P) wou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tps://docs.google.com/document/d/1SHoh70ld4imhtOVkGDKbzlygyqAdDjSWfZWW5eqHfEg/edit?tab=t.0#heading=h.vibtx8lu5x5u). This issue proposes a different approach for the NIXL EP path that requires no new dependencies. See th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
