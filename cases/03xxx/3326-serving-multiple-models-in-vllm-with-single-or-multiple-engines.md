# vllm-project/vllm#3326: Serving multiple models in vLLM with single or multiple engines

| 字段 | 值 |
| --- | --- |
| Issue | [#3326](https://github.com/vllm-project/vllm/issues/3326) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Serving multiple models in vLLM with single or multiple engines

### Issue 正文摘录

Is it possible to serve multiple models inside vLLM? It would be nice to choose which GPUs should load which model. My guess is no since the rest of gpu memory is reserved for the single model's kv cache

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ose which GPUs should load which model. My guess is no since the rest of gpu memory is reserved for the single model's kv cache
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Serving multiple models in vLLM with single or multiple engines Is it possible to serve multiple models inside vLLM? It would be nice to choose which GPUs should load which model. My guess is no since the rest of gpu me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
