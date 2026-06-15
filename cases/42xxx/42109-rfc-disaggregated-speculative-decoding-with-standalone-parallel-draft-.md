# vllm-project/vllm#42109: [RFC]: Disaggregated Speculative Decoding with Standalone Parallel Draft Model

| 字段 | 值 |
| --- | --- |
| Issue | [#42109](https://github.com/vllm-project/vllm/issues/42109) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Disaggregated Speculative Decoding with Standalone Parallel Draft Model

### Issue 正文摘录

### Motivation. Speculative decoding in vLLM today co-locates the draft model with the target: the draft runs on the target's TP group, competes for the same SMs / HBM bandwidth, and is driven by the target's scheduler. This is efficient for small draft models (EAGLE, MTP), but has two structural limits: 1. **Draft compute steals from target compute.** On a TP=2 Llama-3-70B target at high concurrency, a 1B–8B draft can add 10–30% to per-step latency on the target GPUs even when the draft itself is idle-compute-bound, because it shares the forward-pass critical path. 2. **Cache-build parallelism is capped by the target's schedule.** Any "predict what the target will verify next round" caching scheme has to complete between target steps — the draft cannot run ahead. Disaggregated speculative decoding (**Disagg-SD**) moves the draft model to a dedicated GPU (or pool of GPUs) reached over a fast interconnect (ZMQ + shared host for same-node, RDMA for cross-node). The target sends a *verification outcome* after each step; the draft server returns *K draft tokens per request* from a **speculation cache** that was pre-built while the target was verifying the previous round. This gives: -...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Disaggregated Speculative Decoding with Standalone Parallel Draft Model RFC ### Motivation. Speculative decoding in vLLM today co-locates the draft model with the target: the draft runs on the target's TP group,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: 70B target at high concurrency, a 1B–8B draft can add 10–30% to per-step latency on the target GPUs even when the draft itself is idle-compute-bound, because it shares the forward-pass critical path. 2. **Cache-build pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Disaggregated Speculative Decoding with Standalone Parallel Draft Model RFC ### Motivation. Speculative decoding in vLLM today co-locates the draft model with the target: the draft runs on the target's TP group,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: . - Holds a `DraftRouter` with one `ZmqDraftConnector` per draft server. Routing policies: `round_robin` (default) and `affinity` (stable mapping by `hash(verify_server_id) mod num_drafts`). - After each target step, se...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: CULATE` calls (i.e. `d > v`, *and* no amount of pipelining can hide it — cache hits start missing and fall back to JIT). This sets the upper bound on draft model size / fan-out budget for a given target throughput. Anot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
