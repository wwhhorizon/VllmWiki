# vllm-project/vllm#644: beam search bug

| 字段 | 值 |
| --- | --- |
| Issue | [#644](https://github.com/vllm-project/vllm/issues/644) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> beam search bug

### Issue 正文摘录

There is a problem with the implementation of vllm beam search. It seems that the previous search results have been fixed and unchanged. Can you provide some help

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: beam search bug bug There is a problem with the implementation of vllm beam search. It seems that the previous search results have been fixed and unchanged. Can you provide some help

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
