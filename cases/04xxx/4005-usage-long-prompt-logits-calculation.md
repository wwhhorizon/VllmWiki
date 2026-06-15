# vllm-project/vllm#4005: [Usage]: long prompt logits calculation

| 字段 | 值 |
| --- | --- |
| Issue | [#4005](https://github.com/vllm-project/vllm/issues/4005) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: long prompt logits calculation

### Issue 正文摘录

### Your current environment vllm 0.4.0 GPU=A100 ### How would you like to use vllm I need to calculate very long prompt logits like 40k in my usage, I have set gpu_memory_utilization as minimum to support 40k, but softmax and other calculations are still beyond the capacity of a single GPU, how can I adjust it. I have deleted a lot of unneeded calculations that take up the GPU and still have the same problem with tensor_parallel_size=2 Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: support 40k, but softmax and other calculations are still beyond the capacity of a single GPU, how can I adjust it. I have deleted a lot of unneeded calculations that take up the GPU and still have the same problem with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: its calculation usage;stale ### Your current environment vllm 0.4.0 GPU=A100 ### How would you like to use vllm I need to calculate very long prompt logits like 40k in my usage, I have set gpu_memory_utilization as mini...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: long prompt logits calculation usage;stale ### Your current environment vllm 0.4.0 GPU=A100 ### How would you like to use vllm I need to calculate very long prompt logits like 40k in my usage, I have set gpu_me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
