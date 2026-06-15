# vllm-project/vllm#34008: [Feature]: W4A16 (int4) GEMM / Grouped GEMM Kernels for AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#34008](https://github.com/vllm-project/vllm/issues/34008) |
| 状态 | open |
| 标签 | feature request;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: W4A16 (int4) GEMM / Grouped GEMM Kernels for AMD

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM currently lacks performant W4A16 (int4 weight) GEMM support on AMD ROCm/AITER backends. W4A16 Grouped GEMM exists only as a Triton kernel, which is not optimal. Would it be possible to add AMD-optimized native kernels for W4A16 GEMM and W4A16 grouped GEMM? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: currently lacks performant W4A16 (int4 weight) GEMM support on AMD ROCm/AITER backends. W4A16 Grouped GEMM exists only as a Triton kernel, which is not optimal. Would it be possible to add AMD-optimized native kernels f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ature]: W4A16 (int4) GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM currently lacks performant W4A16 (int4 weight) GEMM support on AMD ROCm/AITER backends. W4...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: W4A16 (int4) GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM currently lacks performant W4A16 (int4 weight) GEMM support on AMD ROCm/AITER backends....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: W4A16 (int4) GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM currently lacks performant W4A16 (int4 weight) GEMM support on AMD ROCm/AITER backends....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: W4A16 (int4) GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM currently lacks performant W4A16 (int4 weight) GEMM support on AMD ROCm/AITER backends....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
