# vllm-project/vllm#4766: [Feature]: could paged_attention_v1 support parameter 'attn_bias'

| 字段 | 值 |
| --- | --- |
| Issue | [#4766](https://github.com/vllm-project/vllm/issues/4766) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: could paged_attention_v1 support parameter 'attn_bias'

### Issue 正文摘录

### 🚀 The feature, motivation and pitch could paged_attention_v1[(code is here)](https://github.com/vllm-project/vllm/blob/main/vllm/_custom_ops.py) support parameter 'attn_bias' because while adding a new model, we use RelPositionMultiHeadedAttention([code is here](https://github.com/wenet-e2e/wenet/blob/f2372ae6d97f926688fee821e609e42aaf41571d/wenet/transformer/attention.py#L414)), we need 'attn_bias' too while running PagedAttention.forward_decode ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: could paged_attention_v1 support parameter 'attn_bias' feature request ### 🚀 The feature, motivation and pitch could paged_attention_v1[(code is here)](https://github.com/vllm-project/vllm/blob/main/vllm/_cust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: custom_ops.py) support parameter 'attn_bias' because while adding a new model, we use RelPositionMultiHeadedAttention([code is here](https://github.com/wenet-e2e/wenet/blob/f2372ae6d97f926688fee821e609e42aaf41571d/wenet...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
