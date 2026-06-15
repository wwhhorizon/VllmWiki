# vllm-project/vllm#1627: Where is the part related to system prompt?

| 字段 | 值 |
| --- | --- |
| Issue | [#1627](https://github.com/vllm-project/vllm/issues/1627) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Where is the part related to system prompt?

### Issue 正文摘录

Section 4.4 in the [paper](https://arxiv.org/pdf/2309.06180.pdf) mentioned that you reserved some physic blocks to cope with system prompts; where are the codes for this part?

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ://arxiv.org/pdf/2309.06180.pdf) mentioned that you reserved some physic blocks to cope with system prompts; where are the codes for this part?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
