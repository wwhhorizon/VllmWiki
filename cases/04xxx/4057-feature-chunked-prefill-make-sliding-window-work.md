# vllm-project/vllm#4057: [Feature][Chunked prefill]: Make sliding window work

| 字段 | 值 |
| --- | --- |
| Issue | [#4057](https://github.com/vllm-project/vllm/issues/4057) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Chunked prefill]: Make sliding window work

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, both prefix caching and chunked prefill doesn't work with sliding window attention because the block tables are not updated properly. Both uses `context_attention_forward` (https://github.com/vllm-project/vllm/blob/5c2e66e4871917c5d59cc4a8b89ef53e690e9bd9/vllm/attention/ops/prefix_prefill.py#L621), which I am not sure if sliding window is supported. We should fix this if we want to enable chunked prefill/prefix caching for models that use sliding window attn (e.g., mistral 7B). ### Alternatives N/A ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][Chunked prefill]: Make sliding window work feature request ### 🚀 The feature, motivation and pitch Currently, both prefix caching and chunked prefill doesn't work with sliding window attention because the bloc...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: d chunked prefill doesn't work with sliding window attention because the block tables are not updated properly. Both uses `context_attention_forward` (https://github.com/vllm-project/vllm/blob/5c2e66e4871917c5d59cc4a8b8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d chunked prefill doesn't work with sliding window attention because the block tables are not updated properly. Both uses `context_attention_forward` (https://github.com/vllm-project/vllm/blob/5c2e66e4871917c5d59cc4a8b8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: should fix this if we want to enable chunked prefill/prefix caching for models that use sliding window attn (e.g., mistral 7B). ### Alternatives N/A ### Additional context _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
