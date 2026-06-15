# vllm-project/vllm#33869: [RFC]:DeepSeek-R1 Moe offload

| 字段 | 值 |
| --- | --- |
| Issue | [#33869](https://github.com/vllm-project/vllm/issues/33869) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]:DeepSeek-R1 Moe offload

### Issue 正文摘录

# RFC: CPU Offload for Mixture-of-Experts (MoE) Inference in vLLM PR：https://github.com/vllm-project/vllm/pull/31938 ## Summary This PR proposes a CPU Offload Module for MoE inference in vLLM, enabling a large portion of expert weights and computation to be dynamically offloaded to the CPU while keeping only a small, hot subset of experts cached on GPU. The design supports: - Hybrid GPU–CPU execution - Pinned-memory–based weight streaming - Asynchronous GPU ↔ CPU interaction via callback - AVX / AMX–optimized CPU MoE kernels - Two execution modes: - DBO (Dual Batch Overlap) - Prefetch-based miss expert execution This approach significantly reduces GPU memory footprint and improves scalability for large MoE models with thousands of experts. ## Motivation ### Problem Statement Large MoE models (e.g., Deepseek-like architectures) suffer from GPU memory pressure during inference: - Expert weights dominate memory usage - Only a small subset of experts is active per token Existing approaches typically: - Require all expert weights on GPU - Perform naive CPU fallback with high synchronization overhead ### Key Observations 1. **Expert access is sparse and skewed**: Only a small fraction o...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [RFC]:DeepSeek-R1 Moe offload RFC # RFC: CPU Offload for Mixture-of-Experts (MoE) Inference in vLLM PR：https://github.com/vllm-project/vllm/pull/31938 ## Summary This PR proposes a CPU Offload Module for MoE inference i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n experts being accessed more frequently than others 2. **CPU memory capacity is abundant**: CPU RAM can easily accommodate the full set of expert weights that would otherwise overwhelm GPU memory 3. **Modern CPUs (AVX5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: computation to be dynamically offloaded to the CPU while keeping only a small, hot subset of experts cached on GPU. The design supports: - Hybrid GPU–CPU execution - Pinned-memory–based weight streaming - Asynchronous G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: DBO Mode (Dual Batch Overlap) When the system is in **DBO mode** or in decode/small batch scenarios, the forward pass enters a fully parallel CPU-GPU execution path: - Experts in `copy_map` are asynchronously copied to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: on ### Goals of This RFC - Reduce GPU memory usage without sacrificing throughput - Enable fine-grained expert caching - Overlap GPU compute, CPU compute, and data movement - Integrate cleanly with vLLM's execution mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
