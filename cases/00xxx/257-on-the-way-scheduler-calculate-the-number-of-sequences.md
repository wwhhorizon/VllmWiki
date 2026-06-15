# vllm-project/vllm#257: On the way scheduler calculate the number of sequences

| 字段 | 值 |
| --- | --- |
| Issue | [#257](https://github.com/vllm-project/vllm/issues/257) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> On the way scheduler calculate the number of sequences

### Issue 正文摘录

In version 0.1.1, the scheduler calculates the number of sequences it schedules like the following: ```python num_new_seqs = seq_group.num_seqs(status=SequenceStatus.SWAPPED) num_curr_seqs = len(self.running) if num_curr_seqs + num_new_seqs > self.scheduler_config.max_num_seqs: break ``` `num_curr_seqs` is the number of sequence groups while `num_new_seqs` stands for the number of sequences in the new sequence group, I think it cannot form a meaningful metric by adding them together.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: On the way scheduler calculate the number of sequences bug In version 0.1.1, the scheduler calculates the number of sequences it schedules like the following: ```python num_new_seqs = seq_group.num_seqs(status=SequenceS...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eqs = len(self.running) if num_curr_seqs + num_new_seqs > self.scheduler_config.max_num_seqs: break ``` `num_curr_seqs` is the number of sequence groups while `num_new_seqs` stands for the number of sequences in the new...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: On the way scheduler calculate the number of sequences bug In version 0.1.1, the scheduler calculates the number of sequences it schedules like the following: ```python num_new_seqs = seq_group.num_seqs(status=SequenceS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
