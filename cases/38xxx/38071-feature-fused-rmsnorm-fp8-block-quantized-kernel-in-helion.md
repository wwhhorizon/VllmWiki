# vllm-project/vllm#38071: [Feature]: fused RMSNorm + fp8 block quantized kernel in Helion

| 字段 | 值 |
| --- | --- |
| Issue | [#38071](https://github.com/vllm-project/vllm/issues/38071) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: fused RMSNorm + fp8 block quantized kernel in Helion

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on expanding fused kernel support as tracked in #25179 and would like to implement a fused RMSNorm + fp8 block quantization kernel in Helion. A CUDA kernel for this already exists, but a Helion version would improve portability across hardware (Hopper, AMD, etc.) and help avoid a combinatorial explosion of platform-specific kernels. This is the RMSNorm counterpart to #36972 (fused SiLU + fp8 block quant in Helion). ### Alternatives The existing CUDA kernel works but is not portable. A Triton kernel is another option, but Helion is preferred per the maintainers for better cross-platform support. ### Additional context related issues.... #25179, #36972, #27847 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: o implement a fused RMSNorm + fp8 block quantization kernel in Helion. A CUDA kernel for this already exists, but a Helion version would improve portability across hardware (Hopper, AMD, etc.) and help avoid a combinato...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: on kernel in Helion. A CUDA kernel for this already exists, but a Helion version would improve portability across hardware (Hopper, AMD, etc.) and help avoid a combinatorial explosion of platform-specific kernels. This...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: fused RMSNorm + fp8 block quantized kernel in Helion feature request ### 🚀 The feature, motivation and pitch I'm working on expanding fused kernel support as tracked in #25179 and would like to implement a fu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ### Alternatives The existing CUDA kernel works but is not portable. A Triton kernel is another option, but Helion is preferred per the maintainers for better cross-platform support. ### Additional context related issue...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: fused RMSNorm + fp8 block quantized kernel in Helion feature request ### 🚀 The feature, motivation and pitch I'm working on expanding fused kernel support as tracked in #25179 and would like to implement a fu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
