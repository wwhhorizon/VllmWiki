# vllm-project/vllm#2387: How and where can I set the CUDA_VISIBLE_DEVICES when using vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#2387](https://github.com/vllm-project/vllm/issues/2387) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How and where can I set the CUDA_VISIBLE_DEVICES when using vllm?

### Issue 正文摘录

Such as, I set `tensor_parallel_size = 1`, then it will use the default GPU. Now I want run vllm in another one GPU, so how and where can I set the CUDA_VISIBLE_DEVICES?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: How and where can I set the CUDA_VISIBLE_DEVICES when using vllm? Such as, I set `tensor_parallel_size = 1`, then it will use the default GPU. Now I want run vllm in another one GPU, so how and where can I set the CUDA_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
