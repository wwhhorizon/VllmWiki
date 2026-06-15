# vllm-project/vllm#30112: [RFC]: Elastic DP Rank Recovery: Graceful Handling of GPU Hardware Failures Without Full Cluster Restart

| 字段 | 值 |
| --- | --- |
| Issue | [#30112](https://github.com/vllm-project/vllm/issues/30112) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;moe |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Elastic DP Rank Recovery: Graceful Handling of GPU Hardware Failures Without Full Cluster Restart

### Issue 正文摘录

## Related Work **Relationship to existing work:** - Issue #27774 provides the **fault detection and coordination framework** - Issue #27866 + PR #28296 provide **exception handling and pause/notify/retry** via multi-tier sentinel architecture - Issue #27908 provides the **EPLB infrastructure and MoE rank recovery (replacement)** - **This RFC** enables **elastic DP rank recovery** when entire processes fail **How #27866 complements this RFC:** - Issue #27866 handles **recoverable exceptions**: When exception occurs → Pause, notify external orchestrator, wait for retry - This RFC handles **unrecoverable process death**: GPU hardware failure (XID 79) → Process dies → Keep survivors alive, rebuild - Together: Complete fault tolerance for both recoverable and unrecoverable failures **Example:** ``` Recoverable exception (#27866): CUDA OOM error → Pause, notify orchestrator, retry with smaller batch Unrecoverable failure (This RFC): GPU 2 XID 79 → DP2 process dies → Elastic recovery with 3 ranks ``` Together, these components provide **complete fault tolerance for MoE serving at scale**. ## 2. Motivation ### 2.1 Current Behavior: Full Cluster Failure on Single GPU Fault When a single G...

## 现有链接修复摘要

#28296 Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : GPU hardware failure (XID 79) → Process dies → Keep survivors alive, rebuild - Together: Complete fault tolerance for both recoverable and unrecoverable failures **Example:** ``` Recoverable exception (#27866): CUDA O...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: re Failures Without Full Cluster Restart RFC ## Related Work **Relationship to existing work:** - Issue #27774 provides the **fault detection and coordination framework** - Issue #27866 + PR #28296 provide **exception h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ms: NCCL watchdog calls std::terminate() └─ Reason: Prevent deadlock (other ranks waiting for rank 2) └─ Reason: Prevent data corruption (partial collective results) ↓ T=4ms: C++ runtime calls std::abort() └─ Sends SIGA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 2.1.2 Current Behavior: Cascade Failure **Example scenario:** - Cluster configuration: 4 DP ranks (DP0-DP3), each with 1 GPU - Event: GPU 2 experiences XID 79 hardware failure - Current behavior: 1. NCCL watchdog in DP2...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: tinel architecture - Issue #27908 provides the **EPLB infrastructure and MoE rank recovery (replacement)** - **This RFC** enables **elastic DP rank recovery** when entire processes fail **How #27866 complements this RFC...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28296](https://github.com/vllm-project/vllm/pull/28296) | mentioned | 0.45 | Milestone 1 of Internal Process-level Fault Tolerance (RFC #27866) | he **fault detection and coordination framework** - issue #27866 + pr #28296 provide **exception handling and pause/notify/retry** via multi-tier sentinel architecture - issue #27… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
