# vllm-project/vllm#3021: multi round decoding question

| 字段 | 值 |
| --- | --- |
| Issue | [#3021](https://github.com/vllm-project/vllm/issues/3021) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> multi round decoding question

### Issue 正文摘录

Hi, dear developers, thanks for reading my question! I have question about multi round decoding. we send a prompt to generate, (1. flash attn encode prompt 2. paged attn, single query decode) but after the step, I continue send a prompt and want to use all before paged kv cache, how should I write the code. Is there any existing api to do this?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: fter the step, I continue send a prompt and want to use all before paged kv cache, how should I write the code. Is there any existing api to do this?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t to generate, (1. flash attn encode prompt 2. paged attn, single query decode) but after the step, I continue send a prompt and want to use all before paged kv cache, how should I write the code. Is there any existing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
