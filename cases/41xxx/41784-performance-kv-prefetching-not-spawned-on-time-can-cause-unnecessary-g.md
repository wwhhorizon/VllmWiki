# vllm-project/vllm#41784: [Performance]: KV prefetching not spawned on time can cause unnecessary GPU idle

| 字段 | 值 |
| --- | --- |
| Issue | [#41784](https://github.com/vllm-project/vllm/issues/41784) |
| 状态 | open |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: KV prefetching not spawned on time can cause unnecessary GPU idle

### Issue 正文摘录

### Proposal to improve performance When using vLLM with LMCache, KV prefetching is spawned in the below snippet: ``` if request.num_computed_tokens == 0: # Get locally-cached tokens. new_computed_blocks, num_new_local_computed_tokens = ( self.kv_cache_manager.get_computed_blocks(request) ) # Get externally-cached tokens if using a KVConnector. if self.connector is not None: ext_tokens, load_kv_async = ( self.connector.get_num_new_matched_tokens( request, num_new_local_computed_tokens ) ) ``` vLLM's scheduler, when trying to form a batch, polls the `running` queue first, then `skipped_waiting` and `waiting` queues. If there are sufficient tokens in the `running` queue, the other two queues won't even be checked, meaning the prefetch of newly joined requests in the wait queue are not scheduled on time. Under heavy workloads where KV caches are read from disk, this can cause unnecessary GPU idle due to KV waiting, as illustrated by the below log (I added some loggings by myself): ``` (EngineCore pid=1907951) DEBUG 05-04 05:25:02 [v1/core/sched/scheduler.py:570] schedule step 3748 running queue: (EngineCore pid=1907951) DEBUG 05-04 05:25:02 [v1/core/sched/scheduler.py:572] running qu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LLM with LMCache, KV prefetching is spawned in the below snippet: ``` if request.num_computed_tokens == 0: # Get locally-cached tokens. new_computed_blocks, num_new_local_computed_tokens = ( self.kv_cache_manager.get_co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Stored 6144 out of total 6144 tokens. size: 0.1875 GB, cost 16.8434 ms, throughput: 11.1320 GB/s; offload_time: 15.9973 ms, put_time: 0.8122 ms [3m(cache_engine.py:552:lmcache.v1.cache_engine)[0m (Worker_TP2 pid=19083...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ue first, then `skipped_waiting` and `waiting` queues. If there are sufficient tokens in the `running` queue, the other two queues won't even be checked, meaning the prefetch of newly joined requests in the wait queue a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: G 05-04 05:25:02 [v1/worker/gpu_model_runner.py:3888] Running batch with cudagraph_mode: NONE, batch_descriptor: BatchDescriptor(num_tokens=6144, num_reqs=None, uniform=False, has_lora=False, num_active_loras=0), should...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: n the wait queue are not scheduled on time. Under heavy workloads where KV caches are read from disk, this can cause unnecessary GPU idle due to KV waiting, as illustrated by the below log (I added some loggings by myse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
