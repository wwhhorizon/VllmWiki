# vllm-project/vllm#33214: [RFC]: XPU kernel migration to vllm-xpu-kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#33214](https://github.com/vllm-project/vllm/issues/33214) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: XPU kernel migration to vllm-xpu-kernels

### Issue 正文摘录

### Motivation. This RFC proposes migrating Intel GPU (XPU) support in vLLM from Intel Extension for PyTorch (IPEX) to a dedicated kernel library, [`vllm-xpu-kernels`](https://github.com/vllm-project/vllm-xpu-kernels). This migration aims to improve performance, maintainability, and integration quality for Intel GPU backends in vLLM. **IPEX limitation** - heavy dependency - version compatibility issue between ipex/PyTorch/oneAPI - release cycle. **benifits of vllm-xpu-kernels** - fast moving, better maintainability and lightweight - purpose-built for vLLM inference ### Proposed Change. changing period: 2weeks, starting after v0.15.0 release, migration done before 0.16.0 release. will split to several PRs to make migration smoothly and fast: **0.16.0 milestone** - [x] vllm-xpu-kernel release v0.1.0. => Done. https://github.com/vllm-project/vllm-xpu-kernels/releases/tag/v0.1.0 - [x] remove ipex dependency, replace rms_norm/rope/activation/attention kernel with vllm-xpu-kernels. => Done: https://github.com/vllm-project/vllm/pull/33379 - [x] int4 compressed_tensor_w4a16 => Done https://github.com/vllm-project/vllm/pull/33973 - [x] fp8 gemm/model support (w8a16, w8a8) => Done, https://...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -kernels. => Done: https://github.com/vllm-project/vllm/pull/33379 - [x] int4 compressed_tensor_w4a16 => Done https://github.com/vllm-project/vllm/pull/33973 - [x] fp8 gemm/model support (w8a16, w8a8) => Done, https://g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: on quality for Intel GPU backends in vLLM. **IPEX limitation** - heavy dependency - version compatibility issue between ipex/PyTorch/oneAPI - release cycle. **benifits of vllm-xpu-kernels** - fast moving, better maintai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: done before 0.16.0 release. will split to several PRs to make migration smoothly and fast: **0.16.0 milestone** - [x] vllm-xpu-kernel release v0.1.0. => Done. https://github.com/vllm-project/vllm-xpu-kernels/releases/ta...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: _w4a16 => Done https://github.com/vllm-project/vllm/pull/33973 - [x] fp8 gemm/model support (w8a16, w8a8) => Done, https://github.com/vllm-project/vllm/pull/34117 - [x] unquantized moe support => Done, https://github.co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rove performance, maintainability, and integration quality for Intel GPU backends in vLLM. **IPEX limitation** - heavy dependency - version compatibility issue between ipex/PyTorch/oneAPI - release cycle. **benifits of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
