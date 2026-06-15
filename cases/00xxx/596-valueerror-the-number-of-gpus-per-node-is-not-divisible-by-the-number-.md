# vllm-project/vllm#596: ValueError: The number of GPUs per node is not divisible by the number of tensor parallelism.

| 字段 | 值 |
| --- | --- |
| Issue | [#596](https://github.com/vllm-project/vllm/issues/596) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: The number of GPUs per node is not divisible by the number of tensor parallelism.

### Issue 正文摘录

I have 3 GPUs (3x3090). When I try to load `LLaMA-2-13B` and set the `tensor_parallel_size` to 2 it gives me this error. When I set it to 3 error follows like `ValueError: Total number of attention heads (40) must be divisible by tensor parallel size (3).`

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: umber of GPUs per node is not divisible by the number of tensor parallelism. bug I have 3 GPUs (3x3090). When I try to load `LLaMA-2-13B` and set the `tensor_parallel_size` to 2 it gives me this error. When I set it to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r of tensor parallelism. bug I have 3 GPUs (3x3090). When I try to load `LLaMA-2-13B` and set the `tensor_parallel_size` to 2 it gives me this error. When I set it to 3 error follows like `ValueError: Total number of at...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
