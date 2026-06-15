# vllm-project/vllm#41278: [Feature]: Helion Kernels for MLA (Decode)

| 字段 | 值 |
| --- | --- |
| Issue | [#41278](https://github.com/vllm-project/vllm/issues/41278) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Helion Kernels for MLA (Decode)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Sub issue for #25179 to track custom pytorch-helion kernels for MultiHead Latent Attention + fp8 quantization. Helion guarantees to compile down to a single triton kernel, and with helion autotuner a optimal configuration can be found for the kernel. For complex and fused kernels such as MLA + dynamic fp8 quant, this can result in low effort - high reward scenario using abstact and pytorch native module of helion. ### Implementation Progress - [x] Study FlashMLA and other MLA implementations - [ ] Implement MLA Decode + dynamic fp8 per token quant - [ ] Implement MLA Decode + dynamic fp8 per block quant - [ ] Provide autotuned configs for different hardwares ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: to track custom pytorch-helion kernels for MultiHead Latent Attention + fp8 quantization. Helion guarantees to compile down to a single triton kernel, and with helion autotuner a optimal configuration can be found for t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Helion Kernels for MLA (Decode) feature request ### 🚀 The feature, motivation and pitch Sub issue for #25179 to track custom pytorch-helion kernels for MultiHead Latent Attention + fp8 quantization. Helion gu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ention + fp8 quantization. Helion guarantees to compile down to a single triton kernel, and with helion autotuner a optimal configuration can be found for the kernel. For complex and fused kernels such as MLA + dynamic...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for MultiHead Latent Attention + fp8 quantization. Helion guarantees to compile down to a single triton kernel, and with helion autotuner a optimal configuration can be found for the kernel. For complex and fused kernel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
