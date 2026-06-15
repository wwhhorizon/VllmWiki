# vllm-project/vllm#41951: [Bug]:  v1 Scheduler: preempted requests lose re-admission priority in PriorityRequestQueue, causing redundant recompute

| 字段 | 值 |
| --- | --- |
| Issue | [#41951](https://github.com/vllm-project/vllm/issues/41951) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  v1 Scheduler: preempted requests lose re-admission priority in PriorityRequestQueue, causing redundant recompute

### Issue 正文摘录

### Your current environment vLLM version: Main branch (built from source) OS: macOS (Darwin 25.4.0) Python version: 3.12.8 PyTorch version: 2.8.0 CUDA available: False Note: collect_env.py failed to run locally because my environment is partially unbuilt, but this is a pure Python logic issue in the v1 core scheduler, so hardware/CUDA specifics are not applicable. ### 🐛 Describe the bug ## Bug description ## What happened? In the v1 engine, when using the default SchedulingPolicy.PRIORITY, preempted requests lose their execution priority and can be starved by newly waiting requests that happen to have an earlier arrival_time. Currently, Request.__lt__ sorts by priority and then arrival_time, but completely ignores num_preemptions. If a request A is scheduled but gets preempted, it gets thrown back into the heap. If there is a request B with the same priority that arrived earlier but hadn't started yet, B will be scheduled before A. This causes A's partially computed KV cache blocks to be evicted under memory pressure, resulting in wasted GPU compute. _(Note: While the current documentation and code state that num_preemptions is only used for statistics, relying solely on arrival_...

## 现有链接修复摘要

#41952 [Core] Prioritize preempted requests in v1 Scheduler Priority Queue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ueue, causing redundant recompute bug ### Your current environment vLLM version: Main branch (built from source) OS: macOS (Darwin 25.4.0) Python version: 3.12.8 PyTorch version: 2.8.0 CUDA available: False Note: collec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: v1 Scheduler: preempted requests lose re-admission priority in PriorityRequestQueue, causing redundant recompute bug ### Your current environment vLLM version: Main branch (built from source) OS: macOS (Darwin 25...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OS: macOS (Darwin 25.4.0) Python version: 3.12.8 PyTorch version: 2.8.0 CUDA available: False Note: collect_env.py failed to run locally because my environment is partially unbuilt, but this is a pure Python logic issue...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ed yet, B will be scheduled before A. This causes A's partially computed KV cache blocks to be evicted under memory pressure, resulting in wasted GPU compute. _(Note: While the current documentation and code state that...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 25.4.0) Python version: 3.12.8 PyTorch version: 2.8.0 CUDA available: False Note: collect_env.py failed to run locally because my environment is partially unbuilt, but this is a pure Python logic issue in the v1 core sc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41952](https://github.com/vllm-project/vllm/pull/41952) | closes_keyword | 0.95 | [Core] Prioritize preempted requests in v1 Scheduler Priority Queue | Fixes #41951 --- ## Problem In `PriorityRequestQueue`, `prepend_request()` is a standard `heapq.heappush`. Because `Request.__lt__` previously ignored `num_preemptions`, |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
