# vllm-project/vllm#30654: [Feature][Attention][UX]: Incorporate Features into Attention Selection

| 字段 | 值 |
| --- | --- |
| Issue | [#30654](https://github.com/vllm-project/vllm/issues/30654) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Attention][UX]: Incorporate Features into Attention Selection

### Issue 正文摘录

### 🚀 The feature, motivation and pitch SUMMARY: * we have default attention backends by priority and a notion of which backend supports what hw * however, certain features are not considered in this (e.g. fp8 kv cache, e.g. attention sinks) Recent example, we had test failures because we updated the logic to load kv cache quantization from the model config. But since CUTLASS_MLA is the default backend on B200, we started seeing test failures (since CUTLASS MLA does not support fp8 kv cache) because we were not automatically falling back to FLASHINFER_MLA (which does) So the proposal is to: - make sure all attention backends report what features are supported - update the attention selector to consider these features in the selection ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: The feature, motivation and pitch SUMMARY: * we have default attention backends by priority and a notion of which backend supports what hw * however, certain features are not considered in this (e.g. fp8 kv cache, e.g....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rts what hw * however, certain features are not considered in this (e.g. fp8 kv cache, e.g. attention sinks) Recent example, we had test failures because we updated the logic to load kv cache quantization from the model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n from the model config. But since CUTLASS_MLA is the default backend on B200, we started seeing test failures (since CUTLASS MLA does not support fp8 kv cache) because we were not automatically falling back to FLASHINF...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ures because we updated the logic to load kv cache quantization from the model config. But since CUTLASS_MLA is the default backend on B200, we started seeing test failures (since CUTLASS MLA does not support fp8 kv cac...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: what hw * however, certain features are not considered in this (e.g. fp8 kv cache, e.g. attention sinks) Recent example, we had test failures because we updated the logic to load kv cache quantization from the model con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
