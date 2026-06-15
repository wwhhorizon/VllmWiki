# vllm-project/vllm#29608: [Bug]: CUDA Graph Replay Skips KV Transfer Synchronization in Full Cache Hit Scenarios

| 字段 | 值 |
| --- | --- |
| Issue | [#29608](https://github.com/vllm-project/vllm/issues/29608) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Graph Replay Skips KV Transfer Synchronization in Full Cache Hit Scenarios

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using asynchronous KV transfer connectors with full cache hits, CUDA graph replay can skip the `wait_for_layer_load()` synchronization, leading to potential data races where attention operations use incompletely loaded KV caches. - vLLM version: [v1] - KV Connector: Asynchronous KV transfer （`wait_for_laeyr_load()` support) - CUDA Graph mode: Enabled (FULL, FULL_AND_PIECEWISE, or FULL_DECODE_ONLY) When a request has a full KV cache hit, connectors typically reserve 1 token for the scheduler (as 0-token scheduling is not allowed). In `gpu_model_runner.py:_determine_batch_execution_and_padding()`: ``` uniform_decode = ( (max_num_scheduled_tokens == self.uniform_decode_query_len) # 1 == 1 ✓ and (num_tokens_padded == max_num_scheduled_tokens * num_reqs) # 1 == 1×1 ✓ ) ``` When CUDA graph replays (in `compilation/cuda_graph.py:207-208`): ``` entry.cudagraph.replay() return entry.outputThe replay **directly executes the captured GPU operations** without calling `self.runnable(*args, **kwargs)`, which means: - `unified_attention()` functions are not executed - `@maybe_transfer_kv_layer` decorator is bypassed - **`wait_for_layer_loa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Replay Skips KV Transfer Synchronization in Full Cache Hit Scenarios bug;stale ### Your current environment ### 🐛 Describe the bug When using asynchronous KV transfer connectors with full cache hits, CUDA graph replay c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: es where attention operations use incompletely loaded KV caches. - vLLM version: [v1] - KV Connector: Asynchronous KV transfer （`wait_for_laeyr_load()` support) - CUDA Graph mode: Enabled (FULL, FULL_AND_PIECEWISE, or F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA Graph Replay Skips KV Transfer Synchronization in Full Cache Hit Scenarios bug;stale ### Your current environment ### 🐛 Describe the bug When using asynchronous KV transfer connectors with full cache hits, C...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: CUDA Graph Replay Skips KV Transfer Synchronization in Full Cache Hit Scenarios bug;stale ### Your current environment ### 🐛 Describe the bug When using asynchronous KV transfer connectors with full cache hits, C...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: potential data races where attention operations use incompletely loaded KV caches. - vLLM version: [v1] - KV Connector: Asynchronous KV transfer （`wait_for_laeyr_load()` support) - CUDA Graph mode: Enabled (FULL, FULL_A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
