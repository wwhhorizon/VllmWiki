# vllm-project/vllm#5203: [Feature]: inconsistent vocab_sizes support for draft and target workers while using Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#5203](https://github.com/vllm-project/vllm/issues/5203) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: inconsistent vocab_sizes support for draft and target workers while using Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vllm with Speculative Decoding requires that the draft model and target model have the same vocab size. However, the target model may have a larger parameter size and use more data to train, so the vocab size may also be slightly larger (If we consider using a 0.5B model as the draft model and a 72B model as the target model). In **spec_decode_worker.py** this file, line 564:` asserts all(vocab_sizes[0] == vocab_size for vocab_size in vocab_sizes)` making the inference pipeline unable to run. If this line is removed, the program may encounter a reshape error. So is inconsistent vocab sizes implementation possible? Such as using padding for the vocab size for the draft model? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: inconsistent vocab_sizes support for draft and target workers while using Speculative Decoding feature request ### 🚀 The feature, motivation and pitch Currently, vllm with Speculative Decoding requires that t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pitch Currently, vllm with Speculative Decoding requires that the draft model and target model have the same vocab size. However, the target model may have a larger parameter size and use more data to train, so the voca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
