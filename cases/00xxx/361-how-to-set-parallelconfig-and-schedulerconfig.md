# vllm-project/vllm#361: How to set ParallelConfig and SchedulerConfig?

| 字段 | 值 |
| --- | --- |
| Issue | [#361](https://github.com/vllm-project/vllm/issues/361) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to set ParallelConfig and SchedulerConfig?

### Issue 正文摘录

Is ParallelConfig.pipeline_parallel_size used on multiple gpu cards? Can it be set to the number of GPU cards? Does it relate to processing multiple prompts and generating multiple results in parallel? For example, if there are 2 gpu cards and 7 requests, will it distribute the 7 requests simultaneously to the 2 gpu cards? How is the allocation done? Also, what do the parameters "max_num_batched_tokens" and "max_num_seqs" represent in SchedulerConfig? How can I set it to preserve longer context?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: How to set ParallelConfig and SchedulerConfig? Is ParallelConfig.pipeline_parallel_size used on multiple gpu cards? Can it be set to the number of GPU cards? Does it relate to processing multiple prompts and generating...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to set ParallelConfig and SchedulerConfig? Is ParallelConfig.pipeline_parallel_size used on multiple gpu cards? Can it be set to the number of GPU cards? Does it relate to processing multiple prompts and generating...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
