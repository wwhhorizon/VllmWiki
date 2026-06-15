# vllm-project/vllm#1555: Guidance on how many requests can be processed at a time?

| 字段 | 值 |
| --- | --- |
| Issue | [#1555](https://github.com/vllm-project/vllm/issues/1555) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Guidance on how many requests can be processed at a time?

### Issue 正文摘录

Hello - I am trying to understand how many requests can be processed in parallel with the llm_engine, and what keeps requests WAITING. I see various variables like "max_num_batched_tokens" and "max_num_seqs", but more details or documentation describing how this process occurs would be helpful. Moreover, how can we tune our system to do process more requests in parallel (e.g. use more GPUs if available, use smaller models, use smaller context windows, etc.)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Guidance on how many requests can be processed at a time? documentation;stale Hello - I am trying to understand how many requests can be processed in parallel with the llm_engine, and what keeps requests WAITING. I see...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: process more requests in parallel (e.g. use more GPUs if available, use smaller models, use smaller context windows, etc.)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: more requests in parallel (e.g. use more GPUs if available, use smaller models, use smaller context windows, etc.)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
