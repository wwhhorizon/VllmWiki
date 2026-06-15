# vllm-project/vllm#38079: [RFC] Redesign enable_return_routed_experts to avoid blocking EngineCore event loop

| 字段 | 值 |
| --- | --- |
| Issue | [#38079](https://github.com/vllm-project/vllm/issues/38079) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;moe;operator;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Redesign enable_return_routed_experts to avoid blocking EngineCore event loop

### Issue 正文摘录

## [RFC] Redesign `enable_return_routed_experts` to avoid blocking EngineCore event loop ### Summary The current `enable_return_routed_experts` implementation uses shared memory + file locks for cross-process data transfer between Worker and Scheduler. When enabled, it introduces per-step GPU→CPU synchronization on Workers and per-completed-request blocking reads on the Scheduler's single-threaded event loop. In DP+EP setups, this causes NCCL collective timeouts. We propose a per-request opt-in model with data flowing through the existing `ModelRunnerOutput` pipeline, eliminating shared memory and file locks entirely. ### Motivation We are using `enable_return_routed_experts` in a reinforcement learning pipeline to capture MoE routing decisions during inference, which are then replayed during training. Our setup: gpt-oss-120B, TP=8, DP=2, EP=16 across 2 nodes. **With the flag enabled, vLLM hangs within 20–60 seconds of sustained inference.** The hang manifests as throughput dropping to 0 with requests stuck "Running", eventually triggering NCCL ALLREDUCE timeouts in the expert parallel group. With the flag disabled, the same workload runs indefinitely. ### Root cause analysis We t...

## 现有链接修复摘要

#39568 [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: [RFC] Redesign enable_return_routed_experts to avoid blocking EngineCore event loop ## [RFC] Redesign `enable_return_routed_experts` to avoid blocking EngineCore event loop ### Summary The current `enable_return_routed_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [RFC] Redesign enable_return_routed_experts to avoid blocking EngineCore event loop ## [RFC] Redesign `enable_return_routed_experts` to avoid blocking EngineCore event loop ### Summary The current `enable_return_routed_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d memory + file locks for cross-process data transfer between Worker and Scheduler. When enabled, it introduces per-step GPU→CPU synchronization on Workers and per-completed-request blocking reads on the Scheduler's sin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d_experts` in a reinforcement learning pipeline to capture MoE routing decisions during inference, which are then replayed during training. Our setup: gpt-oss-120B, TP=8, DP=2, EP=16 across 2 nodes. **With the flag enab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lag is on):** 1. `slot_mapping_attn[:num_tokens].cpu().numpy()` — forces CUDA stream synchronization before the forward pass 2. `save_captured_experts()` — `_device_buffer.cpu().numpy()` (GPU→CPU copy ~2MB) + `fcntl.flo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39568](https://github.com/vllm-project/vllm/pull/39568) | closes_keyword | 0.95 | [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support | Close: #38079 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
