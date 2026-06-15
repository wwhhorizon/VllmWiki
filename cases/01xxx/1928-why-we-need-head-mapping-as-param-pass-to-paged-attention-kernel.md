# vllm-project/vllm#1928: Why we need head_mapping as param pass to paged_attention kernel?

| 字段 | 值 |
| --- | --- |
| Issue | [#1928](https://github.com/vllm-project/vllm/issues/1928) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why we need head_mapping as param pass to paged_attention kernel?

### Issue 正文摘录

I think this mapping is used to support MQA/GQA. But kv_head_num is fully to express the relation between q's head and kv's head, which can also avoid loading the map into register. is It better? Or is there have models must use the mapping to express the relation between q and kv?

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Why we need head_mapping as param pass to paged_attention kernel? I think this mapping is used to support MQA/GQA. But kv_head_num is fully to express the relation between q's head and kv's head, which can also avoid lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lso avoid loading the map into register. is It better? Or is there have models must use the mapping to express the relation between q and kv?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
