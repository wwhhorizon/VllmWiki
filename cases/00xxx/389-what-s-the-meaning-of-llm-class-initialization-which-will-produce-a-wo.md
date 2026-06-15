# vllm-project/vllm#389: What's the meaning of LLM class initialization, which will produce a worker and do a prediction with torch.zeros([max_num_batched_tokens]) as input ids?

| 字段 | 值 |
| --- | --- |
| Issue | [#389](https://github.com/vllm-project/vllm/issues/389) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What's the meaning of LLM class initialization, which will produce a worker and do a prediction with torch.zeros([max_num_batched_tokens]) as input ids?

### Issue 正文摘录

Can the initialization process be skipped? In my case, in deeper layers the hidden_states may get NAN (exceed fp16 maximum value), and hence cause the Sampler error.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
