# vllm-project/vllm#497: bloom-1b7 offline inference error

| 字段 | 值 |
| --- | --- |
| Issue | [#497](https://github.com/vllm-project/vllm/issues/497) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> bloom-1b7 offline inference error

### Issue 正文摘录

![微信图片_20230718191039](https://github.com/vllm-project/vllm/assets/50452258/8a7306d1-ff4b-4971-b0c8-5d3e6174bdc5)

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: bloom-1b7 offline inference error bug ![微信图片_20230718191039](https://github.com/vllm-project/vllm/assets/50452258/8a7306d1-ff4b-4971-b0c8-5d3e6174bdc5)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
