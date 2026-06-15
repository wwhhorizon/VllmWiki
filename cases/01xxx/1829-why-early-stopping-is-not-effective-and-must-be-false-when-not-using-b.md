# vllm-project/vllm#1829: Why early_stopping is not effective and must be False when not using beam search?

| 字段 | 值 |
| --- | --- |
| Issue | [#1829](https://github.com/vllm-project/vllm/issues/1829) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why early_stopping is not effective and must be False when not using beam search?

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: early_stopping is not effective and must be False when not using beam search?
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Why early_stopping is not effective and must be False when not using beam search?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
