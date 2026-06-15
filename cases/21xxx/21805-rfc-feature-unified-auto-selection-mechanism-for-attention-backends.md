# vllm-project/vllm#21805: [RFC][Feature]: Unified Auto-Selection Mechanism for Attention Backends

| 字段 | 值 |
| --- | --- |
| Issue | [#21805](https://github.com/vllm-project/vllm/issues/21805) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC][Feature]: Unified Auto-Selection Mechanism for Attention Backends

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Summary This RFC proposes introducing a robust, unified mechanism for automatic selection of attention backends in vLLM, initially focused on ROCm, with a roadmap for extending support to all other major backends. The primary goal is to simplify user experience and ensure optimal backend selection based on hardware, available dependencies, and configuration, while retaining the ability for manual override when needed. # Motivation Manually configuring and selecting the most suitable attention backend has been a significant pain point for ROCm users. The “best performing” attention backend, AiterFlashAttention, requires explicit activation via the environment variable VLLM_ROCM_USE_AITER (False by default). While this was necessary before as the AiterFlashAttentionBackend implementation was “experimental”; However, the AiterFlashAttentionBackend has now been validated and tested on many models and achieves better performance over the Triton implementation. On another note, the TritonAttentionBackend supports two different modes, a “unified attention” mode and a “split prefill decode” mode, with the former being the default backend despite t...

## 现有链接修复摘要

#7701 [Kernel] (2/N) Machete - Integrate into CompressedTensorsWNA16 and GPTQMarlin | #11785 [TPU][Quantization] TPU `W8A8` | #21366 [ROCm] Auto-Select Attention Backend

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [RFC][Feature]: Unified Auto-Selection Mechanism for Attention Backends feature request;stale ### 🚀 The feature, motivation and pitch # Summary This RFC proposes introducing a robust, unified mechanism for automatic sel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC][Feature]: Unified Auto-Selection Mechanism for Attention Backends feature request;stale ### 🚀 The feature, motivation and pitch # Summary This RFC proposes introducing a robust, unified mechanism for automatic sel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: explicit activation via the environment variable VLLM_ROCM_USE_AITER (False by default). While this was necessary before as the AiterFlashAttentionBackend implementation was “experimental”; However, the AiterFlashAttent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: eature]: Unified Auto-Selection Mechanism for Attention Backends feature request;stale ### 🚀 The feature, motivation and pitch # Summary This RFC proposes introducing a robust, unified mechanism for automatic selection...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: optimal backend selection based on hardware, available dependencies, and configuration, while retaining the ability for manual override when needed. # Motivation Manually configuring and selecting the most suitable atte...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7701](https://github.com/vllm-project/vllm/pull/7701) | mentioned | 0.45 | [Kernel] (2/N) Machete - Integrate into CompressedTensorsWNA16 and GPTQMarlin | iguration(similar to the linear kernel selection logic implemented in #7701 and #11785). - provides clear log/warning messages for fallback paths, unsupported cases, and override… |
| [#11785](https://github.com/vllm-project/vllm/pull/11785) | mentioned | 0.45 | [TPU][Quantization] TPU `W8A8` | similar to the linear kernel selection logic implemented in #7701 and #11785). - provides clear log/warning messages for fallback paths, unsupported cases, and override scenarios.… |
| [#21366](https://github.com/vllm-project/vllm/pull/21366) | mentioned | 0.45 | [ROCm] Auto-Select Attention Backend | r and actionable logging. # implementation plan - [ ] merge/improve #21366 as the initial implementation. - [ ] implement selection policy for rocm (mla), cuda, cpu, and additiona… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
