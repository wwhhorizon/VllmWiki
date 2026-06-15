# vllm-project/vllm#21984: [Performance]: Padded Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#21984](https://github.com/vllm-project/vllm/issues/21984) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Padded Speculative Decoding

### Issue 正文摘录

## Problem NOTE: this issue was originally targeting FlashMLA and MTP but padded speculative decoding also allows for overlapping the main model execution with prepping the inputs for spec-decode and is useful in a much broader context (namely when attention metadata construction is expensive and therefore could benefit from the overlap) FlashMLA currently assumes decode operations have `query_len=1`, forcing multi-token speculation requests to use the inefficient prefill path. ### Current Behavior ``` Normal Decode (works great! ✅): ┌─────────────┐ │ Request A │ query_len = 1 │ Request B │ query_len = 1 ──> FlashMLA Decode Path │ Request C │ query_len = 1 (Memory Efficient) │ Request D │ query_len = 1 └─────────────┘ MTP with Speculation (problem! ❌): ┌─────────────┐ │ Request A │ query_len = 4 │ Request B │ query_len = 4 ──> Forced to Prefill Path │ Request C │ query_len = 4 (Memory inefficient!; Compute Optimized) │ Request D │ query_len = 4 └─────────────┘ ``` Options: 1) varlen decode kernels; examples: FlashAttn MLA: https://github.com/vllm-project/vllm/pull/14258 FlashInfer MLA: https://github.com/vllm-project/vllm/pull/13630 *Benefits*: clean implementation *Downside*: can...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance]: Padded Speculative Decoding performance ## Problem NOTE: this issue was originally targeting FlashMLA and MTP but padded speculative decoding also allows for overlapping the main model execution with prep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: : FlashAttn MLA: https://github.com/vllm-project/vllm/pull/14258 FlashInfer MLA: https://github.com/vllm-project/vllm/pull/13630 *Benefits*: clean implementation *Downside*: cant use SOTA Kernels like FlashMLA and the u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ap) FlashMLA currently assumes decode operations have `query_len=1`, forcing multi-token speculation requests to use the inefficient prefill path. ### Current Behavior ``` Normal Decode (works great! ✅): ┌─────────────┐...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: more complicated implementation ## Padded speculation proposal ### 1. Smart Decode Classification Increase decode threshold and use minimum query_len for uniform batches, this ensures we only use the decode path for sma...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ec-decode and is useful in a much broader context (namely when attention metadata construction is expensive and therefore could benefit from the overlap) FlashMLA currently assumes decode operations have `query_len=1`,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
