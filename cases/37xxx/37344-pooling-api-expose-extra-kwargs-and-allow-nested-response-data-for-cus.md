# vllm-project/vllm#37344: Pooling API: expose extra_kwargs and allow nested response data for custom poolers

| 字段 | 值 |
| --- | --- |
| Issue | [#37344](https://github.com/vllm-project/vllm/issues/37344) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Pooling API: expose extra_kwargs and allow nested response data for custom poolers

### Issue 正文摘录

Context: we maintain custom pooling workloads (for example GLiNER-style span outputs) and currently need a local patch against vllm entrypoints pooling protocol.\n\nRequest:\n1. Expose extra_kwargs on PoolingCompletionRequest and PoolingChatRequest, then pass through to PoolingParams.\n2. Relax PoolingResponseData.data typing so 3D nested tensors can be serialized without validation failure.\n\nWhy:\n- Custom poolers require structured metadata beyond prompt tokens.\n- Structured prediction heads can emit nested outputs (for example [L, K, C] logits).\n\nHappy to contribute a PR if this direction is acceptable.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: without validation failure.\n\nWhy:\n- Custom poolers require structured metadata beyond prompt tokens.\n- Structured prediction heads can emit nested outputs (for example [L, K, C] logits).\n\nHappy to contribute a PR...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rrently need a local patch against vllm entrypoints pooling protocol.\n\nRequest:\n1. Expose extra_kwargs on PoolingCompletionRequest and PoolingChatRequest, then pass through to PoolingParams.\n2. Relax PoolingResponse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
