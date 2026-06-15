# vllm-project/vllm#540: Best performance for distributed offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#540](https://github.com/vllm-project/vllm/issues/540) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Best performance for distributed offline inference

### Issue 正文摘录

Perhaps this question is better meant for a discussion forum! I want to run offline inference over a large dataset on a node with multiple A100 GPUs. There is a broad design space available here * using `tensor_parallel_size` in vs offloading jobs to different GPUs over separate processing using `CUDA_VISIBLE_DEVICES` * finding optimal _batch size_ * possibly ordering queries across a batch!? I was curious if you had thoughts on this and is there any recommended approach?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt to run offline inference over a large dataset on a node with multiple A100 GPUs. There is a broad design space available here * using `tensor_parallel_size` in vs offloading jobs to different GPUs over separate proce...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: broad design space available here * using `tensor_parallel_size` in vs offloading jobs to different GPUs over separate processing using `CUDA_VISIBLE_DEVICES` * finding optimal _batch size_ * possibly ordering queries a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
