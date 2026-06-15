# vllm-project/vllm#29920: [Feature]: Add support for fused fp8 output to FlashAttention 3

| 字段 | 值 |
| --- | --- |
| Issue | [#29920](https://github.com/vllm-project/vllm/issues/29920) |
| 状态 | open |
| 标签 | help wanted;performance;feature request;torch.compile;keep-open |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | attention;fp8;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add support for fused fp8 output to FlashAttention 3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On Hopper, we use FlashAttention as the default attention backend. When o-proj is quantized to fp8, we are leaving performance on the table as FA3 does not support fused output fp8 quant. With Triton/ROCm/AITER backends we saw up to 8% speedups with attention+quant fusion. vLLM already maintains our own fork of FA, adding output quant support should be pretty non-intrusive. Subtasks: - vllm-flash-attn: - add `output_scale` parameter to attention forward functions - plumb parameter through all layers of the interface - compare branching at runtime/compile-time for performance and binary size (Hopper) - vllm: - integrate new FA version - add support for attention+quant fusion to FA attention backend - check FA version, hardware version - should be as easy as modifying the `supports_fused_output_quant` method and plumbing `output_scale` from `FlashAttentionImpl.forward()` to the kernel call ### Additional context cc @LucasWilkinson ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## 现有链接修复摘要

#31636 [Frontend] Add FP8 output quantization support to FlashAttention backend

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Feature]: Add support for fused fp8 output to FlashAttention 3 help wanted;performance;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch On Hopper, we use FlashAttention as the default att...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: output to FlashAttention 3 help wanted;performance;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch On Hopper, we use FlashAttention as the default attention backend. When o-proj is quanti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: Add support for fused fp8 output to FlashAttention 3 help wanted;performance;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch On Hopper, we use FlashAttention as the default att...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: uest;torch.compile;keep-open ### 🚀 The feature, motivation and pitch On Hopper, we use FlashAttention as the default attention backend. When o-proj is quantized to fp8, we are leaving performance on the table as FA3 doe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: for fused fp8 output to FlashAttention 3 help wanted;performance;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch On Hopper, we use FlashAttention as the default attention backend. When o-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31636](https://github.com/vllm-project/vllm/pull/31636) | closes_keyword | 0.95 | [Frontend] Add FP8 output quantization support to FlashAttention backend | Fixes #29920 Complementary to https://github.com/vllm-project/flash-attention/pull/113 Changes: - Enable `fused_output_quant_supported()` for FA3 + kFp8StaticTensorSym - Pass out |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
