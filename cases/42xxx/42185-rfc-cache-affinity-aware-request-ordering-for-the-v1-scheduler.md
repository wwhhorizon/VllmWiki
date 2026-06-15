# vllm-project/vllm#42185: [RFC]: Cache-affinity-aware request ordering for the V1 scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#42185](https://github.com/vllm-project/vllm/issues/42185) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Cache-affinity-aware request ordering for the V1 scheduler

### Issue 正文摘录

# [RFC]: Cache-affinity-aware request ordering for the V1 scheduler ## Summary A `CacheAffinityScheduler` plugin loadable via `--scheduler-cls` that reorders the V1 waiting queue by cached-prefix length before each scheduling iteration. In-engine equivalent of sglang's RadixAttention scheduling, on top of vLLM's existing block-hash prefix cache. No token-level radix tree, no KV cache manager surgery, no request-schema changes. ## Motivation vLLM has block-level prefix caching ([docs](https://docs.vllm.ai/en/stable/design/prefix_caching/)), but the V1 scheduler admits waiting requests in priority + FCFS order. A waiting request with thousands of cached prefix tokens is treated identically to a request with no cached prefix — the prefill savings are left on the table when the cache-warm request waits behind a cache-cold one. Issue [#7883](https://github.com/vllm-project/vllm/issues/7883) (open since Aug 2024) identified the budget-calculation half of this problem; the in-flight `[1/n]` series fixes `can_allocate` to consider cached blocks. **Waiting-queue ordering is the other half** and is not addressed by that series — confirmed by reading the merged commits. External evidence the...

## 现有链接修复摘要

#5958 [Core] Adding Priority Scheduling

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Cache-affinity-aware request ordering for the V1 scheduler # [RFC]: Cache-affinity-aware request ordering for the V1 scheduler ## Summary A `CacheAffinityScheduler` plugin loadable via `--scheduler-cls` that reor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ting (default edges `(4, 16, 64, 256)`) prevents per-iteration thrash on small score deltas. Sticky-front semantics preserve the V1 invariant that preempted requests are scheduled first in their preemption order. ## Des...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ivalent of sglang's RadixAttention scheduling, on top of vLLM's existing block-hash prefix cache. No token-level radix tree, no KV cache manager surgery, no request-schema changes. ## Motivation vLLM has block-level pre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: cheduling](https://www.lmsys.org/blog/2024-01-17-sglang/) reports 10–30% throughput uplift on multi-turn / RAG / agentic workloads by reordering requests so those with longer cached prefixes execute first. - Multiple co...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: sglang's RadixAttention scheduling, on top of vLLM's existing block-hash prefix cache. No token-level radix tree, no KV cache manager surgery, no request-schema changes. ## Motivation vLLM has block-level prefix caching...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5958](https://github.com/vllm-project/vllm/pull/5958) | mentioned | 0.45 | [Core] Adding Priority Scheduling | eue. different layers. - **compatible with** priority scheduling ([pr #5958](https://github.com/vllm-project/vllm/pull/5958), [pr #19057](https://github.com/vllm-project/vllm/pull… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
