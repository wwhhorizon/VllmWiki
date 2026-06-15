# vllm-project/vllm#995: PagedAttentionWithALiBi uses wrong dtype for bias

| 字段 | 值 |
| --- | --- |
| Issue | [#995](https://github.com/vllm-project/vllm/issues/995) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> PagedAttentionWithALiBi uses wrong dtype for bias

### Issue 正文摘录

This commit breaks PagedAttentionWithALiBi, where the bias from [set_attn_bias](https://github.com/vllm-project/vllm/blob/1117aa1411d9858ea5eef8a81e044379432e6d0e/vllm/model_executor/layers/attention.py#L343) is initialized to a wrong dtype, causing `RuntimeError: invalid dtype for bias - should match query's dtype` _Originally posted by @chu-tianxiang in https://github.com/vllm-project/vllm/issues/971#issuecomment-1712024749_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: PagedAttentionWithALiBi uses wrong dtype for bias This commit breaks PagedAttentionWithALiBi, where the bias from [set_attn_bias](https://github.com/vllm-project/vllm/blob/1117aa1411d9858ea5eef8a81e044379432e6d0e/vllm/m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/1117aa1411d9858ea5eef8a81e044379432e6d0e/vllm/model_executor/layers/attention.py#L343) is initialized to a wrong dtype, causing `RuntimeError: invalid dtype for bias - should match query's dty...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
