# vllm-project/vllm#3314: What's up with Pipeline Parallelism?

| 字段 | 值 |
| --- | --- |
| Issue | [#3314](https://github.com/vllm-project/vllm/issues/3314) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What's up with Pipeline Parallelism?

### Issue 正文摘录

Hey vllm team, Hope you're all doing great! I‘m focusing on pipeline parallel inference and I hope it can be support on vllm. I noticed that pipeline parallelism was on the old roadmap（#244） , but it's not on the new roadmap（#2681）. Just curious, was there a specific reason you guys decided to skip it for now? Challenges with the implementation, or maybe it just didn't fit into the grand scheme of things at the moment? Would love to get any insights or thoughts you have on this. I'm really looking forward to seeing where you take vllm next!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: What's up with Pipeline Parallelism? feature request;stale Hey vllm team, Hope you're all doing great! I‘m focusing on pipeline parallel inference and I hope it can be support on vllm. I noticed that pipeline parallelis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ） , but it's not on the new roadmap（#2681）. Just curious, was there a specific reason you guys decided to skip it for now? Challenges with the implementation, or maybe it just didn't fit into the grand scheme of things...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: What's up with Pipeline Parallelism? feature request;stale Hey vllm team, Hope you're all doing great! I‘m focusing on pipeline parallel inference and I hope it can be support on vllm. I noticed that pipeline parallelis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
