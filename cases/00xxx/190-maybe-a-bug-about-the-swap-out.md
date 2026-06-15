# vllm-project/vllm#190: Maybe a bug about the swap_out

| 字段 | 值 |
| --- | --- |
| Issue | [#190](https://github.com/vllm-project/vllm/issues/190) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Maybe a bug about the swap_out

### Issue 正文摘录

- [preempt](https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L369) use the _```preempt_by_swap ``` to swap CPU and GPU block - The ```preempt_by_swap ``` will call [swap_out](https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L407) - I see the [swap_out](https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager.py#L199), it will swap all seq in the seq_group even its status is RUNNING. But I think you want to achieve to swap the seq whose status is [SequenceStatus.SWAPPED](https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L393)

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e/scheduler.py#L369) use the _```preempt_by_swap ``` to swap CPU and GPU block - The ```preempt_by_swap ``` will call [swap_out](https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L407) - I see the [s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ut - [preempt](https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L369) use the _```preempt_by_swap ``` to swap CPU and GPU block - The ```preempt_by_swap ``` will call [swap_out](https://github.com/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
