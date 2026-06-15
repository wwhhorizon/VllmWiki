# vllm-project/vllm#29290: [Performance]: Kimi v2 thinking Performance Uplift Plan on ROCM Platform

| 字段 | 值 |
| --- | --- |
| Issue | [#29290](https://github.com/vllm-project/vllm/issues/29290) |
| 状态 | closed |
| 标签 | performance;rocm;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;moe;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Kimi v2 thinking Performance Uplift Plan on ROCM Platform

### Issue 正文摘录

### Proposal to improve performance ## current status - Kimi v2 thinking num_ heads is 64, but aiter mla backend only support num_heads==8 and 128. - TP8+EP8: The attention mechanism uses the vllm Triton MLA backend, and the MoE group GEMM uses the vllm Triton w4a16 kernel. The precision has been aligned. CUDA Graph is not supported, only Eager mode is available. - There are precision issues with DP2+TP4. https://github.com/ROCm/aiter/issues/1455 ## Uplift Plan - [x] Fix the bugs of the Kimiv2 Thinking Model on the ROCm platform. - [ ] Integrate high-performance Triton kernels supporting head_num = 8/64 from aiter. - [ ] Integrate high-performance w4a16 Triton kernels from aiter. - [ ] Support full graph mode and support shared experts multi streams overlap - [ ] Support DP+EP (Data Parallelism + Expert Parallelism) .

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: formance ## current status - Kimi v2 thinking num_ heads is 64, but aiter mla backend only support num_heads==8 and 128. - TP8+EP8: The attention mechanism uses the vllm Triton MLA backend, and the MoE group GEMM uses t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Kimi v2 thinking Performance Uplift Plan on ROCM Platform performance;rocm;stale ### Proposal to improve performance ## current status - Kimi v2 thinking num_ heads is 64, but aiter mla backend only suppo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 8+EP8: The attention mechanism uses the vllm Triton MLA backend, and the MoE group GEMM uses the vllm Triton w4a16 kernel. The precision has been aligned. CUDA Graph is not supported, only Eager mode is available. - The...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: A backend, and the MoE group GEMM uses the vllm Triton w4a16 kernel. The precision has been aligned. CUDA Graph is not supported, only Eager mode is available. - There are precision issues with DP2+TP4. https://github.c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ackend, and the MoE group GEMM uses the vllm Triton w4a16 kernel. The precision has been aligned. CUDA Graph is not supported, only Eager mode is available. - There are precision issues with DP2+TP4. https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
