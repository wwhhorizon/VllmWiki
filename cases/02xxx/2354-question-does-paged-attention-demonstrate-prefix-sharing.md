# vllm-project/vllm#2354: Question: Does paged attention demonstrate prefix sharing? 

| 字段 | 值 |
| --- | --- |
| Issue | [#2354](https://github.com/vllm-project/vllm/issues/2354) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: Does paged attention demonstrate prefix sharing? 

### Issue 正文摘录

Reading https://arxiv.org/abs/2311.04934 and wondering if I would gain anything from prompt cache. My use case is having prompts with overlaping prefixes (mostly a few big ones). And I already use vllm paged attention. Assuming I would only want to cache kv states for prefixes (not positioned anywhere like in the paper). Would there be any gains in caching attention prefix states, or is paged attention and vllm indeed already doing this? Paper: ``` Paged attention also demonstrates simple prefix sharing, where different prompts with an identical prefix share KV Cache ``` Goal: ``` shared inputs with prompt1 | | +---------------------------------+ +-----+------+--------------------+ | | ... | ////|///// | | +---------------------------------+ +------------+--------------------+ prompt 1 prompt 2 request 1 request 2 - store prefix->kvs - request - find shared inputs - assert_kv_cache(prefix-kvs) Any gain from this idea? ``` So do we with paged attention already skip the attention for the shared inputs, or is there anything to be gainend from additionally caching prefix kvs? If it already caches across requests, what is the mechanism that keeps kv-cache entries from busting? Wonderin...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: e prefix sharing, where different prompts with an identical prefix share KV Cache ``` Goal: ``` shared inputs with prompt1 | | +-------------------------
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Question: Does paged attention demonstrate prefix sharing? stale Reading https://arxiv.org/abs/2311.04934 and wondering if I would gain anything from prompt cache. My use case is having prompts with overlaping prefixes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng prefix kvs? If it already caches across requests, what is the mechanism that keeps kv-cache entries from busting? Wondering if there are still potential tweaks to make to make sure certain prefixes stay in `kv-cache`.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
