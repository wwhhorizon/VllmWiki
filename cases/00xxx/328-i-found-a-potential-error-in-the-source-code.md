# vllm-project/vllm#328: I found a potential error in the source code.

| 字段 | 值 |
| --- | --- |
| Issue | [#328](https://github.com/vllm-project/vllm/issues/328) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> I found a potential error in the source code.

### Issue 正文摘录

In the file scheduler.py， I find this ` num_batched_tokens = sum( seq_group.num_seqs(status=SequenceStatus.RUNNING) for seq_group in self.running ) ` and this ` # If the number of batched tokens exceeds the limit, stop. num_prompt_tokens = seq_group.get_seqs()[0].get_len() if (num_batched_tokens + num_prompt_tokens > self.scheduler_config.max_num_batched_tokens): break ` and this ` num_batched_tokens += num_prompt_tokens ` num_batched_tokens is defined as the number of sequences, while num_prompt_tokens is defined as the number of tokens of a waiting sequence, and the new num_batched_tokens is defined as the sum of them. should it be an error?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: I found a potential error in the source code. In the file scheduler.py， I find this ` num_batched_tokens = sum( seq_group.num_seqs(status=SequenceStatus.RUNNING) for seq_group in self.running ) ` and this ` # If the num...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _batched_tokens + num_prompt_tokens > self.scheduler_config.max_num_batched_tokens): break ` and this ` num_batched_tokens += num_prompt_tokens ` num_batched_tokens is defined as the number of sequences, while num_promp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
