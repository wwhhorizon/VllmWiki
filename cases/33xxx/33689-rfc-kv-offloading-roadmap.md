# vllm-project/vllm#33689: [RFC]: KV Offloading Roadmap

| 字段 | 值 |
| --- | --- |
| Issue | [#33689](https://github.com/vllm-project/vllm/issues/33689) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: KV Offloading Roadmap

### Issue 正文摘录

Currently supported features: - [x] Pluggable out-of-tree offloading backend - [x] CPU-GPU Offloading (NVIDIA+AMD) - [x] Custom offloading block size - [x] Fully asynchronous (cross-engine-steps) offloading / loading - [x] Immediate Offloading (as opposed to spill-over) - [x] LRU Eviction - [x] Cross layer blocks - [x] Metrics - [x] Onloading preempted requests - [x] KV Events - [x] Kernel-block-size support - [x] Abstract eviction strategy (LRU, ARC, etc.) - [x] HMA Support Upcoming: - [ ] Documentation - [ ] Extend cross layers to hybrid models - [ ] Support tiering (e.g. CPU -> Pluggable backend) Backlog: - [ ] Create an offloading policy abstraction - [ ] Preemption-only offload mode (old PR: #32398) - [ ] Spillover mode (swap-in swap-out) Tactical tasks: - [x] Move `worker/cpu_gpu.py` to `cpu/gpu_worker.py` - [x] Remove `mediums.py`. Move `GPULoadStoreSpec` to `abstract.py`, `CPULoadStoreSpec` to `cpu/spec.py`. - [x] Remove `kv_offload/spec.py`. Move to `abstract.py`. - [x] Rename `abstract.py` to `base.py` (as well as in `cpu/policies`). - [x] Move `reuse_manager.py` into `cpu/manager.py`. - [x] Add `request_finished` method to `OffloadingManager`. - [ ] Remove `kv_offload/w...

## 现有链接修复摘要

#41772 feat(kv-offload): expose SimpleCPU offload metrics | #41780 [KV Offload] Expose SimpleCPU offload metrics | #41781 [KV Offload] Expose SimpleCPU offload metrics | #41790 [KV Offload] Expose SimpleCPU offload metrics | #43468 [BugFix][kv_offload] Populate BlockStored payloads for OffloadingConnector KV events

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: act.py`. - [x] Rename `abstract.py` to `base.py` (as well as in `cpu/policies`). - [x] Move `reuse_manager.py` into `cpu/manager.py`. - [x] Add `request_finished` method to `OffloadingManager`. - [ ] Remove `kv_offload/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ng backend - [x] CPU-GPU Offloading (NVIDIA+AMD) - [x] Custom offloading block size - [x] Fully asynchronous (cross-engine-steps) offloading / loading - [x] Immediate Offloading (as opposed to spill-over) - [x] LRU Evic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: viction - [x] Cross layer blocks - [x] Metrics - [x] Onloading preempted requests - [x] KV Events - [x] Kernel-block-size support - [x] Abstract eviction strategy (LRU, ARC, etc.) - [x] HMA Support Upcoming: - [ ] Docum...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pen Currently supported features: - [x] Pluggable out-of-tree offloading backend - [x] CPU-GPU Offloading (NVIDIA+AMD) - [x] Custom offloading block size - [x] Fully asynchronous (cross-engine-steps) offloading / loadin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Move CPU memory pinning to a background thread. performance frontend_api;quantization;scheduler_memory kernel memory_layout #41772 feat(kv-offload): expose SimpleCPU offload metrics | #41780 [KV Offload] Expose SimpleCP...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41772](https://github.com/vllm-project/vllm/pull/41772) | closes_keyword | 0.95 | feat(kv-offload): expose SimpleCPU offload metrics | Fixes part of #33689. |
| [#41780](https://github.com/vllm-project/vllm/pull/41780) | mentioned | 0.6 | [KV Offload] Expose SimpleCPU offload metrics | rather than adding a separate runtime-specific telemetry path. Refs #33689. ## Validation - `git diff --check`: passed - `py_compile` on changed Python files: passed - `tests/v1/s… |
| [#41781](https://github.com/vllm-project/vllm/pull/41781) | mentioned | 0.6 | [KV Offload] Expose SimpleCPU offload metrics | rather than adding a separate runtime-specific telemetry path. Refs #33689. ## Validation - `git diff --check`: passed - `py_compile` on changed Python files: passed - `tests/v1/s… |
| [#41790](https://github.com/vllm-project/vllm/pull/41790) | mentioned | 0.6 | [KV Offload] Expose SimpleCPU offload metrics | rather than adding a separate runtime-specific telemetry path. Refs #33689. ## Validation - `git diff --check`: passed - `py_compile` on changed Python files: passed - `tests/v1/s… |
| [#43468](https://github.com/vllm-project/vllm/pull/43468) | mentioned | 0.6 | [BugFix][kv_offload] Populate BlockStored payloads for OffloadingConnector KV events | publishes self-describing `BlockStored` events. Tracks part of RFC #33689 (KV Offloading Roadmap), whose "KV Events" item is already checked off; this PR corrects the `BlockStored… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
