# vllm-project/vllm#1455: RuntimeError: Unsupported head size 32

| 字段 | 值 |
| --- | --- |
| Issue | [#1455](https://github.com/vllm-project/vllm/issues/1455) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: Unsupported head size 32

### Issue 正文摘录

When I used vllm to speed up my custom model inference, I encountered this error: RuntimeError: Unsupported head size 32. Log as follows: ``` File "/jfs/zjq/project/vllm/vllm/model_executor/layers/attention.py", line 289, in forward self.single_query_cached_kv_attention(output, query, key_cache, File "/jfs/zjq/project/vllm/vllm/model_executor/layers/attention.py", line 162, in single_query_cached_kv_attention attention_ops.paged_attention_v1( RuntimeError: Unsupported head size: 32 python-BaseException ``` Why does attention_ops.paged_attention_v1 limited the head_size? How can I fix it.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: meError: Unsupported head size 32 When I used vllm to speed up my custom model inference, I encountered this error: RuntimeError: Unsupported head size 32. Log as follows: ``` File "/jfs/zjq/project/vllm/vllm/model_exec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
