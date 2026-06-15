# vllm-project/vllm#6288: [Usage]: Why compute_full_blocks_in_seq in block manager v1 needs -1

| 字段 | 值 |
| --- | --- |
| Issue | [#6288](https://github.com/vllm-project/vllm/issues/6288) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why compute_full_blocks_in_seq in block manager v1 needs -1

### Issue 正文摘录

### Your current environment Why in this line needs -1 ? https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager_v1.py#L667) ### How would you like to use vllm _No response_

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: Why compute_full_blocks_in_seq in block manager v1 needs -1 usage ### Your current environment Why in this line needs -1 ? https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager_v1.py#L667) ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
