# vllm-project/vllm#18348: [Bug]: vLLM lacks eviction policy for MooncakeStore

| 字段 | 值 |
| --- | --- |
| Issue | [#18348](https://github.com/vllm-project/vllm/issues/18348) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM lacks eviction policy for MooncakeStore

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Disaggregated prefill and decoding with Mooncake only succeeds for a small number of initial queries, after which performance deteriorates. According to the [Mooncake documentation](https://github.com/kvcache-ai/Mooncake/blob/main/doc/en/mooncake-store-preview.md), the mooncake store API has a 3 function semantics: put/get/remove and caching strategies (e.g., eviction policies) are left to upper-layer frameworks (like vLLM). However, the vLLM `KVStoreBufferBase` API uses a 2 function semantics: put/get. Get does not imply remove, and in fact vLLM does not implement any eviction policy. This causes the cache to fill up with already used data. When the store becomes full, any further allocations fail. ``` allocator.cpp:189] allocation_failed size=16777200 Master Metrics: Storage: 63.64 GB / 64.00 GB (99.4%) | Keys: 117 | Requests (Success/Total): Put=234/421, Get=221/304, Exist=0/0, Del=0/0, DelAll=0/0 ``` Decoding still succeeds, there is no crash. However, decoding performance is impacted: the prefill instance(s) are unable to store the new KV-cache entries, causing the decoding instance(s) to fail to retrieve them. ```[engine.py...

## 现有链接修复摘要

#18349 Remove used KV cache from MooncakeStore to prevent overfill

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vLLM lacks eviction policy for MooncakeStore bug;stale ### Your current environment ### 🐛 Describe the bug Disaggregated prefill and decoding with Mooncake only succeeds for a small number of initial queries, aft...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ion semantics: put/get/remove and caching strategies (e.g., eviction policies) are left to upper-layer frameworks (like vLLM). However, the vLLM `KVStoreBufferBase` API uses a 2 function semantics: put/get. Get does not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ug Disaggregated prefill and decoding with Mooncake only succeeds for a small number of initial queries, after which performance deteriorates. According to the [Mooncake documentation](https://github.com/kvcache-ai/Moon...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ormance is impacted: the prefill instance(s) are unable to store the new KV-cache entries, causing the decoding instance(s) to fail to retrieve them. ```[engine.py:160] Exception: Failed to retrieve remote_kv 1222197876...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: orting;model_support;scheduler_memory;speculative_decoding cuda;operator;triton build_error;crash env_dependency #18349 Remove used KV cache from MooncakeStore to prevent overfill Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18349](https://github.com/vllm-project/vllm/pull/18349) | closes_keyword | 0.95 | Remove used KV cache from MooncakeStore to prevent overfill | FIX #18348 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
