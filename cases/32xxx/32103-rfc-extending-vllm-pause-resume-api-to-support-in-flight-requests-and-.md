# vllm-project/vllm#32103: [RFC]: Extending vLLM Pause/Resume API to support in-flight requests and DPEP scenarios

| 字段 | 值 |
| --- | --- |
| Issue | [#32103](https://github.com/vllm-project/vllm/issues/32103) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Extending vLLM Pause/Resume API to support in-flight requests and DPEP scenarios

### Issue 正文摘录

## Overview This document specifies the design for vLLM's pause/resume API to support online RL weight updates. It covers both single-engine and DPEP (Data-Parallel Expert-Parallel) deployments. **Goals**: 1. Enable zero-downtime weight updates for online RL training 2. Support three pause modes: `abort`, `finish`, `keep` 3. Decouple cache management from pause/resume operations 4. Work seamlessly in both single-engine and multi-engine DPEP setups **Key Innovation**: The `keep` mode pauses the scheduler loop while preserving request state, enabling fast weight updates with minimal disruption. --- ## Mental Model: System Architecture ### Three Layers ``` ┌─────────────────────────────────────────────────┐ │ CLIENT │ │ Concerns: finish reasons, partial outputs │ └─────────────────────────────────────────────────┘ │ ▼ ┌─────────────────────────────────────────────────┐ │ FRONTEND (AsyncLLM) │ │ - Request admission control │ │ - abort/finish modes operate here │ └─────────────────────────────────────────────────┘ │ ▼ ┌─────────────────────────────────────────────────┐ │ SCHEDULER (EngineCore) │ │ - Busy loop: schedule() → execute() → update() │ │ - keep mode pauses this loop │ │ - run...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Extending vLLM Pause/Resume API to support in-flight requests and DPEP scenarios RFC ## Overview This document specifies the design for vLLM's pause/resume API to support online RL weight updates. It covers both...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: in-flight requests and DPEP scenarios RFC ## Overview This document specifies the design for vLLM's pause/resume API to support online RL weight updates. It covers both single-engine and DPEP (Data-Parallel Expert-Paral...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: st weight updates with minimal disruption. --- ## Mental Model: System Architecture ### Three Layers ``` ┌─────────────────────────────────────────────────┐ │ CLIENT │ │ Concerns: finish reasons, partial outputs │ └────...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cept: Three Pause Modes ### Mode: `abort` **What happens**: - Frontend blocks new requests - Abort in-flight requests immediately - Return partial outputs with `finish_reason="abort"` **Client impact**: Client-aware (mu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: RL weight updates. It covers both single-engine and DPEP (Data-Parallel Expert-Parallel) deployments. **Goals**: 1. Enable zero-downtime weight updates for online RL training 2. Support three pause modes: `abort`, `fini...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
