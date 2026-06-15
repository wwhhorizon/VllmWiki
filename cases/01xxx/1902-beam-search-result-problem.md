# vllm-project/vllm#1902: Beam Search Result Problem

| 字段 | 值 |
| --- | --- |
| Issue | [#1902](https://github.com/vllm-project/vllm/issues/1902) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Beam Search Result Problem

### Issue 正文摘录

beam search top1 result refers to generate shorted either truncated sequence (seem to generate eos token earlier), other results in beam search generated are normal length sequences, meanwhile reduce length penalty does not take effect has anyone encountered the same question ?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Beam Search Result Problem beam search top1 result refers to generate shorted either truncated sequence (seem to generate eos token earlier), other results in beam search generated are normal length sequences, meanwhile...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
