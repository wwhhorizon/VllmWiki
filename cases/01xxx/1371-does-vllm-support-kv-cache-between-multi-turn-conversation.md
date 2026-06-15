# vllm-project/vllm#1371: Does vllm support KV-cache between multi-turn conversation

| 字段 | 值 |
| --- | --- |
| Issue | [#1371](https://github.com/vllm-project/vllm/issues/1371) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does vllm support KV-cache between multi-turn conversation

### Issue 正文摘录

Hello, in many cases, we need to take multi-turn conversation. That is, the output of the first step will be added to the input of the second step. Could you please tell me whether the common part of the multi-turn conversation will be cached?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Does vllm support KV-cache between multi-turn conversation Hello, in many cases, we need to take multi-turn conversation. That is, the output of the first step will be added to the input of the second step. Could you pl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
