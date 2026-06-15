# vllm-project/vllm#26817: [Feature]: Add process_weights_after_loading to AttentionImpl

| 字段 | 值 |
| --- | --- |
| Issue | [#26817](https://github.com/vllm-project/vllm/issues/26817) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add process_weights_after_loading to AttentionImpl

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, in the `Attention` layer, we check if `process_weights_after_loading` exists and then call it conditionally, and after that we apply flashinfer-specific logic. Instead, we should just add a `process_weights_after_loading` method to AttentionImpl (no-op) by default, call it from `Attention.process_weights_after_loading`, and override it in `FlashInferAttentionImpl`. ### Alternatives _No response_ ### Additional context https://github.com/vllm-project/vllm/pull/23016#discussion_r2414787224 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _loading` exists and then call it conditionally, and after that we apply flashinfer-specific logic. Instead, we should just add a `process_weights_after_loading` method to AttentionImpl (no-op) by default, call it from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ts and then call it conditionally, and after that we apply flashinfer-specific logic. Instead, we should just add a `process_weights_after_loading` method to AttentionImpl (no-op) by default, call it from `Attention.pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 224 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ghts_after_loading to AttentionImpl help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Currently, in the `Attention` layer, we check if `process_weights_after_loading` exists and then c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
