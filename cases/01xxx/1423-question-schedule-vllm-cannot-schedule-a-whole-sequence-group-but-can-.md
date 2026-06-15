# vllm-project/vllm#1423: [Question][Schedule] vLLM cannot schedule a whole sequence group but can schedule some of its sequences

| 字段 | 值 |
| --- | --- |
| Issue | [#1423](https://github.com/vllm-project/vllm/issues/1423) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Question][Schedule] vLLM cannot schedule a whole sequence group but can schedule some of its sequences

### Issue 正文摘录

As the [paper](https://arxiv.org/pdf/2309.06180.pdf) wrote, > The sequences within one sequence group are always preempted or rescheduled together due to potential memory sharing across those sequences. In such a condition: * **Total** GPU memory is not enough to hold a sequence group * **Total** GPU memory is enough to hold some of sequences in that group This may happen in sequence groups with a large size. According to the paper, this sequence group would not be scheduled, and the scheduler would be **stuck**. Would the following method be better for availability while still utilizing the advantage of memory sharing: * First, try scheduling a sequence group. * If all sequence groups to be scheduled can not fit in GPU memory, select one sequence group and schedule as many sequences of this group.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: emory sharing across those sequences. In such a condition: * **Total** GPU memory is not enough to hold a sequence group * **Total** GPU memory is enough to hold some of sequences in that group This may happen in sequen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ording to the paper, this sequence group would not be scheduled, and the scheduler would be **stuck**. Would the following method be better for availability while still utilizing the advantage of memory sharing: * First...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
