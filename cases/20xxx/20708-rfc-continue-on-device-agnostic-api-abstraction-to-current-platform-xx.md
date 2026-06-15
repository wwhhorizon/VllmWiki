# vllm-project/vllm#20708: [RFC]: Continue on Device agnostic API abstraction to current_platform.XXX

| 字段 | 值 |
| --- | --- |
| Issue | [#20708](https://github.com/vllm-project/vllm/issues/20708) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;hardware_porting |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Continue on Device agnostic API abstraction to current_platform.XXX

### Issue 正文摘录

co-author with @jikunshang ### Motivation. This RFC is aiming to reuse `GPUWorker` and `GPUModelRunner` for any GPGPU devices, such as CUDA, ROCM and Intel GPU(aka: XPU). - By doing so, we can remove redundant duplication by adding a new XXXWorker/XXXModelRunner and derive from GPUWorker/GPUModelRunner - Any feature implemented in GPUWorker/GPUModelRunner such as logitsProcessor, samplingOutput optimization, spec_decode can be shared to all GPGPU hardware. **Status & Challenge** - Previous RFC from Huawei has made significant work done through - https://github.com/vllm-project/vllm/issues/9268 - Currently, `GPUWorker` and `GPUModelRunner` is assumed that it will only be used by CUDA and RocM, so hard-coded to cuda API will be used in above two files. Ex:torch.cuda.XXX or tensor.to('cuda') ### Proposed Change. 1. Add abstract API into platforms/interface.py and implement in cuda.py, rocm.py, xpu.py. 2. update any tensor.to('cuda') or tensor.cuda() to use tensor.to(current_platform.device). 3. Add a skip check in case of API mismatch. 4. Add static check to PR pre_commit to indicate future contributor to use current_platform instead calling torch.cuda directly. **Plan** 1. Add abstr...

## 现有链接修复摘要

#20751 [1/N] Refactor platform API to reduce `torch.cuda` call

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: to reuse `GPUWorker` and `GPUModelRunner` for any GPGPU devices, such as CUDA, ROCM and Intel GPU(aka: XPU). - By doing so, we can remove redundant duplication by adding a new XXXWorker/XXXModelRunner and derive from GP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: check and skip 10 | _lazy_init| ✅ | enable with alternative API 11 | _is_compiled | ✅| enable with alternative API 12 | _device_count_amdsmi| ✅ | enable with alternative API 13 | _device_count_nvml | ✅| enable with alte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Continue on Device agnostic API abstraction to current_platform.XXX RFC;stale co-author with @jikunshang ### Motivation. This RFC is aiming to reuse `GPUWorker` and `GPUModelRunner` for any GPGPU devices, such as CUDA,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -> `tensor.to(current_platform.device)` - [x] use `current_platform.dist_backend` for `init_worker_distributed_environment`. Done in #19410 3. add skip check - [ ] add `current_platform.is_graph_mode_supported()` - TBD...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e tensor.to(current_platform.device). 3. Add a skip check in case of API mismatch. 4. Add static check to PR pre_commit to indicate future contributor to use current_platform instead calling torch.cuda directly. **Plan*...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20751](https://github.com/vllm-project/vllm/pull/20751) | mentioned | 0.6 | [1/N] Refactor platform API to reduce `torch.cuda` call | _models.md` and `examples` for a new model. ## Purpose [1/N] of RFC #20708. this PR add several API in `Platform` class , such as `empty_cache`, `reset_peak_memory_stats`, `mem_ge… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
