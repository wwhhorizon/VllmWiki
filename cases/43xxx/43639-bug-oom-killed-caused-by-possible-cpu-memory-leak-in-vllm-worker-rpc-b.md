# vllm-project/vllm#43639: [Bug]: OOM killed caused by possible CPU memory leak in vLLM Worker RPC Broadcast Deserialization Path

| 字段 | 值 |
| --- | --- |
| Issue | [#43639](https://github.com/vllm-project/vllm/issues/43639) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM killed caused by possible CPU memory leak in vLLM Worker RPC Broadcast Deserialization Path

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary We observed steady CPU RSS growth in a vLLM worker process during production traffic. A short sampling window using `pmap`, `/proc/ /status`, `/proc/ /smaps_rollup`, and `memray --leaks` points to retained anonymous private memory allocated while the worker is deserializing RPC broadcast messages. The most suspicious path is not NIXL, file cache, shared memory, pinned memory, or the model `execute_model` path itself. The largest retained allocations are under: ```text worker_busy_loop -> rpc_broadcast_mq.dequeue(...) -> MessageQueue.recv(...) -> pickle.loads(...) ``` During the sampling window, OS-level memory growth and memray retained allocations are closely aligned: - Worker RSS / Private_Dirty increased by roughly **93-108 MiB**. - `memray --leaks` reported roughly **115.5 MiB** of still-live allocations. - Most retained memory came from: - `_PyMem_ArenaAlloc`: about **73 MiB** - `c10::alloc_cpu`: about **38.6 MiB** This suggests the leak is likely caused by Python objects and Torch CPU tensor storage created by RPC message deserialization and retained after the sampled window. ## OS-level memory evidence ### `/pro...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: 0516 kB (~107.93 MiB) Dirty: +110520 kB (~107.93 MiB) ``` Aggregating mappings by type showed almost all growth came from `rw--- [ anon ]` private anonymous mappings: ```text anon: +109.25 MiB Size, +107.39 MiB RSS, +10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: allocations are under: ```text worker_busy_loop -> rpc_broadcast_mq.dequeue(...) -> MessageQueue.recv(...) -> pickle.loads(...) ``` During the sampling window, OS-level memory growth and memray retained allocations are...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: while the worker is deserializing RPC broadcast messages. The most suspicious path is not NIXL, file cache, shared memory, pinned memory, or the model `execute_model` path itself. The largest retained allocations are un...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: raffic. A short sampling window using `pmap`, `/proc/ /status`, `/proc/ /smaps_rollup`, and `memray --leaks` points to retained anonymous private memory allocated while the worker is deserializing RPC broadcast messages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: cious path is not NIXL, file cache, shared memory, pinned memory, or the model `execute_model` path itself. The largest retained allocations are under: ```text worker_busy_loop -> rpc_broadcast_mq.dequeue(...) -> Messag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
