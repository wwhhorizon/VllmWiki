# vllm-project/vllm#2492: `max_num_batched_tokens` and `max_num_seqs values`

| 字段 | 值 |
| --- | --- |
| Issue | [#2492](https://github.com/vllm-project/vllm/issues/2492) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `max_num_batched_tokens` and `max_num_seqs values`

### Issue 正文摘录

Hello, because I am new to vllm, I want to know how to set the `max_num_batched_tokens` and `max_num_seqs values` in order to achieve maximum inference performance. What is the relationship between `max_num_batched_tokens` and `max_num_seqs`? Why do the output tokens appear when I set different max_num_batched_tokens and max_num_seqs? The totals may be inconsistent

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in order to achieve maximum inference performance. What is the relationship between `max_num_batched_tokens` and `max_num_seqs`? Why do the output tokens appear when I set different max_num_batched_tokens and max_num_se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
