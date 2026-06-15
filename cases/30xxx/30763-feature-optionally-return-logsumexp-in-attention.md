# vllm-project/vllm#30763: [Feature]: Optionally Return LogSumExp in Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#30763](https://github.com/vllm-project/vllm/issues/30763) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optionally Return LogSumExp in Attention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Many attention backends [support LSE calculation](can_return_lse_for_decode) (context parallel, etc). It would be good if `lse` was an optional return, so algorithms could be built on top (ex. different formulations of [attention sinks using logsumexp trick](https://github.com/huggingface/transformers/pull/41083/files#diff-4ec978a88157587c096effea51ad2575569aaa093fda44986232d71f9f50c90eR322), recording attention scores, etc). Here's an example from [unsloth.ai docs](https://docs.unsloth.ai/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training#mathematical-derivation-for-attention-sinks) on how it could be used to implement attention sinks (not necessarily headwise scalars already supported in kernels, but also token-wise, etc.) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rmulations of [attention sinks using logsumexp trick](https://github.com/huggingface/transformers/pull/41083/files#diff-4ec978a88157587c096effea51ad2575569aaa093fda44986232d71f9f50c90eR322), recording attention scores,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Optionally Return LogSumExp in Attention feature request;stale ### 🚀 The feature, motivation and pitch Many attention backends [support LSE calculation](can_return_lse_for_decode) (context parallel, etc). It...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ## 🚀 The feature, motivation and pitch Many attention backends [support LSE calculation](can_return_lse_for_decode) (context parallel, etc). It would be good if `lse` was an optional return, so algorithms could be built...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: re request;stale ### 🚀 The feature, motivation and pitch Many attention backends [support LSE calculation](can_return_lse_for_decode) (context parallel, etc). It would be good if `lse` was an optional return, so algorit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
