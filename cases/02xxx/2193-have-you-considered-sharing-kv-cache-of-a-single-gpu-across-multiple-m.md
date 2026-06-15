# vllm-project/vllm#2193: Have you considered sharing KV cache of a single GPU across multiple models?

| 字段 | 值 |
| --- | --- |
| Issue | [#2193](https://github.com/vllm-project/vllm/issues/2193) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Have you considered sharing KV cache of a single GPU across multiple models?

### Issue 正文摘录

Sometimes it is more cost-effective to deploy multiple models on the same set of GPUs. But vLLM supports running one model only, and will occupy fixed-size GPU memory from beginning. That makes it hard to share GPU across multiple models.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Have you considered sharing KV cache of a single GPU across multiple models? Sometimes it is more cost-effective to deploy multiple models on the same set of GPUs. But vLLM supports running one model only, and will occu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Have you considered sharing KV cache of a single GPU across multiple models? Sometimes it is more cost-effective to deploy multiple models on the same set of GPUs. But vLLM supports running one model only, and will occu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
