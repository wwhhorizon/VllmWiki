# vllm-project/vllm#41535: RFC: Memory-backend interface for KV cache hot paths and attention decode

| 字段 | 值 |
| --- | --- |
| Issue | [#41535](https://github.com/vllm-project/vllm/issues/41535) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RFC: Memory-backend interface for KV cache hot paths and attention decode

### Issue 正文摘录

### Motivation. Hi vLLM team, I am experimenting with a TurboQuant-compatible memory backend evaluation path, focused on KV-cache residency, kv_dot, and attention decode hot-path pressure. The goal is not to replace vLLM’s scheduler or execution model, but to explore whether selected KV-cache / attention-decode operations can be routed through an external memory-centric backend while keeping fallback-safe behavior. Current evaluation repository: https://github.com/ixu2486/tq_compat_eval The current direction includes: - KV-cache hot-path analysis - TurboQuant-compatible evaluation layout - memory-backend routing experiments - PIM-compatible execution path exploration - fallback-safe CPU/backend comparison - future compatibility with larger-context inference and speculative decoding pressure points If the vLLM team or maintainers are interested in testing this direction, please reply here. I can add the relevant personnel to this project repository for evaluation access. I would also appreciate guidance on whether this kind of work would fit better as: - an external backend experiment - a plugin-style integration - a future RFC - or a benchmark/evaluation-only companion project Tha...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: RFC: Memory-backend interface for KV cache hot paths and attention decode RFC ### Motivation. Hi vLLM team, I am experimenting with a TurboQuant-compatible memory backend evaluation path, focused on KV-cache residency,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: RFC: Memory-backend interface for KV cache hot paths and attention decode RFC ### Motivation. Hi vLLM team, I am experimenting with a TurboQuant-compatible memory backend evaluation path, focused on KV-cache residency,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: LM team, I am experimenting with a TurboQuant-compatible memory backend evaluation path, focused on KV-cache residency, kv_dot, and attention decode hot-path pressure. The goal is not to replace vLLM’s scheduler or exec...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: RFC: Memory-backend interface for KV cache hot paths and attention decode RFC ### Motivation. Hi vLLM team, I am experimenting with a TurboQuant-compatible memory backend evaluation path, focused on KV-cache residency,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nel to this project repository for evaluation access. I would also appreciate guidance on whether this kind of work would fit better as: - an external backend experiment - a plugin-style integration - a future RFC - or...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
