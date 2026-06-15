# vllm-project/vllm#729: PagedAttentionWithRoPE seems not correctly initialized with model's original position_embedding?

| 字段 | 值 |
| --- | --- |
| Issue | [#729](https://github.com/vllm-project/vllm/issues/729) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> PagedAttentionWithRoPE seems not correctly initialized with model's original position_embedding?

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/66c54aa9c33555a6b41421d57d3ad6c1bf004ec9/vllm/model_executor/models/baichuan.py#L150-L156 Seems like we never tell PagedAttentionWithRoPE the original model position_embedding? The default position_embedding in PagedAttentionWithRoPE is 8192, during register_buffer it seems to register a sequence longer than the original model?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: PagedAttentionWithRoPE seems not correctly initialized with model's original position_embedding? https://github.com/vllm-project/vllm/blob/66c54aa9c33555a6b41421d57d3ad6c1bf004ec9/vllm/model_executor/models/baichuan.py#...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
