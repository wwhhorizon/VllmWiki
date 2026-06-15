# vllm-project/vllm#5406: hidden-states from final (or middle layers)

| 字段 | 值 |
| --- | --- |
| Issue | [#5406](https://github.com/vllm-project/vllm/issues/5406) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> hidden-states from final (or middle layers)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am trying to extract hidden states from the final layer of llama3-8b (i.e., the final batch_size, seq_length, n_emb vector _before_ computing the logits). Would it be possible to add this functionality (i.e., access to hidden states similar to transformers ouput_hidden_states)? Thank you! ### Alternatives HuggingFace Transformers, but this is too slow. ### Additional context I am trying to train a SAE/linear probe on hidden states from llama3.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: and pitch I am trying to extract hidden states from the final layer of llama3-8b (i.e., the final batch_size, seq_length, n_emb vector _before_ computing the logits). Would it be possible to add this functionality (i.e....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hidden-states from final (or middle layers) feature request;unstale ### 🚀 The feature, motivation and pitch I am trying to extract hidden states from the final layer of llama3-8b (i.e., the final batch_size, seq_length,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
