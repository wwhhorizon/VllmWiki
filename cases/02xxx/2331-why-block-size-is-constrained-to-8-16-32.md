# vllm-project/vllm#2331: Why block_size is constrained to 8,16,32?

| 字段 | 值 |
| --- | --- |
| Issue | [#2331](https://github.com/vllm-project/vllm/issues/2331) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why block_size is constrained to 8,16,32?

### Issue 正文摘录

Can I use bigger block_size for longer sequences? Thank you!

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Why block_size is constrained to 8,16,32? Can I use bigger block_size for longer sequences? Thank you!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
