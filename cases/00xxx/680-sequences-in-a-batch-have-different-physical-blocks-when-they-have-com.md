# vllm-project/vllm#680: Sequences in a batch have different physical blocks when they have common prefix.

| 字段 | 值 |
| --- | --- |
| Issue | [#680](https://github.com/vllm-project/vllm/issues/680) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Sequences in a batch have different physical blocks when they have common prefix.

### Issue 正文摘录

When I use Baichuan, I found that every Sequence has its own physical block even the input data has common prefix(The length of the prefix is 16 which is equal to the block_size). Is it expected? According to ![image](https://github.com/vllm-project/vllm/assets/36357015/be397378-aa8c-417e-9ac2-f8af22847d69) , I think they will use shared physical block. This is my "block_tables", every sequence has a common prefix but different physical block id (Pdb) seq_group_metadata_list[0].block_tables {0: [7303, 7302]} (Pdb) seq_group_metadata_list[1].block_tables {1: [7301, 7300]} (Pdb) seq_group_metadata_list[2].block_tables {2: [7299, 7298]} (Pdb) seq_group_metadata_list[3].block_tables {3: [7297, 7296]} (Pdb) seq_group_metadata_list[4].block_tables {4: [7295, 7294]}

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Sequences in a batch have different physical blocks when they have common prefix. When I use Baichuan, I found that every Sequence has its own physical block even the input data has common prefix(The length of the prefi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
