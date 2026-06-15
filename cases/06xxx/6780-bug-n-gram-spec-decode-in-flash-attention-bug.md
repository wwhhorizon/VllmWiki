# vllm-project/vllm#6780: [Bug]: N-gram spec_decode in flash_attention  bug

| 字段 | 值 |
| --- | --- |
| Issue | [#6780](https://github.com/vllm-project/vllm/issues/6780) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: N-gram spec_decode in flash_attention  bug

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug input_block_tables[i, :len(block_table)] = block_table， could not broadcast input array from shape (129,) into shape (128,)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: N-gram spec_decode in flash_attention bug bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug input_block_tables[i, :len(block_table)] = block_table， co...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: he output of `python collect_env.py` ``` ### 🐛 Describe the bug input_block_tables[i, :len(block_table)] = block_table， could not broadcast input array from shape (129,) into shape (128,)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
