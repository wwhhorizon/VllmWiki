# vllm-project/vllm#41204: [RFC]: Expert Weight Backup for Elastic EP

| 字段 | 值 |
| --- | --- |
| Issue | [#41204](https://github.com/vllm-project/vllm/issues/41204) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Expert Weight Backup for Elastic EP

### Issue 正文摘录

### 1. Motivation EPLB (`vllm/distributed/eplb/`) rebalances MoE expert placement every N forward passes via GPU to GPU NCCL P2P. It assumes every source rank is alive and reachable. When a rank dies, the new physical-to-logical map can name an expert whose only live replica was on the dead rank: there is no second source for those weights. This RFC adds a per-node sidecar that mirrors expert weights into host CPU memory, registers them with NIXL, and serves RDMA reads to surviving ranks mid-rebalance. ## 2. Goal - Survive rank loss during EPLB rebalance. - Recover dead-source experts from remote DRAM. - Dormant on the happy path: NCCL P2P remains the primary transport. ### 3. Proposed Change Each client opens ZMQ + NIXL handshakes with **every node's** manager (N managers, one per node). During a rebalance the client may RDMA-read from any subset of them. #### 3.1 CLI / Config ``` --enable-expert-weight-backup # default False; requires --enable-elastic-ep + --enable-eplb --expert-weight-backup-port-base # ZMQ control-plane base, default 35000 ``` `ParallelConfig` gains `enable_expert_weight_backup`, `expert_weight_backup_ib_device`, `expert_weight_backup_port_base`, `expert_weigh...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ## 3.1 CLI / Config ``` --enable-expert-weight-backup # default False; requires --enable-elastic-ep + --enable-eplb --expert-weight-backup-port-base # ZMQ control-plane base, default 35000 ``` `ParallelConfig` gains `en...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC]: Expert Weight Backup for Elastic EP RFC ### 1. Motivation EPLB (`vllm/distributed/eplb/`) rebalances MoE expert placement every N forward passes via GPU to GPU NCCL P2P. It assumes every source rank is alive and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nager's registered region nbytes: int shape: tuple[int, ...] dtype: torch.dtype @dataclass(frozen=True) class ExpertBackupDescriptor: owner_node_rank: int backup_region_base: int # base addr of registered region weight_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nce the client may RDMA-read from any subset of them. #### 3.1 CLI / Config ``` --enable-expert-weight-backup # default False; requires --enable-elastic-ep + --enable-eplb --expert-weight-backup-port-base # ZMQ control-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
