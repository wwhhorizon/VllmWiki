# vllm-project/vllm#32072: [Tracking]: Deprecate CPU seqlen related CommonAttentionMetadata properties

| 字段 | 值 |
| --- | --- |
| Issue | [#32072](https://github.com/vllm-project/vllm/issues/32072) |
| 状态 | open |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking]: Deprecate CPU seqlen related CommonAttentionMetadata properties

### Issue 正文摘录

Track deprecation of ``` seq_lens_cpu num_computed_tokens_cpu ``` in `CommonAttentionMetdata`. Merged PRs: - https://github.com/vllm-project/vllm/pull/31773 - https://github.com/vllm-project/vllm/pull/31774 - https://github.com/vllm-project/vllm/pull/31850 WIP PRs: - https://github.com/vllm-project/vllm/pull/31852 - https://github.com/vllm-project/vllm/pull/32073 ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Tracking]: Deprecate CPU seqlen related CommonAttentionMetadata properties documentation;stale Track deprecation of ``` seq_lens_cpu num_computed_tokens_cpu ``` in `CommonAttentionMetdata`. Merged PRs: - https://github...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cate CPU seqlen related CommonAttentionMetadata properties documentation;stale Track deprecation of ``` seq_lens_cpu num_computed_tokens_cpu ``` in `CommonAttentionMetdata`. Merged PRs: - https://github.com/vllm-project...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
