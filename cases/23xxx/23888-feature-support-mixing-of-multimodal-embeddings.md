# vllm-project/vllm#23888: [Feature]: Support mixing of multimodal embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#23888](https://github.com/vllm-project/vllm/issues/23888) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support mixing of multimodal embeddings

### Issue 正文摘录

Currently the infrastructure is designed to support **non-overlapping continugous embeddings** from multiple modalities, but this assumption might not be always true and has already caused some issue when supporting `audio_in_video` feature for Qwen2.5-Omni. If overlapping contiguous embeddings become more popular, we should think about how to support this need

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support mixing of multimodal embeddings feature request Currently the infrastructure is designed to support **non-overlapping continugous embeddings** from multiple modalities, but this assumption might not b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: en supporting `audio_in_video` feature for Qwen2.5-Omni. If overlapping contiguous embeddings become more popular, we should think about how to support this need
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support mixing of multimodal embeddings feature request Currently the infrastructure is designed to support **non-overlapping continugous embeddings** from multiple modalities, but this assumption might not b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
