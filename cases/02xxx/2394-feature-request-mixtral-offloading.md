# vllm-project/vllm#2394:  [Feature Request] Mixtral Offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#2394](https://github.com/vllm-project/vllm/issues/2394) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  [Feature Request] Mixtral Offloading

### Issue 正文摘录

There's a new cache technique mentioned in the paper https://arxiv.org/abs/2312.17238. (github: https://github.com/dvmazur/mixtral-offloading) They introduced LRU cache to cache experts based on patterns they found, and also took speculative guess to pre-load experts before the computation of the next layer. The result looks quite promising. Can we support it for Mixtral? This helps a lot to run on smaller GPUs.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature Request] Mixtral Offloading feature request;stale There's a new cache technique mentioned in the paper https://arxiv.org/abs/2312.17238. (github: https://github.com/dvmazur/mixtral-offloading) They introduced L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ite promising. Can we support it for Mixtral? This helps a lot to run on smaller GPUs.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature Request] Mixtral Offloading feature request;stale There's a new cache technique mentioned in the paper https://arxiv.org/abs/2312.17238. (github: https://github.com/dvmazur/mixtral-offloading) They introduced L...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ithub.com/dvmazur/mixtral-offloading) They introduced LRU cache to cache experts based on patterns they found, and also took speculative guess to pre-load experts before the computation of the next layer. The result loo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
