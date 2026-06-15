# vllm-project/vllm#935: Running multiple cards in parallel is slower(nearly twice) than a single card

| 字段 | 值 |
| --- | --- |
| Issue | [#935](https://github.com/vllm-project/vllm/issues/935) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Running multiple cards in parallel is slower(nearly twice) than a single card

### Issue 正文摘录

Hi, when I am running four A100 with parameter tensor_parallel_size is 4 in parallel, I found that the speed is slower(nearly twice) than a single card. can you explain what causes this and how to solve it. Thank you.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el is slower(nearly twice) than a single card Hi, when I am running four A100 with parameter tensor_parallel_size is 4 in parallel, I found that the speed is slower(nearly twice) than a single card. can you explain what...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
