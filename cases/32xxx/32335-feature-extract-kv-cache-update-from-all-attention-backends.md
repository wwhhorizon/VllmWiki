# vllm-project/vllm#32335: [Feature]: Extract KV-Cache update from all attention backends

| 字段 | 值 |
| --- | --- |
| Issue | [#32335](https://github.com/vllm-project/vllm/issues/32335) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 51; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Extract KV-Cache update from all attention backends

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Similar to how https://github.com/vllm-project/vllm/pull/25954 extracts it from FlashAttn. Ideally, we want to cover all backends with kv-cache update from `v1/attention/backends`. Backends: - [x] FlashAttention - [x] FlashInfer - [ ] AiterFlashAttention (in progress) - [x] RocmAiterUnifiedAttention - [x] RocmAttention - [x] TritonAttention - [x] FlashAttentionDiffKV - [x] FlexAttention - [x] TreeAttention MLA Backends: - [x] FlashAttnMLA - [x] FlashInferMLA - [x] FlashMLASparse - [x] FlashMLA - [x] AiterMLA - [x] ROCMAiterMLASparse - [x] CutlassMLA - [x] TritonMLA After all backends are supported, we can remove `slot_mapping` from attention metadata. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Feature]: Extract KV-Cache update from all attention backends help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Similar to how https://github.com/vllm-project/vllm/pull/25954 extracts...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Attention - [x] FlashInfer - [ ] AiterFlashAttention (in progress) - [x] RocmAiterUnifiedAttention - [x] RocmAttention - [x] TritonAttention - [x] FlashAttentionDiffKV - [x] FlexAttention - [x] TreeAttention MLA Backend...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: assMLA - [x] TritonMLA After all backends are supported, we can remove `slot_mapping` from attention metadata. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Extract KV-Cache update from all attention backends help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Similar to how https://github.com/vllm-project/vllm/pull/25954 extracts...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: update from all attention backends help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Similar to how https://github.com/vllm-project/vllm/pull/25954 extracts it from FlashAttn. Ideally,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
