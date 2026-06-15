# vllm-project/vllm#3138: Expert Parallelism with current FusedMoE kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#3138](https://github.com/vllm-project/vllm/issues/3138) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Expert Parallelism with current FusedMoE kernel

### Issue 正文摘录

I'm fairly new so bear with me. I wanted to use the fused_moe kernel to implement a model with expert parallelism. Can I do that? Is that possible with the current kernel implementation?

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Expert Parallelism with current FusedMoE kernel stale I'm fairly new so bear with me. I wanted to use the fused_moe kernel to implement a model with expert parallelism. Can I do that? Is that possible with the current ke
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Expert Parallelism with current FusedMoE kernel stale I'm fairly new so bear with me. I wanted to use the fused_moe kernel to implement a model with expert parallelism. Can I do that? Is that possible with the current k...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: new so bear with me. I wanted to use the fused_moe kernel to implement a model with expert parallelism. Can I do that? Is that possible with the current kernel implementation?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Expert Parallelism with current FusedMoE kernel stale I'm fairly new so bear with me. I wanted to use the fused_moe kernel to implement a model with expert parallelism. Can I do that? Is that possible with the current k...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
