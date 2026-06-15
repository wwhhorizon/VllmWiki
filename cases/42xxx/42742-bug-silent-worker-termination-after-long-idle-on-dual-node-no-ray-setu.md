# vllm-project/vllm#42742: [Bug]: Silent worker termination after long idle on dual-node `--no-ray` setup (likely `TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC` SIGABRT)

| 字段 | 值 |
| --- | --- |
| Issue | [#42742](https://github.com/vllm-project/vllm/issues/42742) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;quantization |
| 症状 | oom |
| 根因提示 | dtype;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Silent worker termination after long idle on dual-node `--no-ray` setup (likely `TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC` SIGABRT)

### Issue 正文摘录

## Your current environment ## 🐛 Describe the bug On a 2-node `--no-ray` vLLM serving setup, the head-node worker process **dies silently** after an extended idle period. The container stays "Up" because the API server process continues running briefly, but the engine is dead and all subsequent requests fail. **Specifically observed timeline (UTC):** | Time | Event | | --- | --- | | 09:15:56 | Last successful request completes. Engine 000 reports `Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%` | | 09:15:56 → 11:48:32 | **2 h 32 m of zero traffic.** No log entries on either node during this window. | | 11:48:32 | `(Worker_TP0 pid=193) WARNING multiproc_executor.py:884 WorkerProc was terminated` — no preceding error | | 11:48:45 | `(EngineCore pid=143) ERROR multiproc_executor.py:283 Worker proc VllmWorker-0 died unexpectedly, shutting down executor.` | | 11:48:46 | `RuntimeError: Executor failed.` → `vllm.v1.engine.exceptions.EngineDeadError` → APIServer shutdown | | 12:45:04+ | On worker-rank-1 (gx10-node2): `ProcessGroupNCCL::HeartbeatMonitor::runLoop()` starts logging `TCPStore: sendBytes failed on SocketImpl(... remote=[192.168.0.72]:29501): Broken pipe` — rank 1's...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: on_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization cache;cuda;fp8;kernel;moe;quantization oom dtype;memory_layout;race_condition Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ess continues running briefly, but the engine is dead and all subsequent requests fail. **Specifically observed timeline (UTC):** | Time | Event | | --- | --- | | 09:15:56 | Last successful request completes. Engine 000...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: briefly, but the engine is dead and all subsequent requests fail. **Specifically observed timeline (UTC):** | Time | Event | | --- | --- | | 09:15:56 | Last successful request completes. Engine 000 reports `Running: 0 r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ead head ~1 hour after the head's death | **Critical: no preceding NCCL/CUDA error log, no Xid in dmesg, no kernel OOM kill, no SIGTERM from container runtime.** The only log line at the moment of death is `WorkerProc w...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: est completes. Engine 000 reports `Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%` | | 09:15:56 → 11:48:32 | **2 h 32 m of zero traffic.** No log entries on either node during this window. | | 11:48:32 | `(W...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
