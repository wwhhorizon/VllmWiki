# vllm-project/vllm#29134: [Performance]: Fully Async Spec-Decoding | Make `seq_lens_cpu` in CommonAttentionMetadata optional

| 字段 | 值 |
| --- | --- |
| Issue | [#29134](https://github.com/vllm-project/vllm/issues/29134) |
| 状态 | open |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Fully Async Spec-Decoding \| Make `seq_lens_cpu` in CommonAttentionMetadata optional

### Issue 正文摘录

### Proposal to improve performance Currently fully overlapping input-prep with model forward pass is blocked in the spec-decode case by the following Host<>GPU syncs: 1) `_get_valid_sampled_token_count` (ultimately needed to compute `seq_lens_cpu`): https://github.com/vllm-project/vllm/blob/fe25772aa97beb8bcb07ea49e06a2892b521a7ed/vllm/v1/worker/gpu_model_runner.py#L3109 2) in the `num_speculated_tokens > 1` case by needing to update `seq_lens_cpu` for attention metadata building (specifically for all the speculated tokens after the first one hence only impacting `num_speculated_tokens > 1` context: https://github.com/vllm-project/vllm/pull/26498) Ultimately in-order to realize fully async spec decoding we need to build attention metadata without knowing `seq_lens_cpu` (using device `seq_lens` on device is fine since any metadata building GPU kernels will get queued to after this is updated by the CUDA driver). This is currently not entirely possible for all backends (namely FlashInfer do to D2H or H2D, depending on if a host or device tensor is provided, inside the [plan function](https://github.com/flashinfer-ai/flashinfer/blob/cce4952fdd41b353325e11d99e1fc0b0737961ff/flashinfe...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ly overlapping input-prep with model forward pass is blocked in the spec-decode case by the following Host<>GPU syncs: 1) `_get_valid_sampled_token_count` (ultimately needed to compute `seq_lens_cpu`): https://github.co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ens > 1` case by needing to update `seq_lens_cpu` for attention metadata building (specifically for all the speculated tokens after the first one hence only impacting `num_speculated_tokens > 1` context: https://github....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ed by the CUDA driver). This is currently not entirely possible for all backends (namely FlashInfer do to D2H or H2D, depending on if a host or device tensor is provided, inside the [plan function](https://github.com/fl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ance]: Fully Async Spec-Decoding | Make `seq_lens_cpu` in CommonAttentionMetadata optional performance ### Proposal to improve performance Currently fully overlapping input-prep with model forward pass is blocked in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ata building GPU kernels will get queued to after this is updated by the CUDA driver). This is currently not entirely possible for all backends (namely FlashInfer do to D2H or H2D, depending on if a host or device tenso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
