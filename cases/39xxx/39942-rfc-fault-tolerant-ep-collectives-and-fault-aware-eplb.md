# vllm-project/vllm#39942: [RFC]: Fault-Tolerant EP Collectives and Fault-Aware EPLB

| 字段 | 值 |
| --- | --- |
| Issue | [#39942](https://github.com/vllm-project/vllm/issues/39942) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator |
| 症状 | crash |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Fault-Tolerant EP Collectives and Fault-Aware EPLB

### Issue 正文摘录

## Motivation. vLLM's EPLB uses NCCL collectives on the EP process group to aggregate expert load statistics (`all_reduce`), poll buffer readiness (`all_reduce`), and transfer expert weights (`batch_isend_irecv` / PyNCCL send/recv). If any EP rank dies, these NCCL collectives hang indefinitely, taking down the entire server. EPLB today has no notion of which ranks are alive. It computes expert placements and P2P weight transfers assuming all ranks participate. A `batch_isend_irecv` targeting a dead rank will hang. EPLB must be made **fault-aware**: it needs an `active_ranks` mask to exclude dead ranks from expert placement, and a P2P filter to drop send/recv ops targeting dead peers before they reach the transport layer. The existing elastic EP machinery (`vllm/distributed/elastic_ep/`) handles planned scale-up/scale-down but cannot handle unplanned rank failure: the first NCCL collective after a crash hangs before any recovery logic can run. ## Proposed Change. 1. **Fault-tolerant collectives:** Make the collective backend for EP process groups **configurable**. The first supported fault-tolerant backend is [Mooncake](https://github.com/kvcache-ai/Mooncake). When selected, EPLB c...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Proposed Change. 1. **Fault-tolerant collectives:** Make the collective backend for EP process groups **configurable**. The first supported fault-tolerant backend is [Mooncake](https://github.com/kvcache-ai/Mooncake). W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: PState: active_ranks: torch.Tensor # shape (ep_size,), int32, CUDA last_active_ranks: torch.Tensor # snapshot for change detection active_ranks_cpu: torch.Tensor # shape (ep_size,), int32, CPU def has_changed(self) -> b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: vLLM's EPLB uses NCCL collectives on the EP process group to aggregate expert load statistics (`all_reduce`), poll buffer readiness (`all_reduce`), and transfer expert weights (`batch_isend_irecv` / PyNCCL send/recv). I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: gl0b). Recovery is out-of-scope for this RFC. - **Missing experts retrieval**: This RFC assumes that all experts present in the remaining active ranks. Retrieving expert weights from backup storage (e.g. DRAM) will be a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: putes expert placements and P2P weight transfers assuming all ranks participate. A `batch_isend_irecv` targeting a dead rank will hang. EPLB must be made **fault-aware**: it needs an `active_ranks` mask to exclude dead...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
