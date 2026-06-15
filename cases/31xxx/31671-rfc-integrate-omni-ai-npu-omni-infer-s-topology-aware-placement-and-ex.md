# vllm-project/vllm#31671: [RFC]: Integrate omni-ai-npu/omni-infer's Topology-Aware Placement and Execution Optimizations into vLLM EPLB

| 字段 | 值 |
| --- | --- |
| Issue | [#31671](https://github.com/vllm-project/vllm/issues/31671) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Integrate omni-ai-npu/omni-infer's Topology-Aware Placement and Execution Optimizations into vLLM EPLB

### Issue 正文摘录

### Motivation. As Mixture-of-Experts (MoE) models scale, the efficiency of Expert Parallelism Load Balancing (EPLB) becomes a bottleneck. Based on our analysis of the current vLLM architecture and our experience with OmniInfer (https://github.com/omni-ai-npu/omni-infer), we have identified three key areas for optimization within the existing EPLB modules: Placement Algorithm: The current default policy (deepseek-eplb) does not fully exploit hardware topology awareness (e.g., NVLink vs. PCIe bandwidth differences). Initialization Flexibility: Currently, EplbState defaults to Round-Robin initialization. Users lack the interface to inject a pre-calculated or specific initial expert layout (e.g., from a file). Execution Efficiency: The instruction scheduling for expert movement (rebalance_execute.py) can be optimized to reduce bus contention. Furthermore, calculating the schedule in Python during the inference step introduces overhead. ### Proposed Change. The EPLB module in Omniinfer is called omni_placement. We propose a modular integration plan from omni_placement that respects the current vLLM architecture (Policy -> State -> Execution). 2.1. Policy Module: Register OmniPlacement...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: and maximize bandwidth utilization. Proposal B (High-Performance Solver Backend): OmniInfer utilizes a C++ based host-side scheduler for efficient activation data collection and algorithm calculation. We propose porting...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: stale ### Motivation. As Mixture-of-Experts (MoE) models scale, the efficiency of Expert Parallelism Load Balancing (EPLB) becomes a bottleneck. Based on our analysis of the current vLLM architecture and our experience...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Mixture-of-Experts (MoE) models scale, the efficiency of Expert Parallelism Load Balancing (EPLB) becomes a bottleneck. Based on our analysis of the current vLLM architecture and our experience with OmniInfer (https://g...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lack the interface to inject a pre-calculated or specific initial expert layout (e.g., from a file). Execution Efficiency: The instruction scheduling for expert movement (rebalance_execute.py) can be optimized to reduce...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Optimizations into vLLM EPLB RFC;unstale ### Motivation. As Mixture-of-Experts (MoE) models scale, the efficiency of Expert Parallelism Load Balancing (EPLB) becomes a bottleneck. Based on our analysis of the current vL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
