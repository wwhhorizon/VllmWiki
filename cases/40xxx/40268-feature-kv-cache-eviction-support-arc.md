# vllm-project/vllm#40268: [Feature]: KV Cache Eviction support ARC

| 字段 | 值 |
| --- | --- |
| Issue | [#40268](https://github.com/vllm-project/vllm/issues/40268) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: KV Cache Eviction support ARC

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## 1. The Problem ### 1.1 Pain Point: LRU Has No Memory of How Hot a Block Was vLLM's GPU KV cache (`BlockPool`) uses a **single-queue LRU** implemented in`FreeKVCacheBlockQueue`. When a request finishes, its blocks are appended to the tail of the free queue. When new blocks are needed, eviction drains from the head. This design has one fundamental blind spot: **once `ref_cnt` drops to zero, all blocks are equal candidates for eviction, regardless of how many times they were previously reused.** A system-prompt block touched by 10,000 requests and a one-time-use block are indistinguishable at eviction time. ### 1.2 Pain Point: Burst Requests Cause Scan Pollution In production, LLM serving commonly experiences **bursty traffic**: a wave of requests with unique prompts arrives simultaneously, each generating a large number of KV blocks that immediately become eviction candidates. These low-value blocks flood the tail of the free queue, pushing high-value cached prefix blocks toward the eviction head. This is the classic **scan pollution** problem, well-known in OS page-cache literature. Linux solved it decades ago with the Active/Inactive list...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: KV Cache Eviction support ARC feature request ### 🚀 The feature, motivation and pitch ## 1. The Problem ### 1.1 Pain Point: LRU Has No Memory of How Hot a Block Was vLLM's GPU KV cache (`BlockPool`) uses a **...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Feature]: KV Cache Eviction support ARC feature request ### 🚀 The feature, motivation and pitch ## 1. The Problem ### 1.1 Pain Point: LRU Has No Memory of How Hot a Block Was vLLM's GPU KV cache (`BlockPool`) uses a **...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cture BlockPool └── free_block_queue: FreeKVCacheBlockQueue # one doubly-linked list head (evict first) ←——————————————— tail (evict last) [ old cold blocks ] ... [ recently freed blocks ] The "reverse-order free" heuri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ict another's hot prefix | --- ## 2. Root Cause Analysis ### 2.1 Current Architecture BlockPool └── free_block_queue: FreeKVCacheBlockQueue # one doubly-linked list head (evict first) ←——————————————— tail (evict last)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ch ## 1. The Problem ### 1.1 Pain Point: LRU Has No Memory of How Hot a Block Was vLLM's GPU KV cache (`BlockPool`) uses a **single-queue LRU** implemented in`FreeKVCacheBlockQueue`. When a request finishes, its blocks...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
