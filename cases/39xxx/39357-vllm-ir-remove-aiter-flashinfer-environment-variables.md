# vllm-project/vllm#39357: [vLLM IR] Remove AITER/FlashInfer environment variables

| 字段 | 值 |
| --- | --- |
| Issue | [#39357](https://github.com/vllm-project/vllm/issues/39357) |
| 状态 | open |
| 标签 | rocm;nvidia;vllm-ir |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] Remove AITER/FlashInfer environment variables

### Issue 正文摘录

Once IR ops are ported over, we should remove AITER & FlashInfer environment variables that enable/disable specific ops, in favor of the vLLM IR dispatching mechanism. I think we should just pull the band-aid off but I am open to a deprecation period. This issue does not apply to non-IR ops (GEMM, Attention, MoE, ...), but those environment variables should also be migrated to the proper config.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [vLLM IR] Remove AITER/FlashInfer environment variables rocm;nvidia;vllm-ir Once IR ops are ported over, we should remove AITER & FlashInfer environment variables that enable/disable specific ops, in favor of the vLLM I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [vLLM IR] Remove AITER/FlashInfer environment variables rocm;nvidia;vllm-ir Once IR ops are ported over, we should remove AITER & FlashInfer environment variables that enable/disable specific ops, in favor of the vLLM I...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: open to a deprecation period. This issue does not apply to non-IR ops (GEMM, Attention, MoE, ...), but those environment variables should also be migrated to the proper config.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d remove AITER & FlashInfer environment variables that enable/disable specific ops, in favor of the vLLM IR dispatching mechanism. I think we should just pull the band-aid off but I am open to a deprecation period. This...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ), but those environment variables should also be migrated to the proper config.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
