# vllm-project/vllm#2342: when --gpu-memory-utilization is set to 0.9, while actually  the fraction of  gpu memory utilization is more than 0.9

| 字段 | 值 |
| --- | --- |
| Issue | [#2342](https://github.com/vllm-project/vllm/issues/2342) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> when --gpu-memory-utilization is set to 0.9, while actually  the fraction of  gpu memory utilization is more than 0.9

### Issue 正文摘录

![微信图片_20240104164759](https://github.com/vllm-project/vllm/assets/22477246/971416ee-23b0-4142-b1d8-a872533c302d)

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: --gpu-memory-utilization is set to 0.9, while actually the fraction of gpu memory utilization is more than 0.9 ![微信图片_20240104164759](https://github.com/vllm-project/vllm/assets/22477246/971416ee-23b0-4142-b1d8-a872533c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
