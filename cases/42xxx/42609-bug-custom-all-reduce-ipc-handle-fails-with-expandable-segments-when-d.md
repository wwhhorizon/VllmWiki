# vllm-project/vllm#42609: [Bug] custom_all_reduce IPC handle fails with expandable_segments when DP>1 AND TP>1

| 字段 | 值 |
| --- | --- |
| Issue | [#42609](https://github.com/vllm-project/vllm/issues/42609) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] custom_all_reduce IPC handle fails with expandable_segments when DP>1 AND TP>1

### Issue 正文摘录

## Summary With `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`, starting vllm with both DP>1 and TP>1 crashes during worker init in `custom_all_reduce.cuh:455` (`cudaIpcGetMemHandle` returns `invalid argument`). Either dim alone works. ## Environment - vllm 0.20.2 - 4× H200 (1 node) ## Repro ```bash PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve Qwen/Qwen3-0.6B --data-parallel-size 2 --tensor-parallel-size 2 ``` ``` Failed: Cuda error custom_all_reduce.cuh:455 'invalid argument' EngineCore failed to start: Worker proc VllmWorker-* died unexpectedly ``` ## Matrix (Qwen3-0.6B, expandable_segments enabled) | DP | TP | result | |----|----|--------| | 2 | 1 | ✓ | | 1 | 2 | ✓ | | 2 | 2 | ✗ (crash as above) | Independent of `--enable-sleep-mode` (reproduced with and without it). ## Root cause (best guess) `expandable_segments` reserves virtual address ranges via `cuMemAddressReserve` and commits physical memory lazily with `cuMemMap`. The base pointer returned by `cuPointerGetAttribute(..., rangeStartAddrAttr, ...)` in `get_graph_buffer_ipc_meta` is the head of such a VA range, which is not a valid source for `cudaIpcGetMemHandle` — IPC handles require memory backed by...

## 现有链接修复摘要

#40812 Auto-disable expandable_segments around cumem memory pool | #43923 [Bugfix] Fix crash with PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True set and custom_allreduce enabled

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tered, or detect the cumem-backed pointer and skip custom-all-reduce IPC fallback. @youkaichao could you take a look? performance distributed_parallel;scheduler_memory cuda crash shape #40812 Auto-disable expandable_seg...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: | 2 | 2 | ✗ (crash as above) | Independent of `--enable-sleep-mode` (reproduced with and without it). ## Root cause (best guess) `expandable_segments` reserves virtual address ranges via `cuMemAddressReserve` and commit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls with expandable_segments when DP>1 AND TP>1 ## Summary With `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`, starting vllm with both DP>1 and TP>1 crashes during worker init in `custom_all_reduce.cuh:455` (`cudaIp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o ```bash PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve Qwen/Qwen3-0.6B --data-parallel-size 2 --tensor-parallel-size 2 ``` ``` Failed: Cuda error custom_all_reduce.cuh:455 'invalid argument' EngineCore...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ck. @youkaichao could you take a look? performance distributed_parallel;scheduler_memory cuda crash shape #40812 Auto-disable expandable_segments around cumem memory pool | #43923 [Bugfix] Fix crash with PYTORCH_CUDA_AL...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40812](https://github.com/vllm-project/vllm/pull/40812) | mentioned | 0.45 | Auto-disable expandable_segments around cumem memory pool | egments` or pass `--disable-custom-all-reduce`. ## suggested fix pr #40812 already temporarily disables `expandable_segments` around the cumem sleep-mode pool. the `custom_all_red… |
| [#43923](https://github.com/vllm-project/vllm/pull/43923) | closes_keyword | 0.95 | [Bugfix] Fix crash with PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True set and custom_allreduce enabled | Fixes #42609. Launching vLLM with `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` while custom allreduce is active (tensor or data parallelism) crashes at startup during CUDA |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
