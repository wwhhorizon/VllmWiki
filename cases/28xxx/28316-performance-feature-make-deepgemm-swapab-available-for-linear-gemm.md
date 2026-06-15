# vllm-project/vllm#28316: [Performance][Feature]: make DeepGEMM swapAB available for linear gemm

| 字段 | 值 |
| --- | --- |
| Issue | [#28316](https://github.com/vllm-project/vllm/issues/28316) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance][Feature]: make DeepGEMM swapAB available for linear gemm

### Issue 正文摘录

### Proposal to improve performance In flashinfer we already had fp8_gemm_kernel_swapAB kernel for optimizing Mixture of Experts (MOE) GEMM and Dense GEMM operations [reference 1](https://github.com/flashinfer-ai/flashinfer/tree/main/csrc/nv_internal/tensorrt_llm/deep_gemm), [reference 2](https://github.com/flashinfer-ai/flashinfer/blob/main/csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_gemm_kernel.cuh#L1366), and [reference 3](https://github.com/flashinfer-ai/flashinfer/blob/main/csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_gemm_kernel.cuh#L1493). This kernel improves performance in small batch scenarios by swapping the input order in matrix multiplication. These kernels are currently used for: - MoE operations (exposed via fused_moe module) - Available in the codebase for Dense GEMM but not exposed for linear/dense layers --- Proposed Solution: #### Phase 1: FlashInfer * **Add Python binding to expose linear operations** * Can follow existing `fused_moe` pattern: * Extend current binding or create dedicated binding * Add JIT module generation in `flashinfer/jit/gemm/` * Expose API in `flashinf...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: or linear gemm performance;stale ### Proposal to improve performance In flashinfer we already had fp8_gemm_kernel_swapAB kernel for optimizing Mixture of Experts (MOE) GEMM and Dense GEMM operations [reference 1](https:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Performance][Feature]: make DeepGEMM swapAB available for linear gemm performance;stale ### Proposal to improve performance In flashinfer we already had fp8_gemm_kernel_swapAB kernel for optimizing Mixture of Experts (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ;stale ### Proposal to improve performance In flashinfer we already had fp8_gemm_kernel_swapAB kernel for optimizing Mixture of Experts (MOE) GEMM and Dense GEMM operations [reference 1](https://github.com/flashinfer-ai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 8_blockscale_gemm_kernel.cuh#L1493). This kernel improves performance in small batch scenarios by swapping the input order in matrix multiplication. These kernels are currently used for: - MoE operations (exposed via fu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: el selection heuristics (M threshold-based)** ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
