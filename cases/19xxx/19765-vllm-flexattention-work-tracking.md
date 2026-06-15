# vllm-project/vllm#19765: Vllm + FlexAttention Work Tracking

| 字段 | 值 |
| --- | --- |
| Issue | [#19765](https://github.com/vllm-project/vllm/issues/19765) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Vllm + FlexAttention Work Tracking

### Issue 正文摘录

# FlexAttention Performance & Feature Tracking ## Overview FlexAttention currently has significant performance bottlenecks and missing features that limit its adoption. This tracking issue provides an overview of the main categories of work needed. ## 🚨 Critical Performance Issues **Primary bottleneck**: Custom op prevents cudagraphing, causing ~10x throughput regression. Additional issues include unnecessary recompilations and metadata operations. ## 🔧 Missing Features FlexAttention currently only supports basic causal attention. Many common attention patterns are not yet implemented: - ALiBi slopes - Sliding window attention - Block sparse attention - Quantized KV cache - Encoder/cross-attention support - Speculative decoding - And more... ## 📋 Detailed Work Items & Contributing **All specific issues, performance optimizations, and feature implementations are tracked in the project board:** ### 👉 [**[FlexAttention Project Board](https://github.com/users/drisspg/projects/7/views/1)**] 👈 The project board contains: - Individual issues for each performance bottleneck - Feature implementation tasks with detailed specifications - Priority labels and status tracking - Technical implem...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Vllm + FlexAttention Work Tracking feature request;stale # FlexAttention Performance & Feature Tracking ## Overview FlexAttention currently has significant performance bottlenecks and missing features that limit its ado...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ut regression. Additional issues include unnecessary recompilations and metadata operations. ## 🔧 Missing Features FlexAttention currently only supports basic causal attention. Many common attention patterns are not yet...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s **Primary bottleneck**: Custom op prevents cudagraphing, causing ~10x throughput regression. Additional issues include unnecessary recompilations and metadata operations. ## 🔧 Missing Features FlexAttention currently...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ecoding - And more... ## 📋 Detailed Work Items & Contributing **All specific issues, performance optimizations, and feature implementations are tracked in the project board:** ### 👉 [**[FlexAttention Project Board](http...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: : - ALiBi slopes - Sliding window attention - Block sparse attention - Quantized KV cache - Encoder/cross-attention support - Speculative decoding - And more... ## 📋 Detailed Work Items & Contributing **All specific iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
