# vllm-project/vllm#736: gpu consumption

| 字段 | 值 |
| --- | --- |
| Issue | [#736](https://github.com/vllm-project/vllm/issues/736) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> gpu consumption

### Issue 正文摘录

when i loaded a 7B model with 3090(24G), i found that gpu memory cost around 18G. I know the extra memory is used for KV cache, but i have 2 confusion. 1. why 18G, as i know, it will cost 0.9 * 24G = 21.6G 2. in [https://github.com/vllm-project/vllm/discussions/241](241), we can limit the GPU memory usage by setting the parameter gpu_memory_utilization. but i set gpu_memory_utilization 0.7, i get oom. 0.7 * 24G > 14G. if vllm must cost more memory? and shouldn't pageattention reduce memory?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: gpu consumption when i loaded a 7B model with 3090(24G), i found that gpu memory cost around 18G. I know the extra memory is used for KV cache, but i have 2 confusion. 1. why 18G, as i know, it will cost 0.9 * 24G = 21....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gpu consumption when i loaded a 7B model with 3090(24G), i found that gpu memory cost around 18G. I know the extra memory is used for KV cache, but i have 2 confusion. 1. why 18G, as i know, it will cost 0.9 * 24G = 21....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
